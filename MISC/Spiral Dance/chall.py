#!/usr/bin/env python3
import os
import sys
from time import time

# Hidden flag
FLAG = "CSP{Sp1r4l_D4nc3r_w4s_fun_1sn_it}"

# Spiral transformation function
def spiral_dance(n, steps=0):
    if steps >= 6:
        return n
    if n < 10:
        return spiral_dance(n + 13, steps + 1)  # Small numbers jump outward
    elif n > 100:
        return spiral_dance(n // 2 - 7, steps + 1)  # Big numbers spiral inward
    else:
        return spiral_dance(n * 3 % 137, steps + 1)  # Middle numbers twist

# Dynamic target based on time
def generate_target():
    t = int(time())
    return (t % 50) + 42  # Target between 42 and 91

# Main game logic
def play_spiral(user_input):
    try:
        guess = int(user_input.strip())
        if guess < 0:
            return "No negative numbers allowed in the spiral!"
        
        result = spiral_dance(guess)
        target = generate_target()
        
        # Winning condition
        if result == target:
            return f"You’ve danced to the center! Flag: {FLAG}"
        else:
            # Hint: how many steps off
            diff = abs(result - target)
            return f"Off the mark! Landed at {result}, target was {target}. Difference: {diff}"
    except ValueError:
        return "Invalid input! Enter a number."

def main():
    # Unbuffered stdout for socat
    sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', buffering=1)
    
    # Game intro
    print("Welcome to the Spiral Dance!")
    print("Enter a number to start your journey through the spiral.")
    print("Small numbers (<10) leap +13, big numbers (>100) halve and drop 7,")
    print("and mid-range numbers twist with *3 % 137.")
    print("Land exactly on the time-shifting target to win!")
    print("Enter your number: ", end="")
    
    # Get user input
    user_input = input().strip()
    
    # Run the game
    result = play_spiral(user_input)
    print(result)

if __name__ == "__main__":
    main()
