from storage import get_cipher, save_passwords, load_passwords
from utils import ask_master_password
from password_checker import check_strength
from password_generator import generate_password

def main():
    master_password = ask_master_password()
    cipher = get_cipher(master_password)

    try:
        passwords = load_passwords(cipher)
    except ValueError as e:
        print(e)
        return

    while True:
        print("\n🔐 Password Manager")
        print("1. Check Password Strength")
        print("2. Generate Strong Password")
        print("3. Save New Password")
        print("4. Retrieve Saved Passwords")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            pwd = input("Enter password to check: ")
            print("Strength:", check_strength(pwd))

        # elif choice == "2":
        #     length = int(input("Enter length of password: "))
        #     pwd = generate_password(length)
        #     print("Generated Password:", pwd)
        
        elif choice == "2":
            from password_generator import ask_password_length
            length = ask_password_length()
            pwd = generate_password(length)
            print("🔑 Generated Password:", pwd)


        elif choice == "3":
            site = input("Enter site/app name: ")
            username = input("Enter username: ")
            pwd = input("Enter password: ")
            passwords[site] = {"username": username, "password": pwd}
            save_passwords(passwords, cipher)
            print("✅ Password saved securely!")

        elif choice == "4":
            for site, creds in passwords.items():
                print(f"{site}: {creds['username']} / {creds['password']}")

        elif choice == "5":
            print("👋 Exiting...")
            break
        else:
            print("❌ Invalid choice")

if __name__ == "__main__":
    main()
