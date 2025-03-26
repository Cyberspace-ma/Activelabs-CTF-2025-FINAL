# Description :

> I found it difficult to play against Mr_Togoo. Please help me win against him. I hope for you a good game !!!!!!
> 

> Author : Mr_Togoo


During the analysis challenge, you found a function that gives you the flag only if the value of `TogooHealth` is 0.

But, you can extract the flag directly from the binary, so we can create a script to solve this challenge.

```
def decrypt_flag(encrypted_bytes):
    return bytes(b ^ 0xB2 for b in encrypted_bytes)


encrypted_flag = bytes([
    0xF1, 0xE1, 0xE2, 0xC9, 0xEB, 0x82, 0xE7, 0xED, 
    0x86, 0xE0, 0x81, 0xED, 0xF5, 0x82, 0x82, 0xF6, 
    0xED, 0xF5, 0x86, 0xFF, 0x81, 0xE0, 0x93, 0x93, 
    0x93, 0xCF
])


decrypted_flag = decrypt_flag(encrypted_flag)
print("This is you flag: ", decrypted_flag.decode('utf-8'))
```
Output: 

`This is you flag:  CSP{Y0U_4R3_G00D_G4M3R!!!}`

And congrats , you got the flag!!!

FLAG : 
>CSP{Y0U_4R3_G00D_G4M3R!!!}
