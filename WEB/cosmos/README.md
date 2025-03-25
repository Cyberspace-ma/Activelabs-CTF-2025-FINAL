### **Challenge Overview**

The challenge revolves around identifying weak passwords, bypassing a WAF, and successfully executing a Base64-encoded SQL injection. The goal is to retrieve a flag stored in the administrator account.

---

### **Step 1: Logging In**

1. **Start Point**:
    
    - On the challenge page, you see several cards. One of them is labeled "Cosmos," containing the following hint:
        
        > "The Cosmos project explores the universe's wonders, but during development, the password was accidentally exposed. When checked on Have I Been Pwned, it was found that 'This password has been seen 10,437,277 times before,' highlighting the critical need for strong password practices and vigilance."
        
    - This suggests that the username is `cosmos` and that the password is one of the most commonly used weak passwords.
![Pasted image 20250110121126](https://github.com/user-attachments/assets/0e3b7925-b1cc-43a4-af1b-3acdf7f40ab7)

1. **Testing Credentials**:
    
    - Based on the hint, try `cosmos:password` in the username and password, which works.
3. **Outcome**:
    
    - Upon successful login, a new menu item labeled **"cosmos"** appears in the header.
![Pasted image 20250110121203](https://github.com/user-attachments/assets/c4137c7a-61b3-4c7f-a339-5f27fbf75cf7)


---

### **Step 2: Exploring the "cosmos" Path**

1. **Navigating the New Path**:
    
    - Clicking the "cosmos" link redirects you to a search page with a text input box. You can input queries, but any attempt at standard SQL injection or text-based queries fails due to the Web Application Firewall (WAF).
![Pasted image 20250110121126](https://github.com/user-attachments/assets/4a13a812-405e-41ce-a91a-35399775fffc)

1. **Identifying the WAF Restriction**:
    
    - After several failed attempts, observe that only Base64-encoded inputs do not get blocked.
    - For example, if you input `U0VMRUNUIDEgRlJPTSB1c2VycyE=` (Base64 for `SELECT 1 FROM users!`), you get a response indicating that the query was processed.

---

### **Step 3: Bypassing the WAF**

1. **Encoding SQL Queries**:
    
    - To bypass the WAF, encode your SQL queries in Base64.
    - For example, encoding `SELECT username, password FROM users;` results in the Base64 string:  
        `U0VMRUNUIHVzZXJuYW1lLCBwYXNzd29yZCBGUk9NIHVzZXJzOw==`
2. **Testing Queries**:
    
    - When this Base64-encoded query is entered, the system processes it and returns the **username** and **password** for all users in the database.
3. **Outcome**:
    
    - The query outputs a table with user credentials. Notably, the table includes the **administrator** account and its password.
![Pasted image 20250110120941](https://github.com/user-attachments/assets/7c37b1de-7b15-4635-929c-22a29414f9ba)


---

### **Step 4: Logging In as Administrator**

1. **Using Admin Credentials**:
    
    - Use the retrieved administrator username and password to log in to the admin portal.
![Pasted image 20250110121014](https://github.com/user-attachments/assets/9fd1c174-d7a6-4117-b64b-64c0ef257c33)


1. **Flag Retrieval**:
    
    - Upon successful login, the flag is displayed.
    
![Pasted image 20250110121036](https://github.com/user-attachments/assets/73ff60b7-c062-4550-8aa4-22301a972333)

---
### **Flag**

Congratulations! You have successfully completed the "Cosmos" challenge and retrieved the flag. 🎉
