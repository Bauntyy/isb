import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms
from typing import Tuple


class SymmetricCrypto:
    """
    A class providing symmetric encryption operations using ChaCha20 algorithm.
    """

    def __init__(self):
        self.key = None
        self.nonce = None

    def generate_key(self) -> None:
        """
        Generates a random key and nonce for ChaCha20 symmetric encryption.

        The generated values are stored in instance variables:
        - self.key
        - self.nonce
        """
        self.key = os.urandom(32)
        self.nonce = os.urandom(16)
        print("[SUCCESS] Key and nonce created successfully")

    def sym_encrypt_chacha20(self, text: bytes) -> Tuple[bytes, bytes]:
        """
        Encrypts data using ChaCha20 symmetric encryption algorithm.
        Args:
            text: The data to be encrypted as bytes.
        Returns:
            A tuple containing (ciphertext, nonce) where:
            - ciphertext: The encrypted data
            - nonce: Random value used for encryption (16 bytes)
        Raises:
            ValueError: If key length is invalid or encryption fails.
        """
        try:
            cipher = Cipher(
                algorithm=algorithms.ChaCha20(self.key, self.nonce),
                mode=None,
                backend=default_backend()
            )
            encryptor = cipher.encryptor()
            ciphertext = encryptor.update(text) + encryptor.finalize()

            print("[SUCCESS] Encryption completed successfully")
            return ciphertext, self.nonce

        except ValueError as e:
            print(f"[ERROR] Encryption failed: {str(e)}")
            raise ValueError(f"Encryption error: {str(e)}")
        except Exception as e:
            print(f"[ERROR] Unexpected encryption error: {str(e)}")
            raise

    def sym_decrypt_chacha20(self, ciphertext: bytes) -> bytes:
        """
        Decrypts data using ChaCha20 symmetric encryption algorithm.
        Args:
            ciphertext: The encrypted data to decrypt.
        Returns:
            The decrypted plaintext as bytes.
        Raises:
            ValueError: If decryption fails due to invalid key/nonce or corrupted data.
        """
        try:
            # Initialize cipher with same parameters used for encryption
            cipher = Cipher(
                algorithm=algorithms.ChaCha20(self.key, self.nonce),
                mode=None,
                backend=default_backend()
            )

            # Perform decryption
            decryptor = cipher.decryptor()
            plaintext = decryptor.update(ciphertext) + decryptor.finalize()

            print("[SUCCESS] Decryption completed successfully")
            return plaintext

        except ValueError as e:
            print(f"[ERROR] Decryption failed: {str(e)}")
            raise ValueError(f"Decryption error: {str(e)}")
        except Exception as e:
            print(f"[ERROR] Unexpected decryption error: {str(e)}")
            raise