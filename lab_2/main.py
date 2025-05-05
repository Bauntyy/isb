from functions import read_json, read_sequence, run_tests


def main():
    # constants_path = "constants.json"
    constants, PI_i = read_json("constants.json")
    cpp_sequence_path = constants.get("cpp_sequence")
    java_sequence_path = constants.get("java_sequence")
    print(java_sequence_path, cpp_sequence_path)

    cpp_sequence = read_sequence(cpp_sequence_path)
    java_sequence = read_sequence(java_sequence_path)

    cpp_results = run_tests(cpp_sequence, PI_i)
    java_results = run_tests(java_sequence, PI_i)
    print(cpp_results, "\n", java_results)

if __name__ == "__main__":
    main()