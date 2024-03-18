import base64
import re
import sys

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
    if len(sys.argv) != 2:
        print("Usage: python3 check_base.py <encoded_string>")
        sys.exit(1)

    encoded_string = sys.argv[1]
    encoding = identify_encoding(encoded_string)
    print("Encoding:", encoding)
