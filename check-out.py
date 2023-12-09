import signal
import psutil
import os

process_name = 'check-in.py'

def is_running(process_name):
    for proc in psutil.process_iter(["cmdline"]):
        if proc.info.get("cmdline", []):
            # Check if cmdline exists and contains items
            if process_name.lower() in proc.info["cmdline"]:
                print(True)
            return True
    print(False)
    return False

if is_running(process_name):
    # A process_id a futó folyamat azonosítója.
    process_id = psutil.Process(process_name).pid
    # A kill() parancs leállítja a folyamatot.
    os.kill(process_id, signal.SIGKILL)
