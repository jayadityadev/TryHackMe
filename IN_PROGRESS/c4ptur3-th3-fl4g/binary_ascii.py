import sys

def binary_to_ascii(binary_string):
    # Remove spaces from the binary string
    binary_string = binary_string.replace(" ", "")

    # Convert binary string to ASCII
    ascii_text = ''.join(chr(int(binary_string[i:i+8], 2)) for i in range(0, len(binary_string), 8))

    return ascii_text

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 binary.py '<binary_string>'")
        sys.exit(1)

    binary_string = sys.argv[1]
    ascii_text = binary_to_ascii(binary_string)
    print("ASCII:", ascii_text)
