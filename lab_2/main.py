from functions import read_json, read_sequence, run_tests
from isb.lab_2.functions import write_results


def main():
    constants, PI_i = read_json("constants.json")
    cpp_sequence_path = constants.get("cpp_sequence")
    java_sequence_path = constants.get("java_sequence")
    result_path = constants.get("result_path")
    print(java_sequence_path, cpp_sequence_path)

    cpp_sequence = read_sequence(cpp_sequence_path)
    java_sequence = read_sequence(java_sequence_path)

    cpp_results = run_tests(cpp_sequence, PI_i)
    java_results = run_tests(java_sequence, PI_i)
    print(cpp_results, "\n", java_results)

    write_results(result_path, cpp_results, java_results)

if __name__ == "__main__":
    main()