from apis.auth import get_auth_header
from apis.endpoints import fetch_endpoints, fetch_scan_logs
from utils.file_io import save_scan_logs, load_prompt
from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage
import json

# Fetch data
auth_header = get_auth_header()
endpoints = fetch_endpoints(auth_header)
scan_logs = fetch_scan_logs(endpoints, auth_header)

# Save to file
save_scan_logs(scan_logs, "logs/scan_logs.txt")

# Analyze with LLM
llm = ChatOllama(model="mistral:7b", temperature=0.5, num_predict=-1)
prompt_template = load_prompt("prompts/analyze_logs.txt")

# Convert scan logs list to a readable string for the LLM
scan_logs_text = ""
for eid, log in scan_logs:
    scan_logs_text += f"Endpoint ID: {eid}\n"
    scan_logs_text += json.dumps(log, indent=2)
    scan_logs_text += "\n" + "="*80 + "\n\n"

# Create full prompt
prompt_text = prompt_template + scan_logs_text


response = llm.invoke([HumanMessage(content=prompt_text)])

# Output or save
print("LLM Response:")
print(response.content)

with open("logs/analysis_report.txt", "w") as f:
    f.write(response.content)
