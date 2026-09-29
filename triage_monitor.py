import os
import hashlib
import time
from datetime import datetime, timedelta

# --- CONFIGURATION ---
TARGET_DIR = "./monitored_assets" 
LOG_FILE = "./forensic_triage_log.txt"
CYCLE_HOURS = 6 

def get_file_hash(file_path):
    hasher = hashlib.sha256()
    try:
        with open(file_path, 'rb') as f:
            while chunk := f.read(8192):
                hasher.update(chunk)
        return hasher.hexdigest()
    except Exception as e:
        return f"ERROR: {str(e)}"

def run_triage():
    print(f"[{datetime.now()}] Starting 6-hour forensic triage cycle...")
    time_threshold = datetime.now() - timedelta(hours=CYCLE_HOURS)
    cutoff_epoch = time_threshold.timestamp()
    changes_detected = 0

    if not os.path.exists(TARGET_DIR):
        os.makedirs(TARGET_DIR)
        print(f"-> Created dummy directory at '{TARGET_DIR}'. Place files here to test.")

    with open(LOG_FILE, "a") as log:
        for root, _, files in os.walk(TARGET_DIR):
            for file in files:
                file_path = os.path.join(root, file)
                try:
                    stat = os.stat(file_path)
                    modification_time = stat.st_mtime
                    if modification_time >= cutoff_epoch:
                        file_hash = get_file_hash(file_path)
                        mod_datetime = datetime.fromtimestamp(modification_time)
                        log_line = f"{datetime.now()} | MODIFIED: {file_path} | Last Mod: {mod_datetime} | SHA256: {file_hash}\n"
                        log.write(log_line)
                        print(f"-> Logged delta: {file}")
                        changes_detected += 1
                except Exception as e:
                    log.write(f"{datetime.now()} | ERROR accessing {file_path}: {str(e)}\n")

        if changes_detected == 0:
            log.write(f"{datetime.now()} | CYCLE PASS: No modifications found in the last {CYCLE_HOURS} hours.\n")
            print("-> Cycle complete. Zero deltas found. Minimal storage used.")
        else:
            print(f"-> Cycle complete. Logged {changes_detected} modified paths.")

if __name__ == "__main__":
    run_triage()
