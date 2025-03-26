# Sada9at Writeup

This challenge was vulnerable to **Local File Inclusion (LFI)** in the user registration feature. Here's how the vulnerability can be exploited:

**Step 1: Registering a User**

To trigger the LFI, you need to register a user with a special payload in the username or another input field. In this case, I used the following payload:

```
../flag.txt
```

**Step 2: Logging In**

Once the user is registered, log in with the newly created account.

**Step 3: Accessing the Profile**

After logging in, navigate to the "View Profile" section. Due to the LFI vulnerability, the application attempts to include the `../flag.txt` file, which contains the flag.

**Result: The Flag**

Upon accessing the profile, the flag is revealed:

```
CSP{Allah_yt4kabal_s1yamakom}
```
