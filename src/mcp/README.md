# MCP Math Operations Server

This is a remote MCP (Model Context Protocol) server built with FastMCP that uses the Streamable HTTP protocol. The server exposes three mathematical operations: add, subtract, and multiply.

## Features

- **Add**: Adds two numbers together
- **Subtract**: Subtracts the second number from the first
- **Multiply**: Multiplies two numbers together
- Built with FastMCP for easy MCP protocol implementation
- Uses Streamable HTTP for real-time communication
- RESTful API endpoints
- JSON-RPC 2.0 protocol support

## Installation

1. Make sure you have Python 3.7+ installed
2. Install the required dependencies from the root directory:

```bash
pip install -r ../../requirements.txt
```

## Running the Server

### Option 1: Direct execution
```bash
python server.py
```

### Option 2: Using the startup script
```bash
python run_server.py
```

The server will start on `http://localhost:8000` using the Streamable HTTP protocol.

## API Endpoints

### Health Check
- **GET** `/` - Server health check

### MCP Protocol Endpoint
- **POST** `/mcp/v1/` - Main MCP protocol endpoint

## Available Tools

### 1. Add
Adds two numbers together.

**Parameters:**
- `a` (float): First number
- `b` (float): Second number

**Returns:** The sum of a and b

### 2. Subtract
Subtracts the second number from the first number.

**Parameters:**
- `a` (float): First number (minuend)
- `b` (float): Second number (subtrahend)

**Returns:** The difference of a and b (a - b)

### 3. Multiply
Multiplies two numbers together.

**Parameters:**
- `a` (float): First number
- `b` (float): Second number

**Returns:** The product of a and b

## Testing

Run the test script to verify the server is working correctly:

```bash
python test_server.py
```

Make sure the server is running before executing the tests.

## Example Usage

### JSON-RPC Request Example

```json
{
    "jsonrpc": "2.0",
    "method": "tools/call",
    "params": {
        "name": "add",
        "arguments": {
            "a": 5.5,
            "b": 3.2
        }
    },
    "id": 1
}
```

### Response Example

```json
{
    "jsonrpc": "2.0",
    "result": {
        "content": [
            {
                "type": "text",
                "text": "8.7"
            }
        ]
    },
    "id": 1
}
```

## Integration with MCP Clients

This server can be integrated with any MCP-compatible client. The server URL for integration is:

```
http://localhost:8000/mcp/v1/
```

## Development

The server is built using:
- **FastMCP**: For MCP protocol implementation
- **FastAPI**: For HTTP server functionality
- **Uvicorn**: For ASGI server
- **Streamable HTTP**: For real-time communication protocol

## Configuration

The server runs on:
- **Host**: 0.0.0.0 (accepts connections from any IP)
- **Port**: 8000
- **Reload**: Enabled (automatically reloads on code changes)

You can modify these settings in the `server.py` or `run_server.py` files.