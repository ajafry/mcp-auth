# MCP auth with Azure Entra Id

A FastAPI-based application that demonstrates Azure AD authentication for both REST API endpoints and Model Context Protocol (MCP) servers. This project showcases how to secure APIs using Azure Active Directory OAuth2.1 authentication and implements mathematical operations through an MCP server.

## 🏗️ Project Structure

```
ApiMcpAuth/
├── README.md
├── requirements.txt
├── src/
│   ├── test.http              # HTTP test requests
│   ├── api/                   # FastAPI REST API
│   │   ├── auth.py           # Azure AD authentication setup
│   │   ├── main.py           # FastAPI application entry point
│   │   └── README.md
│   └── mcp/                   # Model Context Protocol server
│       ├── auth.py           # MCP authentication logic
│       ├── run_server.py     # MCP server runner
│       ├── server.py         # MCP server implementation
│       ├── test_server.py    # MCP server tests
│       └── README.md
```

## 🚀 Features

### FastAPI REST API
- **Azure AD Authentication**: Secure endpoints using Azure Active Directory OAuth2
- **CORS Support**: Cross-origin resource sharing enabled
- **Swagger UI Integration**: Interactive API documentation with OAuth2 flow
- **Mathematical Operations**: Simple endpoints for basic calculations

### MCP Server
- **Remote MCP Server**: FastMCP-based server for mathematical operations
- **Role-based Authorization**: Different access levels (admin, user)
- **JWT Token Validation**: Secure MCP tool access
- **Mathematical Tools**: Add, subtract, and multiply operations

## 🛠️ Prerequisites

- Python 3.8+
- [uv](https://github.com/astral-sh/uv) package manager
- Azure AD application registration
- Valid Azure AD tenant

## ⚙️ Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd ApiMcpAuth
   ```

2. **Install dependencies using uv**:
   ```bash
   uv sync
   ```

   Or install from requirements.txt:
   ```bash
   uv pip install -r requirements.txt
   ```

## 🔧 Configuration

1. **Create a `.env` file** in the root directory:
   ```bash
   # Copy the example environment file and customize it
   cp .env.example .env
   ```
   
   Then edit the `.env` file with your actual Azure AD values:
   ```env
   # Azure AD Configuration
   TENANT_ID=your-azure-tenant-id
   API_CLIENT_ID=your-api-application-client-id
   MCP_CLIENT_ID=your-mcp-client-id
   
   # Scopes
   SCOPE=api://your-app-id/User.CallApi
   API_SCOPES={"api://your-app-id/User.CallApi": "User.CallApi"}
   ```

2. **Azure AD Application Setup**:
   - Register an application in Azure AD
   - Configure redirect URIs for OAuth2 flow
   - Set up API permissions and scopes
   - Note down the tenant ID and client IDs

## 🏃‍♂️ Running the Application

### FastAPI REST API

1. **Navigate to the API directory**:
   ```bash
   cd src/api
   ```

2. **Run the FastAPI server**:
   ```bash
   uv run python main.py
   ```
   
   Or using uvicorn directly:
   ```bash
   uv run uvicorn main:app --host 0.0.0.0 --port 8000 --reload
   ```

3. **Access the application**:
   - API: http://localhost:8000
   - Swagger UI: http://localhost:8000/docs
   - ReDoc: http://localhost:8000/redoc

### MCP Server

1. **Navigate to the MCP directory**:
   ```bash
   cd src/mcp
   ```

2. **Run the MCP server**:
   ```bash
   uv run python run_server.py
   ```

## 📚 API Endpoints

### Public Endpoints
- `GET /hello/{name}` - Simple greeting endpoint (no authentication required)

### Protected Endpoints (require Azure AD authentication)
- `GET /add/{num1}/{num2}` - Add two numbers
- `GET /mcp/` - MCP integration endpoint

### MCP Tools
- `add(a, b)` - Add two numbers (requires admin role)
- `subtract(a, b)` - Subtract two numbers
- `multiply(a, b)` - Multiply two numbers

## 🧪 Testing

Use the provided test files:

1. **HTTP Tests**: Use [`src/test.http`](src/test.http) with your HTTP client
2. **MCP Tests**: Run the MCP server tests:
   ```bash
   cd src/mcp
   uv run python test_server.py
   ```

## 🔐 Authentication Flow

1. **OAuth2 Authorization Code Flow**: Used for web applications
2. **JWT Token Validation**: Bearer tokens validated against Azure AD
3. **Role-based Access**: Different endpoints require different roles
4. **PKCE Support**: Enhanced security for public clients

## 🛡️ Security Features

- **Token Validation**: JWT tokens validated with Azure AD public keys
- **Role-based Authorization**: Fine-grained access control
- **CORS Protection**: Configurable cross-origin policies
- **Secure Headers**: Standard security headers included

## 🔍 Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `TENANT_ID` | Azure AD tenant identifier | Yes |
| `API_CLIENT_ID` | API application client ID | Yes |
| `MCP_CLIENT_ID` | MCP client ID (can be same as API_CLIENT_ID) | Yes |
| `API_SCOPES` | JSON object of API scopes | Yes |
| `SCOPE` | OAuth2 scope for API access | Yes |

## 🚨 Troubleshooting

### Common Issues

1. **Authentication Errors**:
   - Verify Azure AD configuration
   - Check client IDs and tenant ID
   - Ensure scopes are correctly configured

2. **CORS Issues**:
   - Check CORS middleware configuration
   - Verify allowed origins in production

3. **Token Validation Failures**:
   - Ensure tokens are not expired
   - Verify audience claims match client ID

### Logging

The application uses structured logging. Check logs for detailed error information:
- API logs: Console output when running the FastAPI server
- MCP logs: Console output when running the MCP server

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

[Add your license information here]

## 🔗 Dependencies

- **FastAPI**: Modern, fast web framework for building APIs
- **fastapi-azure-auth**: Azure AD authentication for FastAPI
- **FastMCP**: Model Context Protocol server implementation
- **python-dotenv**: Environment variable management
- **MSAL**: Microsoft Authentication Library
- **PyJWT**: JSON Web Token implementation