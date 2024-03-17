
---
---

<div align="center">

# TryHackMe OhSINT


<img src="https://tryhackme-images.s3.amazonaws.com/room-icons/9c6bc7e6db746ea68ecaa99e328923f1.png" alt="THM OhSINT" width="220px" height="220px" style="margin-right: 85px;">
<img src="https://assets.tryhackme.com/img/THMlogo.png" alt="THM Logo" width="250px" height="150px" style="margin-bottom: 50px;">

<br>

🔗 [Click here to access the TryHackMe room](https://tryhackme.com/room/ohsint)

<br>

</div>


This room doesn't have a vulnerable machine to work with. Rather it requires the use of OSINT (Open Source Intelligence) to answer the questions related to the file given to be downloaded.

## Examining the given file:

* ### Executing some basic file operations to see if something strikes

	> ls -l

	```
	-rw-rw-r-- 1 b1ack b1ack 234081 Mar 14 15:42 WindowsXP.jpg
	```

	> eog WindowsXP.jpg

	The image is the classic OG WindowsXP background wallpaper. <br>
	Let's see what we can extract from this image.

	Exiftool is a command line utility that shows the exif information embedded within the image.

	> exiftool WindowsXP.jpg

	```
	ExifTool Version Number         : 12.65
	File Name                       : WindowsXP.jpg
	Directory                       : .
	File Size                       : 234 kB
	File Modification Date/Time     : 2024:03:14 15:42:47+05:30
	File Access Date/Time           : 2024:03:14 15:44:00+05:30
	File Inode Change Date/Time     : 2024:03:14 15:43:33+05:30
	File Permissions                : -rw-rw-r--
	File Type                       : JPEG
	File Type Extension             : jpg
	MIME Type                       : image/jpeg
	XMP Toolkit                     : Image::ExifTool 11.27
	GPS Latitude                    : 54 deg 17' 41.27" N
	GPS Longitude                   : 2 deg 15' 1.33" W
	Copyright                       : OWoodflint
	Image Width                     : 1920
	Image Height                    : 1080
	Encoding Process                : Baseline DCT, Huffman coding
	Bits Per Sample                 : 8
	Color Components                : 3
	Y Cb Cr Sub Sampling            : YCbCr4:2:0 (2 2)
	Image Size                      : 1920x1080
	Megapixels                      : 2.1
	GPS Latitude Ref                : North
	GPS Longitude Ref               : West
	GPS Position                    : 54 deg 17' 41.27" N, 2 deg 15' 1.33" W
	```

* ### Examining the exif data

	It appears that the owner of the file might be somewhat related to the copyright owner. Let's browse the web to see if something matches with the given data.

	Found some social media accounts under the name `OWoodflint`.

	[Twitter](https://twitter.com/owoodflint?lang=en) <br>
	[GitHub](https://github.com/OWoodfl1nt/)

	Also, there's a repository `people_finder` in the user's GitHub account that gives some relative intelligence about the owner.

	Also, the `people_finder` repo shows that there's a blog website of this user on [Wordpress](https://oliverwoodflint.wordpress.com/).

	Exploring the blog, gives some more relevant details such as the statement:
	```Im in New York right now, so I will update this site right away with new photos!```
	which might be the answer to one of the THM Questions.

	Looking up in the source code of the Wordpress blog, something peculiar comes up:
	
	```HTML
	<div class="entry-content">
	<p>Im in New York right now, so I will update this site right away with new photos!</p>
	<p style="color:#ffffff;" class="has-text-color">pennYDr0pper.!</p>
	</div><!-- .entry-content -->
	```

	There's a 


<br>

## THM Questions:

* _Q1_: What is this user's avatar of? <br> _A_: `cat`
* _Q2_: What city is this person in? <br> _A_: `London`
* _Q3_: What is his personal email address? <br> _A_: `owoodflint@gmail.com`
* _Q4_: What site did you find his email address on? <br> _A_: `GitHub`
* _05_: Where has he gone on holiday? <br> _A_: `New York`


	
---
---

<div align="center">

💻 Created by [Jayaditya Dev](https://tryhackme.com/p/jayadityadev)

🚀 Find me on [GitHub](https://github.com/jayadityadev)

</div>

---
---