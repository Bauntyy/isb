import os
from cryptography.hazmat.primitives.asymmetric import rsa
from asymmetrical import AsymmetricCrypto

class GenerateKeys:

    @staticmethod
    def generate_sym_key() :

        key = os.urandom(32)
        nonce = os.urandom(16)
        print("[SUCCESS] Key and nonce created successfully")
        return key, nonce

    @staticmethod
    def generate_rsa_key_pair():

        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048
        )
        public_key = private_key.public_key()
        print("[SUCCESS] Keys created successfully")
        return public_key, private_key

    @staticmethod
    def generate_and_encrypt_keys(config: dict) -> tuple:
        """
        Generates symmetric and asymmetric keys, then encrypts the symmetric key.
        Args:
            config: Dictionary containing configuration parameters including:
                - 'symmetric_key_path': Primary path for symmetric key storage
                - 'symmetric_key': Fallback path if primary not specified

        Returns:
            tuple: (public_key, private_key, encrypted_symmetric_key)
        Raises:
            SystemExit: If no valid path is provided in the configuration
        """
        print("Starting key generation process...")

        symmetric_key, nonce = GenerateKeys.generate_sym_key()
        public_key, private_key = GenerateKeys.generate_rsa_key_pair()

        symmetric_key_path = config.get('symmetric_key_path')

        if not symmetric_key_path:
            print("[ERROR] No valid path specified for symmetric key storage in configuration")
            exit(1)

        encrypted_sym_key = AsymmetricCrypto.encrypt_with_public_key(public_key, symmetric_key)

        print("[SUCCESS] Key generation and encryption completed successfully")
        return public_key, private_key, encrypted_sym_key
