#  Blacklist Terminal Writeup

## Overview
This challenge involves interacting with a restricted terminal environment where only specific commands are allowed. The goal is to find the flag hidden in the `flag.txt` file. However, only a subset of commands can be executed, and any attempt to execute unauthorized commands will result in a denial message.

## Key Features:
1. **Allowed Commands:**
   - `whoami`: Displays the current user.
   - `ls`: Lists the files in the current directory.
   - `rev flag.txt`: Reverses the contents of the `flag.txt` file (this is the key to obtaining the flag).
   
2. **Restricted Commands:** Any command other than the ones specified will be rejected with a message saying "Hhhhh la walo."

3. **Objective:** The user must figure out how to use the allowed commands to reveal the flag stored in `flag.txt`.

## Challenge Analysis:
1. The script runs a terminal interface with a prompt (`$ `), awaiting user input.
2. The function `is_allowed_command` checks if the entered command is either `whoami`, `ls`, or the special `rev flag.txt`.
3. Commands outside of this list will trigger a rejection response.

## Steps to Solve:
1. Enter `rev flag.txt` in the terminal. This command will reverse the contents of `flag.txt` and reveal the flag.
2. Use other allowed commands like `whoami` and `ls` to explore and gather additional information if necessary.

## Solution:
- The flag is in the `flag.txt` file. By running the allowed command `rev flag.txt`, the contents of the file will be reversed, revealing the flag.

## Example Interaction:
```
$ rev flag.txt
}3r4mthg1n_4_s1_5dn4mm0c_ts1l_kc4lB{PSC
```

In this case, reversing the contents of `flag.txt` would reveal the flag, which can be read from the output.
