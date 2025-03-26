# Panel Writeup

This challenge was relatively straightforward due to the hidden hint embedded in the HTML source code:

```html
<!-- Hidden hint -->
<!-- 
TODO: Fix the request matcher in security middleware.
John mentioned something about CRLF but I don't see the issue?
-->
```

Based on this hint, we can deduce that the vulnerability may be related to CRLF (Carriage Return Line Feed) injection. To exploit this, we can use regular expressions (regex) to bypass the request matcher in the security middleware.

**Step 1: Finding the Bypass**

I used the following URL to successfully access the admin panel:

```
admin/index?param=%0d
```

The `%0d` is the URL-encoded version of the CR (Carriage Return) character, which seems to bypass the security check in place.

![panel](https://github.com/user-attachments/assets/c84039ab-6a3f-4843-a4c6-048ad5c540a8)

**Step 2: The Flag**

After successfully bypassing the security mechanism, I obtained the flag:

```
CSP{R3g3x_Byp4ss_Vuln_1n_M4tch3r}
```
