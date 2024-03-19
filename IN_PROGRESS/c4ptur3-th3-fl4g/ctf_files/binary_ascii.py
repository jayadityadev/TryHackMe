# binary_ascii.py

import argparse

def binary_to_ascii(binary_data):
    ascii_text = ""
    # Remove any spaces or newline characters from the binary data
    binary_data = binary_data.replace(" ", "").replace("\n", "")
    for i in range(0, len(binary_data), 8):
        byte = binary_data[i:i+8]
        decimal = int(byte, 2)
        ascii_text += chr(decimal)
    return ascii_text

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert binary data to ASCII text.")
    parser.add_argument("--file", type=str, required=True, help="Path to the binary file.")
    args = parser.parse_args()

    with open(args.file, "rb") as f:
        binary_data = f.read().decode()  # Read as binary, decode to a string
        binary_data = binary_data.replace(" ", "").replace("\n", "")  # Remove spaces and newlines

    ascii_text = binary_to_ascii(binary_data)
    print(f"ASCII: {ascii_text}")
