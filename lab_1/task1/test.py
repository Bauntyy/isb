from utility_functions import polybius_encode, read_file, write_file


def main():
    """
    Main function of the program. It reads an input text and a key, encrypts the text using the Polybius Square method,
    and writes the result to an output file.

    Input files are expected to be in UTF-8 format.

    Parameters:
    None

    Exceptions:
    - FileNotFoundError: Raised when either the input file or the key file is not found.
    - ValueError: Raised when there is an issue with the encryption key.
    - Exception: Catches any unexpected errors during execution.
    """
    try:
        # Reading the input text and key
        input_filename = 'input.txt'
        key_filename = 'key.txt'
        output_filename = 'encrypted.txt'

        text = read_file(input_filename)
        key = read_file(key_filename).strip()

        # Encrypting the text
        encrypted_text = polybius_encode(text, key)

        # Writing the result to the output file
        write_file(output_filename, encrypted_text)
        print(f"The text has been successfully encrypted and saved to {output_filename}")

    except FileNotFoundError as e:
        print(f"Error: File not found - {e.filename}")
    except ValueError as e:
        print(f"Error in the key: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == '__main__':
    main()