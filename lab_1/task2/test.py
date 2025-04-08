from constants import *
from utility_functions import calculate_frequency, read_json, read_file, write_to_file


def main():
    """
    Основная функция программы. Читает зашифрованный текст из файла,
    вычисляет индекс частот встречаемости символов, дешифрует текст,
    выводит результаты и сохраняет их в файлах.

    Исключение FileNotFoundError возникает, если файл зашифрованного текста не найден.
    Исключение UnicodeDecodeError возникает, если возникает проблема с кодировкой файла.
    Другие исключения обрабатываются общим блоком except.
    """
    try:
        # Чтение зашифрованного текста из файла
        text = read_file(PATH_ENCRYPTED)
        print("\n", "*" * 40, "Зашифрованный текст", "*" * 40, "\n")
        print(text)

        # Вычисление индекса частот символов
        percent_dict = calculate_frequency(text)
        print("\n", "*" * 40, "Индекс частот", "*" * 40, "\n")
        sorted_dict = {}
        for key in sorted(percent_dict, key=percent_dict.get, reverse=True):
            sorted_dict[key] = percent_dict[key]
        print(sorted_dict)

        # Дешифровка текста
        print("\n", "*" * 40, "Дешифрованный текст", "*" * 40, "\n")
        new_text = text
        for original_char, replacement_char in DECRYPT_KEY.items():
            new_text = new_text.replace(original_char, replacement_char)
        print(new_text)

        # Вывод ключа дешифрования
        crypt_key = read_json(PATH_KEY)
        print("\n", "*" * 40, "Ключ шифрования", "*" * 40, "\n")
        print(crypt_key)

        # Запись результатов в файлы
        write_to_file(PATH_DECRYPTED, new_text)
        print("\nРезультаты успешно записаны в файлы")

    except FileNotFoundError:
        print("Ошибка: файл зашифрованного текста не найден")
    except UnicodeDecodeError:
        print("Ошибка: проблема с кодировкой файла")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


if __name__ == "__main__":
    main()