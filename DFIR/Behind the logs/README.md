# Description :

> A major financial institution suffered a critical security breach in their client database. Hackers exfiltrated sensitive credit card information belonging to over 500 high-profile clients. The breach went undetected for hours until a security analyst, reviewing alerts in the bank’s SIEM system, flagged a suspicious event. The forensic team quickly extracted logs from the SIEM. Can you help the SOC team determine how this happened !!!

> Author : Mr_Togoo


During our analysis, we discovered a malicious IP, 184.105.247.238. We filtered its requests and found multiple attempts. After further investigation, we identified that the attacker successfully entered the system and pulled data using Git.

Since Git is the shell for GitHub, we examined the log and found the following entry:

```
{
    "timestamp": "2025-01-23 09:30:15",
    "method": "POST",
    "url": "/MrTogoo/WebServer",
    "query": "cmd=git pull origin master",
    "protocol": "HTTP/1.1",
    "ip": "184.105.247.238",
    "user_agent": "curl/7.88.1",
    "status_code": 200,
    "response_size": 274,
    "error_code": 0,
    "duration_ms": 1578
}
```

We then searched GitHub for the repository `/MrTogoo/WebServer`, where we found a PowerShell script. 


```powershell
function Find-CardFile {
    Write-Host "Searching for target file (cards.txt)..." -ForegroundColor Yellow
    $searchPaths = @(
        "$env:USERPROFILE\Desktop",
        "$env:USERPROFILE\Documents",
        "C:\"
    )

    foreach ($path in $searchPaths) {
        $file = Get-ChildItem -Path $path -Filter "cards.txt" -Recurse -ErrorAction SilentlyContinue | Select-Object -First 1
        if ($file) {
            Write-Host "Target file located: $($file.FullName)" -ForegroundColor Green
            return $file.FullName
        }
    }
    return $null
}

$cardFile = Find-CardFile

if ($cardFile) {
    Write-Host "Initiating credit extraction..." -ForegroundColor Yellow
    Start-Sleep -Seconds 2

    $breachedData = Get-Content $cardFile
    $totalCards = $breachedData.Count

    Write-Host "Extraction successful! Retrieved $totalCards credit records." -ForegroundColor Red
    Write-Host "Dumping extracted credit data..." -ForegroundColor Cyan
    Start-Sleep -Seconds 1

    Write-Host "Sample of extracted data:" -ForegroundColor White
    $breachedData | Select-Object -First 5 | ForEach-Object {
        Write-Host $_ -ForegroundColor Magenta
    }

    Write-Host "`nAnalyzing extracted credit card numbers..." -ForegroundColor Yellow
    Start-Sleep -Seconds 2

    $visaCount = ($breachedData | Where-Object { $_ -like "4*" }).Count
    $mastercardCount = ($breachedData | Where-Object { $_ -like "5*" }).Count
    $amexCount = ($breachedData | Where-Object { $_ -like "3*" }).Count
    $discoverCount = ($breachedData | Where-Object { $_ -like "6*" }).Count

    Write-Host "Breakdown of card types:" -ForegroundColor White
    Write-Host "Visa: $visaCount" -ForegroundColor Green
    Write-Host "Mastercard: $mastercardCount" -ForegroundColor Green
    Write-Host "American Express: $amexCount" -ForegroundColor Green
    Write-Host "Discover: $discoverCount" -ForegroundColor Green

    $outputFile = "extracted_cards_$(Get-Date -Format 'yyyyMMdd_HHmmss').txt"
    $breachedData | Out-File $outputFile
    Write-Host "`nData temporarily saved to $outputFile." -ForegroundColor Yellow

    Write-Host "Establishing connection to external server..." -ForegroundColor Cyan
    Start-Sleep -Seconds 2

    $Server = "https://pastebin.com/hugnTkxk"
    Write-Host "Uploading data to $Server..." -ForegroundColor Red
    Start-Sleep -Seconds 3

    try {
        Write-Host "Transferring $totalCards records..." -ForegroundColor White
        Start-Sleep -Seconds 2
        Write-Host "Upload successful! Data transferred to external server." -ForegroundColor Green
    } catch {
        Write-Host "Error during upload: $($_.Exception.Message)" -ForegroundColor Red
    }

    Write-Host "Cleaning up local traces..." -ForegroundColor Yellow
    Remove-Item $outputFile -Force
    Start-Sleep -Seconds 1
    Write-Host "Local file $outputFile deleted." -ForegroundColor Green
    Write-Host "Credit extraction complete. No real systems were harmed." -ForegroundColor Green
} else {
    Write-Host "Error: cards.txt not found on the system." -ForegroundColor Red
    Write-Host "Ensure the file exists in Desktop, Documents, or C:\ with credit card numbers in the format: XXXX-XXXX-XXXX-XXXX-XXXXXX" -ForegroundColor Yellow
}
```


Upon analyzing it, we discovered that it contained a C2 server that was exfiltrating data, leading to a data breach.

`https://pastebin.com/hugnTkxk`

When we opened the link, we discovered the data breach, which contained over 500 credit card details.


![image](https://github.com/user-attachments/assets/9b6aa937-01bf-416a-840c-77aa0152731d)



And congrats , you got the flag!!!

FLAG : 
>CSP{L0gs_3s3nt13l_1n_S0C}
