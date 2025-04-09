import json


def write_to_file(filename, content):
    """
    Writes content to a file.

    Parameters:
    filename (str): The name of the file to write to.
    content (str): The content to be written to the file.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(content)


def read_file(filename):
    """
    Reads data from a file.

    Parameters:
    filename (str): The name of the file to read from.

    Returns:
    str: The contents of the file.
    """
    with open(filename, "r", encoding="utf-8") as file:
        return file.read()


def read_json(filename: str) -> dict:
    """
    Loads data from a JSON file.

    Parameters:
    filename (str): The name of the JSON file to load.

    Returns:
    dict: The loaded data as a dictionary.
    """
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading {filename}: {e}")
        return {}


def sort_dict(unsorted_dict):
    sorted_dict = {}
    for key in sorted(unsorted_dict, key=unsorted_dict.get, reverse=True):
        sorted_dict[key] = unsorted_dict[key]
    print(sorted_dict)
    return sorted_dict


def calculate_frequency(text):
    """
    Calculates character frequencies in a given text.

    Parameters:
    text (str): The input text to analyze.

    Returns:
    dict: A dictionary where keys are characters and values are their frequency percentages.
    """
    char_count = {}  # Dictionary to store character counts
    text_len = len(text)

    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    char_frequency = {}
    for char, count in char_count.items():
        char_frequency[char] = (count / text_len)

    return char_frequency
