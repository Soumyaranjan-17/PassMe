import os
import json
import base64
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet

STORAGE_FILE = "data/passwords.enc"
SALT_FILE = "data/salt.bin"

# Ensure data folder always exists
os.makedirs("data", exist_ok=True)

def get_salt() -> bytes:
    """Return existing salt or generate a new one"""
    if not os.path.exists(SALT_FILE):
        salt = os.urandom(16)
        with open(SALT_FILE, "wb") as f:
            f.write(salt)
        return salt
    else:
        with open(SALT_FILE, "rb") as f:
            return f.read()

def derive_key(master_password: str, salt: bytes) -> bytes:
    """Derive a secure key from the master password using PBKDF2"""
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=390000,  # large number to slow brute-force
    )
    return base64.urlsafe_b64encode(kdf.derive(master_password.encode()))

def get_cipher(master_password: str) -> Fernet:
    """Return Fernet cipher tied to master password"""
    salt = get_salt()
    key = derive_key(master_password, salt)
    return Fernet(key)

def save_passwords(passwords: dict, cipher: Fernet):
    """Encrypt and save passwords"""
    data = json.dumps(passwords).encode()
    encrypted = cipher.encrypt(data)
    with open(STORAGE_FILE, "wb") as f:
        f.write(encrypted)

def load_passwords(cipher: Fernet) -> dict:
    """Decrypt and load passwords"""
    if not os.path.exists(STORAGE_FILE):
        return {}
    with open(STORAGE_FILE, "rb") as f:
        encrypted = f.read()
    try:
        decrypted = cipher.decrypt(encrypted)
        return json.loads(decrypted.decode())
    except Exception:
        raise ValueError("❌ Incorrect master password!")
