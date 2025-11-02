from typing import List
from fastapi import HTTPException
import jwt
import logging
from pydantic import BaseModel
import os

from dotenv import load_dotenv

load_dotenv()

logger = logging.getLogger(__name__)

# Azure AD configuration
AZURE_TENANT_ID = os.getenv("TENANT_ID")
AZURE_CLIENT_ID = os.getenv("API_CLIENT_ID")

class UserClaims(BaseModel):
    """User claims extracted from JWT token."""
    def __init__(self, token_payload: dict):
        self.payload = token_payload
        self.username = token_payload.get('preferred_username', 'Unknown')
        self.user_id = token_payload.get('oid')
        self.roles = self._extract_roles(token_payload)
    
    def _extract_roles(self, payload: dict) -> List[str]:
        """Extract roles from token."""
        roles = []
        if 'roles' in payload:
            roles.extend(payload['roles'])
        if 'scp' in payload:
            roles.extend(payload['scp'].split(' '))
        return [role.lower() for role in roles]
    
    def has_role(self, required_role: str) -> bool:
        return required_role.lower() in self.roles

def validate_token(token: str) -> UserClaims:
    """Validate token - simple version."""
    try:
        # Decode without verification (development mode)
        payload = jwt.decode(token, options={"verify_signature": False})
        
        # Basic validation
        if payload.get('aud') != AZURE_CLIENT_ID:
            raise HTTPException(401, "Invalid audience")
        
        return UserClaims(payload)
    except Exception as e:
        raise HTTPException(401, f"Invalid token: {e}")

# Global user context
current_user: UserClaims = None

def require_auth(role: str = "user"):
    """Simple auth decorator."""
    def decorator(func):
        def wrapper(*args, **kwargs):
            if not current_user:
                raise HTTPException(401, "Authentication required")
            if not current_user.has_role(role):
                raise HTTPException(403, f"Required role: {role}")
            return func(*args, **kwargs)
        return wrapper
    return decorator