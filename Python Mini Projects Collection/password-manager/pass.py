from cryptography.fernet import Fernet
import json
import random
import string
import os

KEY_FILE = "key.key"
DATA_FILE = "passwords.json"

def generate_key():
    key = Fernet.generate_key()
    with open(KEY_FILE, "wb") as f:
        f.write(key)

def load_key():
    if not os.path.exists(KEY_FILE):
        generate_key()
    return open(KEY_FILE, "rb").read()

cipher = Fernet(load_key())

def load_passwords():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {}

def save_passwords(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

def generate_password():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=12))

while True:
    print("\n1. Store Password\n2. Retrieve Password\n3. Exit")
    choice = input("Choose: ")

    passwords = load_passwords()

    if choice == "1":
        site = input("Website: ")
        pwd = generate_password()
        encrypted = cipher.encrypt(pwd.encode()).decode()
        passwords[site] = encrypted
        save_passwords(passwords)
        print("Generated Password:", pwd)

    elif choice == "2":
        site = input("Website: ")
        if site in passwords:
            decrypted = cipher.decrypt(passwords[site].encode()).decode()
            print("Password:", decrypted)
        else:
            print("No password found")

    elif choice == "3":
        break