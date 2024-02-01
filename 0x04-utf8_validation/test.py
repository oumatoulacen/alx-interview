def fix_utf8_encoding(byte_list):
    fixed_bytes = []

    for num in byte_list:
        # Check if the number is within the valid range for a single byte
        if 0 <= num <= 127:
            fixed_bytes.append(num)
        else:
            # Convert the number to binary representation
            binary_representation = bin(num)[2:]
            print(fixed_bytes)
            # Determine the number of bytes needed for the UTF-8 encoding
            if 128 <= num <= 2047:
                # Two-byte character
                binary_representation = '0' * (11 - len(binary_representation)) + binary_representation
                fixed_bytes.append(int('110' + binary_representation[:5], 2))
                fixed_bytes.append(int('10' + binary_representation[5:], 2))
                print(fixed_bytes, ' 128 <= num <= 2047')

            elif 2048 <= num <= 65535:
                # Three-byte character
                binary_representation = '0' * (16 - len(binary_representation)) + binary_representation
                fixed_bytes.append(int('1110' + binary_representation[:4], 2))
                fixed_bytes.append(int('10' + binary_representation[4:10], 2))
                fixed_bytes.append(int('10' + binary_representation[10:], 2))
                print(fixed_bytes, ' 2048 <= num <= 65535')

            elif 65536 <= num <= 1114111:
                # Four-byte character
                binary_representation = '0' * (21 - len(binary_representation)) + binary_representation
                fixed_bytes.append(int('11110' + binary_representation[:3], 2))
                fixed_bytes.append(int('10' + binary_representation[3:9], 2))
                fixed_bytes.append(int('10' + binary_representation[9:15], 2))
                fixed_bytes.append(int('10' + binary_representation[15:], 2))
                print(fixed_bytes, ' 65536 <= num <= 1114111')

            else:
                # Out of range, handle as needed (e.g., replace with a placeholder)
                fixed_bytes.append(239)  # Placeholder for invalid character

    return fixed_bytes

# Example usage:
data = [229, 65, 127, 256]
fixed_data = fix_utf8_encoding(data)
print(fixed_data)
