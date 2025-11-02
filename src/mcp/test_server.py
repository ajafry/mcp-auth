"""
Test script for the MCP server.
This script demonstrates how to test the server locally.
"""

import requests
import json


def test_mcp_server():
    """Test the MCP server endpoints."""
    base_url = "http://localhost:8000"
    
    # Test server health
    try:
        response = requests.get(f"{base_url}/mcp")
        print(f"Server health check: {response.status_code}")
    except requests.exceptions.ConnectionError:
        print("Server is not running. Please start the server first.")
        return
    
    # Test add function
    test_add = {
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
    
    # Test subtract function
    test_subtract = {
        "jsonrpc": "2.0",
        "method": "tools/call",
        "params": {
            "name": "subtract",
            "arguments": {
                "a": 10.0,
                "b": 4.0
            }
        },
        "id": 2
    }
    
    # Test multiply function
    test_multiply = {
        "jsonrpc": "2.0",
        "method": "tools/call",
        "params": {
            "name": "multiply",
            "arguments": {
                "a": 7.0,
                "b": 6.0
            }
        },
        "id": 3
    }
    
    tests = [
        ("add", test_add, 8.7),
        ("subtract", test_subtract, 6.0),
        ("multiply", test_multiply, 42.0)
    ]
    
    for test_name, test_data, expected in tests:
        try:
            response = requests.post(
                f"{base_url}/mcp/v1/",
                json=test_data,
                headers={"Content-Type": "application/json"}
            )
            result = response.json()
            print(f"\nTest {test_name}:")
            print(f"Request: {test_data['params']['arguments']}")
            print(f"Response: {result}")
            print(f"Expected: {expected}")
            
            if response.status_code == 200 and "result" in result:
                actual = result["result"]["content"][0]["text"]
                print(f"Actual result: {actual}")
                print(f"Test {'PASSED' if float(actual) == expected else 'FAILED'}")
            else:
                print("Test FAILED - Invalid response")
                
        except Exception as e:
            print(f"Test {test_name} FAILED with error: {e}")


if __name__ == "__main__":
    print("Testing MCP Server...")
    test_mcp_server()