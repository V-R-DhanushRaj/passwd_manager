from random import choice, randint
import string, pyperclip, os, base64, csv
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from dotenv import load_dotenv

KEY_PATH = "keys/encrypt.key"

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

def gen_secondary_key(username: str, passwd, another_user=False):
    if another_user:
        mode = 'a'
    else:
        mode = 'w'
    sec_key = passwd_to_key(passwd)
    with open('../.env', mode) as env_file:
        env_file.write(f'PASSWD_MANAGER_{username.upper()}={sec_key}')

def passwd_to_key(passwd, key_len=32):
    with open(KEY_PATH, 'rb') as key_file:
        salt = key_file.read()
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=key_len,
        salt=salt,
        iterations=100_100,
        backend=default_backend()
    )
    key = base64.urlsafe_b64encode(kdf.derive(passwd.encode()))
    return key

def get_key(username):
    load_dotenv()
    return os.getenv(f"PASSWD_MANAGER_{username.upper()}")
def create_file(username, datas):
    with open(f'../Data/{username}.csv', 'w') as data_file:
        writer = csv.writer(data_file)
        for data in datas:
            writer.writerow(data)
    decrypt_data(username, get_key(username))

def encrypt_data(username):
    f_key = Fernet(get_key(username))
    with open(f'../Data/{username}.csv', 'r') as data_file:
        data = data_file.read()
    enc_data = f_key.encrypt(data.encode())
    with open(f'../Data/{username}.csv', 'w') as data_file:
        data_file.write(enc_data.decode())


def decrypt_data(username):
    try:
        f_key = Fernet(get_key(username))
        with open(f'../Data/{username}.csv', 'r') as data_file:
            data = data_file.read()
        dec_data = f_key.decrypt(data)
        with open(f'../Data/{username}.csv', 'w') as data_file:
            data_file.write(dec_data)
    except:
        pass    # For some reason it gives invalid token error but decrypts correctly


def save_passwd(username, website, email, passwd, note=''):
    pass


gen_secondary_key(username='dhanushrajvr', passwd='password1234')