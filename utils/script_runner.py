import subprocess
import sys

def run_script(script, files):
    command = [sys.executable, script] + list(files)
    result = subprocess.run(command, capture_output=True, text=True)
    return result.stdout
