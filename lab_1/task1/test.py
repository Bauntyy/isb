from utility_functions import polybius_encode, read_file, write_file
from constants import *


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
        text = read_file(INPUT_FILENAME)
        key = read_file(KEY_FILENAME).strip()

        # Encrypting the text
        encrypted_text = polybius_encode(text, key)

        # Writing the result to the output file
        write_file(OUTPUT_FILENAME, encrypted_text)
        print(f"The text has been successfully encrypted and saved to {OUTPUT_FILENAME}")

    except FileNotFoundError as e:
        print(f"Error: File not found - {e.filename}")
    except ValueError as e:
        print(f"Error in the key: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == '__main__':
    main()
