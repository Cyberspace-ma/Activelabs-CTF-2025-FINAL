#!/usr/bin/env python3
from pwn import *
import time

# Spiral transformation function
def spiral_dance(n, steps=0):
    if steps >= 6:
        return n
    if n < 10:
        return spiral_dance(n + 13, steps + 1)
    elif n > 100:
        return spiral_dance(n // 2 - 7, steps + 1)
    else:
        return spiral_dance(n * 3 % 137, steps + 1)

# Dynamic target
def generate_target():
    t = int(time.time())
    return (t % 50) + 42

# Find a winning number
def find_winning_number(target):
    # Try a larger range and debug outputs
    for i in range(0, 2000):  # Expanded range
        result = spiral_dance(i)
        if result == target:
            print(f"Debug: {i} transforms to {result}")
            return i
    print(f"Debug: No number found for target {target}")
    return None

def main():
    # Connection details
    host = "172.23.92.82"
    port = 1234
    
    # Connect to server
    r = remote(host, port)
    
    # Receive intro text until the prompt
    intro = r.recvuntil(b"Enter your number: ").decode()
    print(intro)
    
    # Calculate target
    target = generate_target()
    print(f"Calculated target: {target}")
    
    # Find winning number
    winning_num = find_winning_number(target)
    if winning_num is None:
        print("Couldn't find a winning number!")
        r.close()
        return
    
    print(f"Sending winning number: {winning_num}")
    
    # Send the number
    r.sendline(str(winning_num).encode())
    
    # Get response
    response = r.recvall(timeout=2).decode()
    print(response)
    
    r.close()

if __name__ == "__main__":
    main()