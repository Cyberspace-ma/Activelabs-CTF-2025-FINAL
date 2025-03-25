# Cracked Writeup

## Overview

In this challenge, you need to find the last user who joined the Cracking forum website, **Cracked.io**. The flag format is `CSP{username}`, where `username` is the last registered user. This is important for our investigation.

## Steps to Solve

We will use the **Wayback Machine** from [archive.org](https://web.archive.org/) to find the last user registered on the website.

### Step 1: Go to the Wayback Machine

1. Open the website [https://web.archive.org/web/](https://web.archive.org/web/) in your browser.
2. Type **cracked.io** in the search bar and press Enter.
3. Look at the different snapshots (saved versions) of the website.

### Step 2: Find the Snapshot from the Right Date

We need to find a snapshot of the website just before the **FBI seized the website**. According to the challenge, the important date is **January 28, 2025, at 23:33:33**. 

1. Find the snapshot closest to **January 28, 2025**, at **23:33:33**.
2. Click on that snapshot to see how the website looked at that time.

![cracked](https://github.com/user-attachments/assets/e02c3dcd-b164-4ca9-bce6-5b4367f50c14)


### Step 3: Find the Last User

Look at the website in the snapshot and find where it shows the users who registered. The last user shown is the one who joined just before the snapshot was taken.

1. In this case, the last user who joined is **Klyrt**.
   
![last user joined](https://github.com/user-attachments/assets/d29eba23-7ed8-44df-930b-fb67c1aeb3d7)


### Step 4: Submit the Flag

The flag format is `CSP{username}`. So, the flag for this challenge is:

**CSP{Klyrt}**
