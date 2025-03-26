**Challenge Overview:**

This challenge revolves around an AWS S3 bucket misconfiguration. When I initially created the bucket, I mistakenly made it public, allowing anyone to access it. You can easily access the bucket using the AWS CLI or simply by visiting the URL in your browser.

**Step 1: Initial Access**

At first glance, the website may seem secure with no visible vulnerabilities. However, upon closer inspection, you notice that some of the links are requesting images from an AWS S3 bucket.

![epictv](https://github.com/user-attachments/assets/52fedf64-e03e-45fc-94f0-163830130fe0)


**Step 2: Discovering the Secret File**

By accessing one of these links, you will be directed to a file named `secret.txt` stored within the S3 bucket.

![link](https://github.com/user-attachments/assets/91ada2ab-b942-47ed-bb0f-6a6e29dde2be)


**Step 3: Decoding the Secret**

When you open `secret.txt` in your browser, you will find a secret string encoded in Base64 format.

![link](https://github.com/user-attachments/assets/04efe689-3749-4df1-802f-d808785717d3)


The string looks like this:

```
Q1NQe0FXU18xc19UaDNfQjNzdF9DbDB1ZF9TM3J2MWMzc19idXRfc3QxbGxfYzRuX2IzX20xc2MwbmYxZ3VyM2R9
```

To decode it, you can use the following command in your terminal:

```bash
echo "Q1NQe0FXU18xc19UaDNfQjNzdF9DbDB1ZF9TM3J2MWMzc19idXRfc3QxbGxfYzRuX2IzX20xc2MwbmYxZ3VyM2R9" | base64 --decode
```

**Step 4: Final Flag**

Running the above command will decode the string, revealing the flag:

```
CSP{AWS_1s_Th3_B3st_Cl0ud_S3rv1c3s_but_st1ll_c4n_b3_m1sc0nf1gur3d}
```
