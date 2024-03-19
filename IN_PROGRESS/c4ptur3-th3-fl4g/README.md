
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


## THM Questions (Task 1):

* ### _Q1_: c4n y0u c4p7u23 7h3 f149?

    The answer to this one seems pretty straightforward.

    <b> _A_: `can you capture the flag?` <br> </b> 


* ### _Q2_: 01101100 01100101 01110100 01110011 00100000 01110100 01110010 01111001 00100000 01110011 01101111 01101101 01100101 00100000 01100010 01101001 01101110 01100001 01110010 01111001 00100000 01101111 01110101 01110100 00100001

    This one seems to be some binary code.

    Python script to convert `binary to ascii`:

    ```python
    # binary_ascii.py

    import argparse

    def binary_to_ascii(binary_data):
        ascii_text = ""
        binary_data = binary_data.replace(" ", "").replace("\n", "")
        for i in range(0, len(binary_data), 8):
            byte = binary_data[i:i+8]
            decimal = int(byte, 2)
            ascii_text += chr(decimal)
        return ascii_text

    if __name__ == "__main__":
        parser = argparse.ArgumentParser(description="Convert binary to ASCII text.")
        parser.add_argument("--file", type=str, required=True, help="Path to binary file.")
        args = parser.parse_args()

        with open(args.file, "rb") as f:
            binary_data = f.read().decode()
            binary_data = binary_data.replace(" ", "").replace("\n", "")

        ascii_text = binary_to_ascii(binary_data)
        print(f"ASCII: {ascii_text}")
    ```

    Executing commands:

    > echo "01101100 01100101 01110100 01110011 00100000 01110100 01110010 01111001 00100000 01110011 01101111 01101101 01100101 00100000 01100010 01101001 01101110 01100001 01110010 01111001 00100000 01101111 01110101 01110100 00100001" > task1/flag2

    > python3 binary_ascii.py --file task1/flag2

    ```
    ASCII: lets try some binary out!
    ```

    Can also be decoded online at [RapidTables.com](hhttps://www.rapidtables.com/convert/number/ascii-hex-bin-dec-converter.html).

    <b> _A_: `lets try some binary out!` <br> </b>


* ### _Q3_: MJQXGZJTGIQGS4ZAON2XAZLSEBRW63LNN5XCA2LOEBBVIRRHOM======

    This one seemed to be base64 at once, but base64 decoders weren't giving any readable content. Further research gave hints for base32.

    Python script to check if the string is `base64 or base32`:
    
    ```python
    # check_base.py

    import base64
    import re
    import sys
    import argparse 

    def identify_encoding(encoded_string):
        base64_pattern = re.compile(r'^[A-Za-z0-9+/]*={0,2}$')
        if base64_pattern.match(encoded_string):
            return "Base64"

        base32_pattern = re.compile(r'^[A-Z2-7]*={0,6}$')
        if base32_pattern.match(encoded_string):
            return "Base32"

        return "Unknown"

    if __name__ == "__main__":
        parser = argparse.ArgumentParser(description="Identify encoding")
        parser.add_argument("--file", type=str, required=True, help="Path to the file.")
        args = parser.parse_args()

        with open(args.file, "r") as f:
            encoded_string = f.read().strip()

        encoding = identify_encoding(encoded_string)
        print("Encoding:", encoding)
    ```

    Executing commands:
    
    > echo "MJQXGZJTGIQGS4ZAON2XAZLSEBRW63LNN5XCA2LOEBBVIRRHOM======" > task1/flag3
    
    > python3 check_base.py --file task1/flag3
    
    ```
    Encoding: Base32
    ```
    
    > cat task1/flag3 | base32 --decode
    
    ```
    base32 is super common in CTF's
    ```

    Can also be decoded using an online [base32 decoder](https://emn178.github.io/online-tools/base32_decode.html).
    
    <b> _A_: `base32 is super common in CTF's` <br> </b>

    <br>

    **Note to Self:** Difference between base64 and base32 -

    | Character Set | Base64                       | Base32                       |
    |---------------|------------------------------|------------------------------|
    | Characters    | A-Z, a-z, 0-9, +, /          | A-Z, 2-7                     |
    | Padding       | '=' (one or two)             | '=' (up to six)              |
    | Density       | Denser encoding              | Less dense encoding          |
    | Length        | Multiple of 4 (with padding) | Multiple of 8 (with padding) |


* ### _Q4_: RWFjaCBCYXNlNjQgZGlnaXQgcmVwcmVzZW50cyBleGFjdGx5IDYgYml0cyBvZiBkYXRhLg==

    Using the previous python script to check if it's base64 or base32. Executing commands:

    > echo "RWFjaCBCYXNlNjQgZGlnaXQgcmVwcmVzZW50cyBleGFjdGx5IDYgYml0cyBvZiBkYXRhLg==" > task1/flag4

    > python3 check_base.py --file task1/flag4

    ```
    Encoding: Base64
    ```

    > cat task1/flag4 | base64 --decode

    ```
    Each Base64 digit represents exactly 6 bits of data.
    ```

    Can also be decoded online at [RapidTables.com](https://www.rapidtables.com/convert/number/ascii-hex-bin-dec-converter.html).

    <b> _A_: `Each Base64 digit represents exactly 6 bits of data.` <br> </b>


* ### _Q5_: 68 65 78 61 64 65 63 69 6d 61 6c 20 6f 72 20 62 61 73 65 31 36 3f

    This text appears to be `hexadecimal` (as it consists only `0-9` and `a-f`)

    Executing commands:

    > echo "68 65 78 61 64 65 63 69 6d 61 6c 20 6f 72 20 62 61 73 65 31 36 3f" > task1/flag5

    > cat task1/flag5 | xxd -r -p

    ```
    hexadecimal or base16?
    ```

    Can also be decoded online at [RapidTables.com](https://www.rapidtables.com/convert/number/ascii-hex-bin-dec-converter.html).

    <b> _A_: `hexadecimal or base16?` <br> </b>


* ### _Q6_: Ebgngr zr 13 cynprf!

    With the presence of the number `13`, it gives some hint that the encryption used might be `ROT13` (every letter is rotated 13 places around the english alphabet).

    Executing commands:

    > echo "Ebgngr zr 13 cynprf!" > task1/flag6

    > cat flag6 | tr 'A-Za-z' 'N-ZA-Mn-za-m'

    ```
    Rotate me 13 places!
    ```

    Can also be deciphered at [rot13.com](rot13.com).

    <b> _A_: `Rotate me 13 places!` <br> </b>


* ### _Q7_: *@F DA:? >6 C:89E C@F?5 323J C:89E C@F?5 Wcf E:>6DX

    This one **might** be `ROT47` due to the presence of a mix of characters.

    Trying to decode using an [online decoder](https://www.dcode.fr/rot-47-cipher).

    <b> _A_: `You spin me right round baby right round (47 times)` <br> </b>

    <br>

    **Note to Self:** Identifying ROT47 -

    | Feature    | Indicator                                              |
    |------------|--------------------------------------------------------|
    | Characters | Mix of letters (upper and lower), numbers, and symbols |
    | Obscurity  | More obscure than ROT13 but still easily decoded       |
    | Usage      | Puzzles, playful messages, light text obfuscation      |


* ### _Q8_: - . .-.. . -.-. --- -- -- ..- -. .. -.-. .- - .. --- -.  . -. -.-. --- -.. .. -. --.

    Looking at the `dashes` and `dots`, this one appears to be `Morse Code`.

    Using an online morse code [translater](https://morsedecoder.com/).

    <b> _A_: `TELECOMMUNICATION ENCODING` <br> </b>


* ### _Q9_: 85 110 112 97 99 107 32 116 104 105 115 32 66 67 68

    This one seems pretty much like the decimal representations of `ASCII` characters.

    Executing commands:

    > export flag9=$(cat flag9); echo $flag9 | tr ' ' '\n' | awk '{printf "%c", $1}'

    ```
    Unpack this BCD
    ```

    Can also be decoded online at [RapidTables.com](https://www.rapidtables.com/convert/number/ascii-hex-bin-dec-converter.html).

    <b> _A_: `Unpack this BCD` <br> </b>


* ### _Q10_: LS0tLS0gLi0tLS0gLi0tLS0gLS0tLS0g ...... 0gLS0tLS0gLi0tLS0gLS0tLS0gLi0tLS0=

    Judging from the combination of characters and the `=` at the end, it might be base64 or base32.

    Trying out the check_base.py script:

    > python3 check_base.py --file task1/flag10

    ```
    Encoding: Base64
    ```

    Attempting decode:

    > cat flag10 | base64 --decode

    ```
    ----- .---- .---- ----- ----- .---- .---- -----
    ----- .---- .---- ----- ----- .---- ----- .----
    ----- ----- .---- ----- ----- ----- ----- -----
    < a really long string of dots and dashes >
    ----- ----- .---- ----- ----- ----- ----- -----
    ----- .---- .---- ----- ----- ----- .---- .----
    ----- .---- .---- ----- ----- .---- ----- .----
    ```

    The output seems to be `Morse Code`. Attempting decryption using an online [decoder](https://morsedecoder.com/).

    ```
    0110011001100101001000000110000001011111011000000010
    0000011000000110000001100101001000000110001001101000
    0010000001100000011000000110010000100000011000100110
    < a really long binary output >
    0001001000000110000001011111011010000010000001101000
    0001101000011010000010000001100000010111110110011000
    1001100011001000000110001101100101001000000110001101
    ```

    The output appears to be `binary`. Trying to convert that to `ASCII` at [RapidTables.com](https://www.rapidtables.com/convert/number/ascii-hex-bin-dec-converter.html).

    ```
    fe `_` ``e bh ``d ba `_h hf `_f `_` ba ``e `_c `_d ``d ba hf ba hg `_d ``e ba ``e ``c `_d hh `_f `_d `_` ``c ce ce ce
    ```

    From the looks of the combination of characters and symbols, it resemebles a hint of `ROT47` cipher.
    
    Attempting decipher using an [online decoder](https://www.dcode.fr/rot-47-cipher).

    ```
    76 101 116 39 115 32 109 97 107 101 32 116 104 105 115 32 97 32 98 105 116 32 116 114 105 99 107 105 101 114 46 46 46
    ```

    And this one looks like some `decimal` values :/

    Attempting conversion of `decimal to ASCII` using [RapidTables.com](https://www.rapidtables.com/convert/number/ascii-hex-bin-dec-converter.html).

    ```
    Let's make this a bit trickier...
    ```

    And there's the final decrypted message!!!

    <b> _A_: `Let's make this a bit trickier...` <br> </b>



---
---

<div align="center">

💻 Created by [Jayaditya Dev](https://tryhackme.com/p/jayadityadev)

🚀 Find me on [GitHub](https://github.com/jayadityadev), [LinkedIn](https://www.linkedin.com/in/jayadityadev26/) and [X](https://twitter.com/jayadityadev)

</div>

---
---
