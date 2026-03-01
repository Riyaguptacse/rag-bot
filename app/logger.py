import json
import os

LOG_FILE = "../chat_logs.json"

def log_message(question, answer):
    # Load existing logs
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r", encoding="utf-8") as f:
            logs = json.load(f)
    else:
        logs = []

    # Append new entry
    logs.append({"question": question, "answer": answer})

    # Save back to file
    with open(LOG_FILE, "w", encoding="utf-8") as f:
        json.dump(logs, f, indent=4)