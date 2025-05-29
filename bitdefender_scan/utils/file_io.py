import json

def save_scan_logs(logs, filepath):
    with open(filepath, "w") as f:
        for eid, data in logs:
            f.write(f"Endpoint ID: {eid}\n")
            f.write(json.dumps(data, indent=2))
            f.write("\n" + "="*80 + "\n\n")

def load_prompt(path):
    with open(path, "r") as f:
        return f.read()
