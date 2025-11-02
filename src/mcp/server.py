"""
Remote MCP Server with FastMCP using Streamable HTTP protocol.
Exposes three mathematical operations: add, subtract, and multiply.
"""

from fastmcp import FastMCP
from fastapi import Request
from typing import Union
from auth import validate_token, require_auth
import logging

# Initialize FastMCP server
mcp = FastMCP("Math Operations Server")

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

@mcp.tool()
@require_auth("admin")
def add(a: float, b: float) -> float:
    """
    Add two numbers together.
    
    Args:
        a: First number
        b: Second number
        
    Returns:
        The sum of a and b
    """
    result = a + b
    return result


@mcp.tool()
def subtract(a: float, b: float) -> float:
    """
    Subtract the second number from the first number.
    
    Args:
        a: First number (minuend)
        b: Second number (subtrahend)
        
    Returns:
        The difference of a and b (a - b)
    """
    result = a - b
    return result


@mcp.tool()
def multiply(a: float, b: float) -> float:
    """
    Multiply two numbers together.
    
    Args:
        a: First number
        b: Second number
        
    Returns:
        The product of a and b
    """
    result = a * b
    return result


# Create the HTTP app from the MCP instance using streamable-http transport
app = mcp.http_app(transport="streamable-http")

# # Add a health check endpoint (no auth required)
# @app.get("/health")
# async def health_check():
#     return {"status": "healthy", "service": "MCP Math Server with RBAC"}

# # Add an endpoint to check user roles (useful for debugging)
# @app.get("/user/roles")
# async def get_user_roles(user: UserClaims = Depends(verify_token)):
#     return {
#         "username": user.username,
#         "user_id": user.user_id,
#         "roles": user.roles,
#         "raw_payload": user.payload
#     }

@app.middleware("http")
async def auth_middleware(request: Request, call_next):
    global current_user
    current_user = None
    
    if request.url.path == "/mcp":
        auth_header = request.headers.get("authorization", "")
        if auth_header.startswith("Bearer "):
            try:
                token = auth_header[7:]
                current_user = validate_token(token)
            except:
                pass  # Let tools handle auth errors
    
    return await call_next(request)

if __name__ == "__main__":
    # Run the server directly using FastMCP's run method with streamable-http transport
    mcp.run(
        transport="streamable-http",
        host="0.0.0.0",
        port=8000
    )