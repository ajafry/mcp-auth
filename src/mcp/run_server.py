"""
Startup script for the MCP server.
Run this script to start the server on localhost:8000
"""

import sys
import os

# Add the current directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from server import mcp

if __name__ == "__main__":
    print("Starting MCP Server...")
    print("Server will be available at: http://localhost:8000")
    print("MCP endpoint will be at: http://localhost:8000/mcp/v1/")
    print("Press Ctrl+C to stop the server")
    
    # Run the server directly using FastMCP's run method with streamable-http transport
    mcp.run(
        transport="streamable-http",
        host="0.0.0.0",
        port=8000
    )