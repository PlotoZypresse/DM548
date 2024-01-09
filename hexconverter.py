def convert_hex_number(hex_number, output_format='binary'):
    """
    Convert a hexadecimal number to either binary or decimal format, with leading zeros.

    :param hex_number: A string representing the hex number (e.g., '568da3').
    :param output_format: 'binary' or 'decimal' to specify the output format.
    :return: A string representing the converted number in the specified format.
    """
    try:
        # Convert to integer first (base 10)
        decimal_number = int(hex_number, 16)
    except ValueError:
        return "Invalid hexadecimal number."

    if output_format == 'binary':
        # Convert to binary and format with leading zeros to ensure proper length
        binary_number = bin(decimal_number)[2:]  # Remove the '0b' prefix
        # Pad with leading zeros to make sure it's a multiple of 4 bits
        binary_number = binary_number.zfill(len(hex_number)*4)
        return binary_number
    elif output_format == 'decimal':
        # It's already in decimal, just convert to string
        return str(decimal_number)
    else:
        return "Invalid output format."

# Interactive part to ask for user input
hex_input = input("Enter a hexadecimal number: ")
output_format = input("Enter the desired output format ('binary' or 'decimal'): ")

# Get the conversion
converted_output = convert_hex_number(hex_input, output_format)

# Print the result
print(f"Converted number: {converted_output}")
