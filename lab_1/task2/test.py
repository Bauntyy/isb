from constants import *
from utility_functions import calculate_frequency, read_json, read_file, sort_dict, write_to_file


def main():
    """
    Main function of the program. Reads the encrypted text from a file,
    calculates the frequency index of symbols, decrypts the text,
    displays results, and saves them to files.

    Raises:
    - FileNotFoundError: If the encrypted text file cannot be found.
    - UnicodeDecodeError: If there's an issue with the file's encoding.
    - Exception: Handles all other unforeseen exceptions.
    """
    try:
        # Read the encrypted text from the file
        text = read_file(PATH_ENCRYPTED)
        print("\n", "*" * 40, "Encrypted Text", "*" * 40, "\n")
        print(text)

        # Calculate the frequency index of symbols
        frequency_dict = calculate_frequency(text)
        print("\n", "*" * 40, "Frequency Index", "*" * 40, "\n")
        sort_dict(frequency_dict)

        # Decrypt the text
        decrypt_key = read_json(PATH_KEY)
        print("\n", "*" * 40, "Decrypted Text", "*" * 40, "\n")
        new_text = text
        for original_char, replacement_char in decrypt_key.items():
            new_text = new_text.replace(original_char, replacement_char)
        print(new_text)

        # Display the decryption key
        crypt_key = read_json(PATH_KEY)
        print("\n", "*" * 40, "Decryption Key", "*" * 40, "\n")
        print(crypt_key)

        # Write the results to files
        write_to_file(PATH_DECRYPTED, new_text)
        print("\nResults have been successfully written to files.")

    except FileNotFoundError:
        print("Error: The encrypted text file was not found.")
    except UnicodeDecodeError:
        print("Error: There was a problem with the file's encoding.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()