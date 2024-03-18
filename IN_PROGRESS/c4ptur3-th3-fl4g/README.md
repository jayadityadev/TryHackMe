
---
---

<div align="center">

# TryHackMe c4ptur3-th3-fl4g


<img src="https://tryhackme-images.s3.amazonaws.com/room-icons/8b906b3d444362152f1cd3e521aa7e4a.png" alt="THM c4ptur3-th3-fl4g" width="300px" height="220px" style="margin-right: 55px;">
<img src="https://assets.tryhackme.com/img/THMlogo.png" alt="THM Logo" width="250px" height="150px" style="margin-bottom: 50px;">

<br>

🔗 [Click here to access the TryHackMe room](https://tryhackme.com/room/c4ptur3th3fl4g)

<br>

</div>


## THM Questions:

### _Q1_: c4n y0u c4p7u23 7h3 f149?

The answer to this one seems pretty straightforward.

<b> _A_: `can you capture the flag?` <br> </b> <br>


### _Q2_: 01101100 01100101 01110100 01110011 00100000 01110100 01110010 01111001 00100000 01110011 01101111 01101101 01100101 00100000 01100010 01101001 01101110 01100001 01110010 01111001 00100000 01101111 01110101 01110100 00100001

This one seems to be some binary code. Trying that on [RapidTables](https://www.rapidtables.com/convert/number/binary-to-ascii.html).

Python script to convert `binary to ascii`:

```python
import sys

def binary_to_ascii(binary_string):
    binary_string = binary_string.replace(" ", "")

    ascii_text = ''.join(chr(int(binary_string[i:i+8], 2)) for i in range(0, len(binary_string), 8))

    return ascii_text

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 binary.py '<binary_string>'")
        sys.exit(1)

    binary_string = sys.argv[1]
    ascii_text = binary_to_ascii(binary_string)
    print("ASCII:", ascii_text)
```

Solving via command line:

> python3 binary_ascii.py "01101100 01100101 01110100 01110011 00100000 01110100 01110010 01111001 00100000 01110011 01101111 01101101 01100101 00100000 01100010 01101001 01101110 01100001 01110010 01111001 00100000 01101111 01110101 01110100 00100001"

```
ASCII: lets try some binary out!
```

<b> _A_: `lets try some binary out!` <br> </b> <br>


### _Q3_: MJQXGZJTGIQGS4ZAON2XAZLSEBRW63LNN5XCA2LOEBBVIRRHOM======

This one seemed to be base64 at once, but base64 decoders weren't giving any readable content. Further research gave hints for base32. Trying out on an online [base32 decoder](https://emn178.github.io/online-tools/base32_decode.html).

Python script to check if the string is `base64 or base32`:

```python
import base64
import re
import sys

def identify_encoding(encoded_string):
    base64_pattern = re.compile(r'^[A-Za-z0-9+/]*={0,2}$')
    if base64_pattern.match(encoded_string):
        return "Base64"

    base32_pattern = re.compile(r'^[A-Z2-7]*={0,6}$')
    if base32_pattern.match(encoded_string):
        return "Base32"

    return "Unknown"

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 check_base.py <encoded_string>")
        sys.exit(1)

    encoded_string = sys.argv[1]
    encoding = identify_encoding(encoded_string)
    print("Encoding:", encoding)
```

Solving via command line:

> python3 check_base.py MJQXGZJTGIQGS4ZAON2XAZLSEBRW63LNN5XCA2LOEBBVIRRHOM======

```
Encoding: Base32
```

> echo MJQXGZJTGIQGS4ZAON2XAZLSEBRW63LNN5XCA2LOEBBVIRRHOM====== | base32 --decode

```
base32 is super common in CTF's
```

<b> _A_: `base32 is super common in CTF's` <br> </b>

<br>

**NOTE to self:**
Difference between base64 and base32 -
| Character Set | Base64                       | Base32                       |
|---------------|------------------------------|------------------------------|
| Characters    | A-Z, a-z, 0-9, +, /          | A-Z, 2-7                     |
| Padding       | '=' (one or two)             | '=' (up to six)              |
| Density       | Denser encoding              | Less dense encoding          |
| Length        | Multiple of 4 (with padding) | Multiple of 8 (with padding) |

<br>


### _Q4_: RWFjaCBCYXNlNjQgZGlnaXQgcmVwcmVzZW50cyBleGFjdGx5IDYgYml0cyBvZiBkYXRhLg==

Using the previous python script to check if it's base64 or base32:

> python3 check_base.py RWFjaCBCYXNlNjQgZGlnaXQgcmVwcmVzZW50cyBleGFjdGx5IDYgYml0cyBvZiBkYXRhLg==

```
Encoding: Base64
```

Solving via command line:

> echo "RWFjaCBCYXNlNjQgZGlnaXQgcmVwcmVzZW50cyBleGFjdGx5IDYgYml0cyBvZiBkYXRhLg==" | base64 --decode

```
Each Base64 digit represents exactly 6 bits of data.
```

<b> _A_: `Each Base64 digit represents exactly 6 bits of data.` <br> </b>


### _Q5_: 68 65 78 61 64 65 63 69 6d 61 6c 20 6f 72 20 62 61 73 65 31 36 3f

This text appears to be `hexadecimal` (as it consists only `0-9` and `a-f`)



---
---

<div align="center">

💻 Created by [Jayaditya Dev](https://tryhackme.com/p/jayadityadev)

🚀 Find me on [GitHub](https://github.com/jayadityadev), [LinkedIn](https://www.linkedin.com/in/jayadityadev26/) and [X](https://twitter.com/jayadityadev)

</div>

---
---
