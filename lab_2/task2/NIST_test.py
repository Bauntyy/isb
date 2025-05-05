import math as m
from scipy.special import gammainc


def frequency_test(binary_sequence: str):
    if len(binary_sequence) == 0:
        raise ValueError("Последовательность не может быть пустой")
    result = 0

    for bit in binary_sequence:
        if bit == "1":
            result += 1
        else:
            result -= 1

    S_N = abs(result)/m.sqrt(len(binary_sequence))
    p_value = m.erfc(S_N/m.sqrt(2))
    return p_value


def same_bits_test(binary_sequence):

    if len(binary_sequence) == 0:
        raise ValueError("Последовательность не может быть пустой")

    ones_count = 0
    for bit in binary_sequence:
        if bit == "1":
            ones_count += 1
    unit_of_ones = ones_count/len(binary_sequence)

    if abs(unit_of_ones - 0.5) >= 2/m.sqrt(len(binary_sequence)):
        p_value = 0
        return p_value

    number_of_sign_alternations = 0
    for i in range(len(binary_sequence) - 1):
        if binary_sequence[i] != binary_sequence[i + 1]:
            number_of_sign_alternations += 1

    p_value = (abs(number_of_sign_alternations - 2 * len(binary_sequence) * unit_of_ones * (1 - unit_of_ones))) / (2 * m.sqrt(2*len(binary_sequence) * unit_of_ones * (1 - unit_of_ones)))

    return p_value


def longest_sequence_test(binary_sequence, PI_i,  block_size = 8):
    if len(binary_sequence) == 0:
        raise ValueError("Последовательность не может быть пустой")

    if block_size > len(binary_sequence):
        raise ValueError("Бинарная последовательность должна быть больше длины блока")

    if len(binary_sequence) % block_size != 0:
        raise ValueError("Длина блока должна быть кратна длине последовательности")


    V_i = [0] * 4
    for i in range(0, len(binary_sequence), block_size):
        block = binary_sequence[i:i + block_size]
        max_len = 0
        cur_len = 0

        for bit in block:
            if bit not in {"0", "1"}:
                raise ValueError(f"Блок содержит посторонние символы: '{i}'")

            match bit:
                case "1":
                    cur_len += 1
                case "0":
                    cur_len = 0
            max_len = max(cur_len, max_len)

        match max_len:
            case _ if max_len <= 1:
                V_i[0] += 1
            case 2:
                V_i[1] += 1
            case 3:
                V_i[2] += 1
            case _:
                V_i[3] += 1

    hi_square = 0.0
    for i in range(len(V_i)):
        hi_square += ((V_i[i] - 16 * PI_i[i]) ** 2) / (16 * PI_i[i])

    p_value = gammainc(3/2, hi_square/2)
    return p_value