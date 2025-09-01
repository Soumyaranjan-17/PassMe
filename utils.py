from getpass import getpass

def ask_master_password() -> str:
    return getpass("Enter master password: ")
