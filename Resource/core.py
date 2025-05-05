from random import choice, randint
import string, pyperclip, os
from cryptography.fernet import Fernet

KEY_PATH = "./.key/encrypt.key"

def generate_password():
    length = randint(15, 20)
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(choice(chars) for _ in range(length))
    pyperclip.copy(password)
    return password

def gen_primary_key():
    key = Fernet.generate_key()
    with open(KEY_PATH, 'wb') as key_file:
        key_file.write(key)

def gen_secondary_key(username, passwd, another_user=False):
    with open(KEY_PATH, 'rb') as key_file:
        key = key_file.read()
    key_var = Fernet(key)
    main_key = key_var.encrypt(passwd.encode())
    print(Fernet.generate_key(),'\n', main_key)
    key_check = Fernet('password'.encode())
    if another_user:
        mode = 'a'
    else:
        mode = 'w'
    with open('../.env', mode) as file:
        file.write(f"PASSWD_MANAGER_KEY_{username}={key_var.encrypt(main_key)}")

    # Load

def save_passwd(website, email, passwd, note=''):
    pass

