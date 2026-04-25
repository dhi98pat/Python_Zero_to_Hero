from datetime import datetime
def log(message: str):
    timestamp = datetime.utcnow().isoformat()
    print(f"[{timestamp}] {message}")