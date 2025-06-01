from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding, rsa
from typing import Optional


class AsymmetricCrypto:
    """A class for asymmetric encryption and decryption using RSA with OAEP padding."""

    def __init__(self):
        self.private_key = None
        self.public_key = None

    def generate_keys(self) -> None:
        """
        Generates a new RSA key pair (private and public keys).

        The generated keys are stored in the instance variables:
        - self.private_key
        - self.public_key
        """

        self.private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048
        )
        self.public_key = self.private_key.public_key()
        print("[SUCCESS] Keys created successfully")


    def encrypt_with_public_key(self, data: bytes) -> Optional[bytes]:
        """
        Encrypts data using RSA public key with OAEP padding.
        Args:
            data: Data to be encrypted (typically a symmetric key)
        Returns:
            Encrypted data as bytes if successful, None otherwise
        Raises:
            RuntimeError: If encryption fails
        """
        print("[INFO] Encrypting data with public key...")
        try:
            encrypted_data = self.public_key.encrypt(
                data,
                padding.OAEP(
                    mgf=padding.MGF1(algorithm=hashes.SHA256()),
                    algorithm=hashes.SHA256(),
                    label=None
                )
            )
            print("[SUCCESS] Data encrypted successfully")
            return encrypted_data
        except Exception as e:
            print(f"[ERROR] Encryption failed: {str(e)}")
            raise RuntimeError(f"Encryption error: {str(e)}")

    def decrypt_with_private_key(self, encrypted_data: bytes) -> Optional[bytes]:
        """
        Decrypts data using RSA private key with OAEP padding.
        Args:
            encrypted_data: Encrypted data to decrypt
        Returns:
            Decrypted data as bytes if successful, None otherwise
        Raises:
            RuntimeError: If decryption fails
        """
        print("[INFO] Decrypting data with private key...")
        try:
            decrypted_data = self.private_key.decrypt(
                encrypted_data,
                padding.OAEP(
                    mgf=padding.MGF1(algorithm=hashes.SHA256()),
                    algorithm=hashes.SHA256(),
                    label=None
                )
            )
            print("[SUCCESS] Data decrypted successfully")
            return decrypted_data
        except Exception as e:
            print(f"[ERROR] Decryption failed: {str(e)}")
            raise RuntimeError(f"Decryption error: {str(e)}")