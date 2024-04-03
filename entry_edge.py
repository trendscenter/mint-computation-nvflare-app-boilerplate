import subprocess
import time
import psutil
import sys  # Ensure sys is imported for sys.exit()

# Start the shell script
print("Starting the shell script...")
subprocess.Popen(["/bin/bash", "/workspace/runKit/startup/start.sh"])

# Wait a few seconds to give the nvflare process time to start
time.sleep(10)  # Adjust this delay as needed

print("Polling for nvflare process and printing process details for debugging...")
while True:
    process_found = False
    for proc in psutil.process_iter(attrs=['cmdline']):
        cmdline = ' '.join(proc.info['cmdline']) if proc.info['cmdline'] else ''
        if 'nvflare' in cmdline:
            process_found = True
            print("nvflare process is running...")
            break  # Exit the loop if nvflare process is found
    
    if process_found:
        time.sleep(10)  # Check every 10 seconds
    else:
        print("nvflare process is not running anymore or not found. Exiting.")
        sys.exit(0)  # Exit the script
