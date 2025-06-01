import argparse

from generate_keys import GenerateKeys
from file_processing import FileOperations
from asymmetrical import AsymmetricCrypto
from symmetrical import SymmetricCrypto


def main():
    """
        Main function for cryptographic operations management.

        Supports three modes:
        - Generation: Creates and saves cryptographic keys
        - Encryption: Encrypts files using hybrid cryptography
        - Decryption: Decrypts files using hybrid cryptography

        Usage:
            python script.py [-gen | -enc | -dec] -c CONFIG_FILE
        """
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required = True)
    group.add_argument('-gen','--generation',action='store_true',help='Запускает режим генерации ключей')
    group.add_argument('-enc','--encryption',action='store_true',help='Запускает режим шифрования')
    group.add_argument('-dec','--decryption',action='store_true',help='Запускает режим дешифрования')
    parser.add_argument('-c', '--config', required=True, help='Путь к файлу конфигурации')

    args = parser.parse_args()
    if args.generation:
        mode = 'generation'
        print("\n[STATUS] Starting key generation process...")
    elif args.encryption:
        mode = 'encryption'
        print("\n[STATUS] Starting file encryption process...")
    else:
        mode = 'decryption'
        print("\n[STATUS] Starting file decryption process...")

    try:
        # Load configuration
        print("[INFO] Loading configuration file...")
        cfg = FileOperations.load_config(args.config)

        match mode:
            case 'generation':
                # Key generation workflow
                print("[INFO] Generating cryptographic keys...")
                public_key, private_key, encrypt_sym_key = GenerateKeys.generate_and_encrypt_keys(cfg)

                print("[INFO] Saving keys to files...")
                FileOperations.save_public_key(public_key, cfg['public_key_path'])
                FileOperations.save_private_key(private_key, cfg['private_key_path'])
                FileOperations.save_encrypted_sym_key(encrypt_sym_key, cfg['symmetric_key_path'])

                print("[SUCCESS] All keys generated and saved successfully")

            case 'encryption':
                # Encryption workflow
                print("[INFO] Loading required keys...")
                private_key = FileOperations.read_private_key(cfg['private_key_path'])
                encrypted_sym_key = FileOperations.read_binary_file(cfg['symmetric_key_path'])

                print("[INFO] Decrypting symmetric key...")
                symmetric_key = AsymmetricCrypto.decrypt_with_private_key(private_key, encrypted_sym_key)

                print(f"[INFO] Reading input file: {cfg['input_file_path']}")
                text = FileOperations.read_binary_file(cfg['input_file_path'])

                print("[INFO] Encrypting file content...")
                encrypted_text, nonce = SymmetricCrypto.sym_encrypt_chacha20(text, symmetric_key)

                print("[INFO] Saving encrypted data...")
                FileOperations.write_binary_file(cfg['encrypted_file_path'], encrypted_text)
                FileOperations.write_binary_file(cfg['nonce'], nonce)

                print(f"[SUCCESS] File encrypted successfully. Output: {cfg['encrypted_file_path']}")

            case 'decryption':
                # Decryption workflow
                print("[INFO] Loading required keys...")
                private_key = FileOperations.read_private_key(cfg['private_key_path'])
                encrypted_sym_key_data = FileOperations.read_binary_file(cfg['symmetric_key_path'])

                print("[INFO] Decrypting symmetric key...")
                symmetric_key = AsymmetricCrypto.decrypt_with_private_key(private_key, encrypted_sym_key_data)

                print(f"[INFO] Reading encrypted file: {cfg['encrypted_file_path']}")
                encrypted_text = FileOperations.read_binary_file(cfg['encrypted_file_path'])
                nonce = FileOperations.read_binary_file(cfg['nonce'])

                print("[INFO] Decrypting file content...")
                decrypted_text = SymmetricCrypto.sym_decrypt_chacha20(encrypted_text, symmetric_key, nonce)

                print("[INFO] Saving decrypted data...")
                FileOperations.write_binary_file(cfg['decrypted_file_path'], decrypted_text)

                print(f"[SUCCESS] File decrypted successfully. Output: {cfg['decrypted_file_path']}")

    except FileNotFoundError as e:
        print(f"[ERROR] File not found: {str(e)}")
        exit(1)
    except ValueError as e:
        print(f"[ERROR] Cryptographic operation failed: {str(e)}")
        exit(1)
    except Exception as e:
        print(f"[ERROR] Unexpected error: {str(e)}")
        exit(1)

if __name__ == "__main__":
    main()