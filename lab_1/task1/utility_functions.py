def read_file(filename):
    """
    Reads the contents of a file.

    Parameters:
    filename (str): The path to the file that needs to be read.

    Returns:
    str: The contents of the file.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read()


def write_file(filename, content):
    """
    Writes content to a specified file.

    Parameters:
    filename (str): The path to the file where the content will be written.
    content (str): The data to be written to the file.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(content)


def polybius_encode(text, key):
    """
    Encodes a given text using the Polybius Square cipher based on the provided key.

    Parameters:
    text (str): The message to encode.
    key (str): The custom alphabet used to create the Polybius Square.

    Raises:
    ValueError: If the key does not contain at least 33 unique characters.

    Returns:
    str: The encoded text represented by coordinate pairs from the Polybius Square.
    """
    # Create the Polybius square based on the key
    key = key.lower().replace(' ', '')  # Remove spaces and convert to lowercase
    unique_chars = set(key)

    if len(unique_chars) <= 33:
        raise ValueError("Key must contain at least 33 unique characters")

    matrix = [['' for _ in range(6)] for _ in range(6)]
    index = 0

    for i in range(6):
        for j in range(6):
            if index < len(unique_chars):
                matrix[i][j] = key[index]
                index += 1

    # Encode the text into coordinates of the matrix or special codes
    encoded_text = []
    text = text.lower()

    for char in text:
        if char.isalpha():  # Handle alphabetic characters
            for i in range(6):
                for j in range(6):
                    if matrix[i][j] == char:
                        encoded_text.append(str(i + 1))
                        encoded_text.append(str(j + 1))
                        break
        else:
            continue  # Ignore other non-alphanumeric characters

    for i in range(6):
        for j in range(6):
            print(matrix[i][j], end=" ")
        print("\n")

    return ''.join(encoded_text)