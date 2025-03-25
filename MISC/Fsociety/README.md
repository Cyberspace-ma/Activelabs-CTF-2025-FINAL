# fsociety Writeup

## Overview

In this challenge, I was provided with two files:
1. **darkwebradar_fsociety_report.pdf**: This document indicates that 37 data entries have been breached from the company **fsociety.com**.
2. **URL to Pastebin**: A URL, **https://pastebin.com/1jHW7VRT**, which previously contained critical information necessary for the task. However, the data has been removed from Pastebin.

## Steps to Solve

### 1. Analyze the Report

The **darkwebradar_fsociety_report.pdf** contains an overview of the breach, mentioning that **37 data** entries have been compromised. This report also provides a **contact number**, which will be used as a password for accessing the data.

### 2. Use the Password

The contact number provided in the report, **17894723455**, serves as the password to access the data in the **Pastebin** URL. However, the data from Pastebin has since been removed, so we cannot access it directly.

### 3. Extract MR Robot’s Password

Although the Pastebin data is no longer available, we know from the challenge description that **MR Robot's password** is included in the data. This password is encoded in **Base64** and serves as the **flag**.

### 4. Decode the Flag

The encoded flag **Q1NQe01yX1IwYjB0X3M0eXNfaDNsbDB9** was found as MR Robot's password. Decoding this Base64 string will give us the flag.

#### Example Command:
```bash
echo 'Q1NQe01yX1IwYjB0X3M0eXNfaDNsbDB9' | base64 --decode

CSP{Mr_R0b0t_s4ys_h3ll0}
