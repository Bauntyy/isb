import json
from NIST_test import frequency_test, same_bits_test, longest_sequence_test

def read_json(path):
    try:
        with open(path, "r") as file:
            data = json.load(file)
            PI_constants = data.get("PI_I", [])
            return data, PI_constants
    except FileNotFoundError:
            print(f"File {path} not found!")
            return {}, []


def read_sequence(path: str):
    try:
        with open(path, "r") as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        raise Exception(f"File {path} not found.")\


def run_tests(sequence, PI_i):
    results = []
    freq_test_result = frequency_test(sequence)
    results.append(f"Result of frequency bit test: {freq_test_result}")
    run_same_result = same_bits_test(sequence)
    results.append(f"Result of run same bit test: {run_same_result}")
    longest_one_result = longest_sequence_test(sequence, PI_i)
    results.append(f"Result of longest one sequence test: {longest_one_result}")
    return results