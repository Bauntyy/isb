import json
import os
from task2.NIST_test import frequency_test, same_bits_test, longest_sequence_test


def read_json(filename: str) -> tuple[dict, list]:
    """Читает JSON-файл из той же папки, где и скрипт."""
    try:
        # Формируем полный путь
        file_path = os.path.join(os.path.dirname(__file__), filename)

        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            PI_constants = data.get("PI_I", [])
            return data, PI_constants

    except FileNotFoundError:
        print(f"Файл {filename} не найден в папке скрипта!")
        return {}, []
    except json.JSONDecodeError:
        print("Ошибка: файл не в формате JSON!")
        return {}, []


def read_sequence(file_path):
    try:
        with open(file_path, "r") as file:
            return file.read().replace(" ", "")
    except FileNotFoundError:
        raise Exception(f"Файл {file_path} не найден")


def run_tests(sequence, PI_i):
    results = []
    freq_test_result = frequency_test(sequence)
    results.append(f"Result of frequency bit test: {freq_test_result}")
    run_same_result = same_bits_test(sequence)
    results.append(f"Result of run same bit test: {run_same_result}")
    longest_ones_result = longest_sequence_test(sequence, PI_i)
    results.append(f"Result of longest ones sequence test: {longest_ones_result}")
    return results

def write_results(path, cpp_result, java_result):
    try:
        with open(path, "w") as file:
            file.write("C++ results:\n")
            for results in cpp_result:
                file.write(results + "\n")

            file.write("JAVA results:\n")
            for results in java_result:
                file.write(results + "\n")
    except IOError as e:
        raise Exception(f"Error while writing to file: {e}")