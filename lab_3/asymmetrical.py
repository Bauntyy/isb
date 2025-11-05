from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from typing import Any


class AsymmetricCrypto:
    """A class for asymmetric encryption and decryption using RSA with OAEP padding."""

    @staticmethod
    def encrypt_with_public_key(public_key: Any, data: bytes) -> bytes:
        """
        Encrypts data using RSA public key with OAEP padding.
        Args:
            public_key: RSA public key for encryption
            data: Data to be encrypted (typically a symmetric key)
        Returns:
            Encrypted data as bytes
        Raises:
            ValueError: If data is too large for RSA encryption
            RuntimeError: If encryption fails for other reasons
        """
        print("[INFO] Encrypting data with public key...")
        try:
            encrypted_data = public_key.encrypt(
                data,
                padding.OAEP(
                    mgf=padding.MGF1(algorithm=hashes.SHA256()),
                    algorithm=hashes.SHA256(),
                    label=None
                )
            )
            print("[SUCCESS] Data encrypted successfully")
            return encrypted_data
        except ValueError as e:
            print(f"[ERROR] Data too large for encryption: {str(e)}")
            raise ValueError(f"Data size error: {str(e)}")
        except Exception as e:
            print(f"[ERROR] Encryption failed: {str(e)}")
            raise RuntimeError(f"Encryption error: {str(e)}")

    @staticmethod
    def decrypt_with_private_key(private_key: Any, encrypted_data: bytes) -> bytes:
        """
        Decrypts data using RSA private key with OAEP padding.
        Args:
            private_key: RSA private key for decryption
            encrypted_data: Encrypted data to decrypt
        Returns:
            Decrypted data as bytes
        Raises:
            ValueError: If decryption fails due to invalid input
            RuntimeError: If decryption fails for other reasons
        """
        print("[INFO] Decrypting data with private key...")
        try:
            decrypted_data = private_key.decrypt(
                encrypted_data,
                padding.OAEP(
                    mgf=padding.MGF1(algorithm=hashes.SHA256()),
                    algorithm=hashes.SHA256(),
                    label=None
                )
            )
            print("[SUCCESS] Data decrypted successfully")
            return decrypted_data
        except ValueError as e:
            print(f"[ERROR] Invalid ciphertext or key: {str(e)}")
            raise ValueError(f"Decryption input error: {str(e)}")
        except Exception as e:
            print(f"[ERROR] Decryption failed: {str(e)}")
            raise RuntimeError(f"Decryption error: {str(e)}")