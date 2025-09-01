# 🔐 PassMe – Secure CLI Password Manager

A simple **command-line password manager** built in Python for learning cybersecurity basics.
It can **check password strength, generate strong passwords, and store them securely in an encrypted file system** using your master password.

---

## 🚀 Features

✅ **Password Strength Checker** – Test your passwords against best practices.
✅ **Strong Password Generator** – Create random, secure passwords with custom length.
✅ **Encrypted Storage** – Save and retrieve passwords, locked with a master password.
✅ **PBKDF2 + AES Encryption** – Strong security with password-derived key and salt.
✅ **Cross-Platform** – Runs on Windows, Linux, or macOS.
✅ **Beginner-Friendly** – Clean Python code with modular structure.

---

## 📂 Project Structure

```
password_manager/
│── main.py                  # Entry point (menu system)
│── password_checker.py       # Password strength checker
│── password_generator.py     # Secure password generator
│── storage.py                # Encryption & storage handler
│── utils.py                  # Helper functions
│── requirements.txt          # Dependencies
│── data/
    ├── passwords.enc         # Encrypted password database
    └── salt.bin              # Salt for key derivation
```

---

## 🛠️ Installation

### 1. Clone Repository

```bash
git clone https://github.com/your-username/passme.git
cd passme
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate it:

* **Windows (PowerShell):**

  ```bash
  venv\Scripts\activate
  ```
* **Linux/macOS:**

  ```bash
  source venv/bin/activate
  ```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Usage

Run the program:

```bash
python main.py
```

You’ll see the menu:

```
🔐 Password Manager
1. Check Password Strength
2. Generate Strong Password
3. Save New Password
4. Retrieve Saved Passwords
5. Exit
```

* **First Run:** Enter a master password (used for encryption).
* **Later Runs:** Use the same master password to unlock storage.

---

## 🧩 Example Workflow

1. **Generate a Password**

   * Option `2` → Generate 16-char random password.

2. **Save a Password**

   * Option `3` → Enter site/app name, username, and password.

3. **Retrieve Passwords**

   * Option `4` → View stored credentials (decrypted on-the-fly).

---

## 🔒 Security Notes

* Uses **PBKDF2 (390k iterations)** with a random **salt** to derive a secure key.
* Encrypts data with **AES-256 (Fernet)**.
* Wrong master password = cannot decrypt data.
* Passwords are stored **locally only** (no cloud sync).

⚠️ **Disclaimer:** This project is for **learning purposes only**.
Do not use it as your primary password manager for sensitive accounts.

---

## 🌟 Future Improvements

* Clipboard copy (avoid showing password in console).
* Auto-expiry reminders for old passwords.
* GUI version with Tkinter / PyQt.
* Browser extension for autofill.

---

## 👨‍💻 Author

**Soumya Ranjan Sahoo** – Cybersecurity & Python Enthusiast 🚀

