import pandas as pd
from mcp.server.fastmcp import FastMCP
from apis.auth import get_auth_header
from apis.endpoints import fetch_endpoints, fetch_scan_logs
from utils.file_io import save_scan_logs, load_prompt

# Create an MCP server
mcp = FastMCP("Demo")

@mcp.tool(name="get_log_data", description="Retrieve scan logs for all endpoints to analyze for suspicious activity.")
def get_log_data():
    auth_header = get_auth_header()
    endpoints = fetch_endpoints(auth_header)
    scan_logs = fetch_scan_logs(endpoints, auth_header)

    # Save to file
    save_scan_logs(scan_logs, "logs/scan_logs.txt")
    return scan_logs

mcp.run(transport="streamable-http")