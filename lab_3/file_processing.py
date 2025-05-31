import json
from typing import Union, Dict, Any
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.serialization import load_pem_public_key, load_pem_private_key


class FileOperations:
    """
    A utility class for handling file operations including reading and writing
    bytes, text, and JSON data.
    """
    @staticmethod
    def read_binary_file(file_path: str) -> Union[bytes, None]:
        """
        Read and return the contents of a binary file.
        Args:
            file_path: Path to the file to be read.
        Returns:
            The file contents as bytes if successful, None otherwise.
        """
        try:
            with open(file_path, 'rb') as file:
                return file.read()
        except FileNotFoundError:
            print(f"Error: File not found at path '{file_path}'")
        except IOError as e:
            print(f"Error reading binary file '{file_path}': {str(e)}")
        return None

    @staticmethod
    def write_binary_file(file_path: str, data: bytes) -> bool:
        """
        Write binary data to a file.
        Args:
            file_path: Path where the file will be saved.
            data: Binary data to write.
        Returns:
            True if operation succeeded, False otherwise.
        """
        try:
            with open(file_path, 'wb') as file:
                file.write(data)
            return True
        except IOError as e:
            print(f"Error writing binary file '{file_path}': {str(e)}")
            return False

    @staticmethod
    def read_text_file(file_path: str) -> Union[str, None]:
        """
        Read and return the contents of a text file.
        Args:
            file_path: Path to the file to be read.
        Returns:
            The file contents as string if successful, None otherwise.
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                return file.read()
        except FileNotFoundError:
            print(f"Error: File not found at path '{file_path}'")
        except UnicodeDecodeError:
            print(f"Error: Failed to decode text file '{file_path}' (invalid encoding)")
        except IOError as e:
            print(f"Error reading text file '{file_path}': {str(e)}")
        return None

    @staticmethod
    def write_text_file(file_path: str, content: str) -> bool:
        """
        Write text content to a file.
        Args:
            file_path: Path where the file will be saved.
            content: Text content to write.
        Returns:
            True if operation succeeded, False otherwise.
        """
        try:
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(content)
            return True
        except IOError as e:
            print(f"Error writing text file '{file_path}': {str(e)}")
            return False

    @staticmethod
    def read_json_file(file_path: str) -> Union[Dict[str, Any], None]:
        """
        Read and parse a JSON file.
        Args:
            file_path: Path to the JSON file to be read.
        Returns:
            Parsed JSON data as dictionary if successful, None otherwise.
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                return json.load(file)
        except FileNotFoundError:
            print(f"Error: JSON file not found at path '{file_path}'")
        except json.JSONDecodeError as e:
            print(f"Error: Invalid JSON format in file '{file_path}': {str(e)}")
        except IOError as e:
            print(f"Error reading JSON file '{file_path}': {str(e)}")
        return None

    @staticmethod
    def write_json_file(file_path: str, data: Dict[str, Any]) -> bool:
        """
        Write data to a file in JSON format.
        Args:
            file_path: Path where the JSON file will be saved.
            data: Dictionary to be serialized as JSON.
        Returns:
            True if operation succeeded, False otherwise.
        """
        try:
            with open(file_path, 'w', encoding='utf-8') as file:
                json.dump(data, file, ensure_ascii=False, indent=1)
            return True
        except TypeError as e:
            print(f"Error: Non-serializable data in JSON: {str(e)}")
        except IOError as e:
            print(f"Error writing JSON file '{file_path}': {str(e)}")
            return False

    @staticmethod
    def load_config(path: str) -> dict:
        """
        Загрузка json
        :param path: путь к json
        :return: загрузка
        """
        try:
            with open(path, 'r') as f:
                return json.load(f)
        except Exception as e:
            print("Error..", str(e))

    @staticmethod
    def read_public_key(key_path: str):
        """
        Load and return an RSA public key from a PEM file.
        Args:
            key_path: Path to the public key file.
        Returns:
            The loaded public key or None if loading fails.
        Raises:
            FileNotFoundError: If the key file doesn't exist.
            ValueError: If the key data is invalid.
        """
        print(f"Loading public key from {key_path}...")
        try:
            with open(key_path, 'rb') as key_file:
                public_key = load_pem_public_key(key_file.read())
            print("[SUCCESS] Public key loaded successfully")
            return public_key
        except FileNotFoundError:
            print(f"[ERROR] Public key file not found at {key_path}")
            raise
        except Exception as e:
            print(f"[ERROR] Failed to load public key: {str(e)}")
            raise ValueError(f"Invalid public key: {str(e)}")

    @staticmethod
    def save_public_key(public_key, output_path: str) -> None:
        """
        Save an RSA public key to a file in PEM format.
        Args:
            public_key: The public key to save.
            output_path: Destination file path.
        Raises:
            IOError: If the file cannot be written.
        """
        print(f"Saving public key to {output_path}...")
        try:
            pem_data = public_key.public_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PublicFormat.SubjectPublicKeyInfo
            )
            with open(output_path, 'wb') as key_file:
                key_file.write(pem_data)
            print(f"[SUCCESS] Public key saved to {output_path}")
        except IOError as e:
            print(f"[ERROR] Failed to save public key: {str(e)}")
            raise
        except Exception as e:
            print(f"[ERROR] Unexpected error saving public key: {str(e)}")
            raise

    @staticmethod
    def read_private_key(key_path: str, password: bytes = None):
        """
        Load and return an RSA private key from a PEM file.
        Args:
            key_path: Path to the private key file.
            password: Optional password for encrypted private keys.
        Returns:
            The loaded private key or None if loading fails.
        Raises:
            FileNotFoundError: If the key file doesn't exist.
            ValueError: If the key data is invalid or password is incorrect.
        """
        print(f"Loading private key from {key_path}...")
        try:
            with open(key_path, 'rb') as key_file:
                private_key = load_pem_private_key(
                    key_file.read(),
                    password=password
                )
            print("[SUCCESS] Private key loaded successfully")
            return private_key
        except FileNotFoundError:
            print(f"[ERROR] Private key file not found at {key_path}")
            raise
        except TypeError as e:
            print(f"[ERROR] Incorrect password or corrupted key: {str(e)}")
            raise ValueError("Incorrect password or corrupted key") from e
        except Exception as e:
            print(f"[ERROR] Failed to load private key: {str(e)}")
            raise ValueError(f"Invalid private key: {str(e)}") from e

    @staticmethod
    def save_private_key(private_key, output_path: str) -> None:
        """
        Save an RSA private key to a file in PEM format.
        Args:
            private_key: The private key to save.
            output_path: Destination file path.
        Raises:
            IOError: If the file cannot be written.
        """
        print(f"Saving private key to {output_path}...")
        try:
            pem_data = private_key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.TraditionalOpenSSL,
                encryption_algorithm=serialization.NoEncryption()
            )
            with open(output_path, 'wb') as key_file:
                key_file.write(pem_data)
            print(f"[SUCCESS] Private key saved to {output_path}")
        except IOError as e:
            print(f"[ERROR] Failed to save private key: {str(e)}")
            raise
        except Exception as e:
            print(f"[ERROR] Unexpected error saving private key: {str(e)}")
            raise