# check_base.py

import base64
import re
import sys
import argparse 

def identify_encoding(encoded_string):
    # Check if the string contains only valid Base64 characters
    base64_pattern = re.compile(r'^[A-Za-z0-9+/]*={0,2}$')
    if base64_pattern.match(encoded_string):
        return "Base64"

    # Check if the string contains only valid Base32 characters
    base32_pattern = re.compile(r'^[A-Z2-7]*={0,6}$')
    if base32_pattern.match(encoded_string):
        return "Base32"

    return "Unknown"

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Identify encoding of a string in a file.")
    parser.add_argument("--file", type=str, required=True, help="Path to the file containing the encoded string.")
    args = parser.parse_args()

    with open(args.file, "r") as f:
        encoded_string = f.read().strip()  # Read the string and remove any leading/trailing whitespace

    encoding = identify_encoding(encoded_string)
    print("Encoding:", encoding)
