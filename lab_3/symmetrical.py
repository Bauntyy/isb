import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms
from typing import Tuple


class SymmetricCrypto:
    """
    A class providing symmetric encryption operations using ChaCha20 algorithm.
    """

    @staticmethod
    def sym_encrypt_chacha20(text: bytes, key: bytes, nonce: bytes = None) -> Tuple[bytes, bytes]:
        """
        Encrypts data using ChaCha20 symmetric encryption algorithm.
        Args:
            text: The data to be encrypted as bytes
            key: The encryption key (must be 32 bytes)
            nonce: Optional nonce value (16 bytes). If None, will be generated.
        Returns:
            A tuple containing (ciphertext, nonce)
        """
        try:
            if nonce is None:
                nonce = os.urandom(16)

            cipher = Cipher(
                algorithm=algorithms.ChaCha20(key, nonce),
                mode=None,
                backend=default_backend()
            )
            encryptor = cipher.encryptor()
            ciphertext = encryptor.update(text) + encryptor.finalize()

            print("[SUCCESS] Encryption completed successfully")
            return ciphertext, nonce

        except ValueError as e:
            print(f"[ERROR] Encryption failed: {str(e)}")
            raise ValueError(f"Encryption error: {str(e)}")
        except Exception as e:
            print(f"[ERROR] Unexpected encryption error: {str(e)}")
            raise

    @staticmethod
    def sym_decrypt_chacha20(ciphertext: bytes, key: bytes, nonce: bytes) -> bytes:
        """
        Decrypts data using ChaCha20 symmetric encryption algorithm.
        Args:
            ciphertext: The encrypted data to decrypt
            key: The encryption key (must match key used for encryption)
            nonce: The nonce used during encryption (16 bytes)
        Returns:
            The decrypted plaintext as bytes

        """
        try:
            cipher = Cipher(
                algorithm=algorithms.ChaCha20(key, nonce),
                mode=None,
                backend=default_backend()
            )
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