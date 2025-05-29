import requests
import json

API_URL = "https://cloudgz.gravityzone.bitdefender.com/api/v1.0/jsonrpc/network"

def fetch_endpoints(auth_header):
    payload = {
        "params": {},
        "jsonrpc": "2.0",
        "method": "getEndpointsList",
        "id": "301f7b05-ec02-481b-9ed6-c07b97de2b7b"
    }
    response = requests.post(API_URL, json=payload, verify=False, headers=auth_header)
    return response.json()["result"]["items"]

def fetch_scan_logs(endpoints, auth_header):
    logs = []
    for item in endpoints:
        eid = item.get("id")
        if not eid:
            continue
        payload = {
            "params": {"endpointId": eid},
            "options": {"includeScanLogs": True},
            "jsonrpc": "2.0",
            "method": "getManagedEndpointDetails",
            "id": "301f7b05-ec02-481b-9ed6-c07b97de2b7b"
        }
        response = requests.post(API_URL, json=payload, verify=False, headers=auth_header)
        data = response.json()
        logs.append((eid, data))
    return logs
