import base64

def get_auth_header():
    api_key = "0743d3ed68811c657a27fafebac7d29b036cbb38f7b90905210338e17b773eca"
    token = base64.b64encode(f"{api_key}:".encode()).decode("utf-8")
    return {
        "Content-Type": "application/json",
        "Authorization": f"Basic {token}"
    }
