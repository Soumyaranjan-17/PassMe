import secrets
import string

def generate_password(length: int = 16) -> str:
    """Generate a strong random password"""
    alphabet = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(alphabet) for _ in range(length))

def ask_password_length() -> int:
    """Ask user for a valid password length"""
    while True:
        try:
            length_input = input("Enter length of password (min 8, default 16): ").strip()
            if length_input == "":
                return 16  # Default length
            length = int(length_input)
            if length < 8:
                print("❌ Password length should be at least 8 characters. Try again.")
            else:
                return length
        except ValueError:
            print("❌ Invalid input! Please enter a number.")
