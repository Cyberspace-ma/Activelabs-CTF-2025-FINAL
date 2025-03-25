import sys
import shlex
import subprocess
import os

# Function to get the figlet 'blacklist' text
def get_figlet_blacklist():
    try:
        # Run the figlet command to get the 'blacklist' header
        result = subprocess.check_output(['figlet', 'blacklist'], text=True)
        return result
    except subprocess.CalledProcessError as e:
        return f"Error generating figlet text: {e}"

sys.stdout.write(f"{get_figlet_blacklist()}\n")
sys.stdout.write("Welcome to the blacklist terminal challenge.\n")
sys.stdout.write("Only specific commands are allowed. The flag is in flag.txt, but can you get it?\n")
sys.stdout.flush()

def is_allowed_command(cmd):
    parts = shlex.split(cmd)

    # Allow `whoami` and `ls` commands
    if len(parts) == 1:
        if parts[0] == "whoami" or parts[0] == "ls":
            return True

    # Allow rev command only on flag.txt
    elif len(parts) == 2:
        if parts[0] == "rev" and parts[1] == "flag.txt":
            return True

    return False

while True:
    sys.stdout.write("$ ")
    sys.stdout.flush()
    try:
        command = sys.stdin.readline().strip()
    except UnicodeDecodeError:
        sys.stdout.write("Invalid input\n")
        sys.stdout.flush()
        continue
    if not command:
        break
    if command == "exit":
        break
    if is_allowed_command(command):
        parts = shlex.split(command)
        try:
            output = subprocess.check_output(parts, text=True)
            sys.stdout.write(output)
        except subprocess.CalledProcessError as e:
            sys.stdout.write(f"Error: {e}\n")
    else:
        sys.stdout.write("Hhhhh la walo\n")
    sys.stdout.flush()

