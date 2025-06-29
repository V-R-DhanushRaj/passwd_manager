from random import choice, randint
import string, pyperclip, os, base64, csv, json
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from dotenv import load_dotenv

KEY_PATH = "./Resource/keys/encrypt.key"

def generate_password():
    length = randint(19, 23)
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
    with open('./.env', mode) as env_file:
        env_file.write(f'PASSWD_MANAGER_{username.upper()}={sec_key.decode()}')


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


def create_file(username):
    with open(f'./Data/{username}.csv', 'w', newline='') as data_file:
        pass
    encrypt_data(username)


def encrypt_data(username):
    f_key = Fernet(get_key(username))
    with open(f'./Data/{username}.csv', 'r') as data_file:
        data = data_file.read()
    enc_data = f_key.encrypt(data.encode())
    with open(f'./Data/{username}.csv', 'w') as data_file:
        data_file.write(enc_data.decode())


def decrypt_data(username):
    f_key = Fernet(get_key(username))
    with open(f'./Data/{username}.csv', 'r') as data_file:
        data = data_file.read()
    dec_data = f_key.decrypt(token=data.encode()).decode()
    with open(f'./Data/{username}.csv', 'w') as data_file:
        data_file.write(dec_data)


def save_passwd(username, website, email, passwd, note):
    data = get_data(username)
    try:
        prev_index = int(data[-1][0])
    except:
        prev_index = -1

    decrypt_data(username)
    with open(f'./Data/{username}.csv', 'w', newline='') as data_file:
        writer = csv.writer(data_file)
        data.append([prev_index+1, website, email, passwd, note.strip()])
        writer.writerows(data)
    encrypt_data(username)


def get_data(username):
    decrypt_data(username)
    with open(f'./Data/{username}.csv', 'r', newline='') as data_file:
        data = []
        for i in csv.reader(data_file):
            data.append(i)
    encrypt_data(username)
    return data


def dashboard_data(username):
    decrypt_data(username)
    password = []
    mail_id = []
    site_secured = []
    with open(f'./Data/{username}.csv', 'r', newline='') as data_file:
        data = csv.reader(data_file)
        if data != []:
            for i in data:
                password.append(i[3])
                if i[2] not in mail_id:
                    mail_id.append(i[2])
                if i[1] not in site_secured:
                    site_secured.append(i[1])
    encrypt_data(username)
    return len(password), len(mail_id), len(site_secured)

def search_passwd(search, username):
    decrypt_data(username)
    with open(f'./Data/{username}.csv', 'r', newline='') as data_file:
        data = csv.reader(data_file)
        searched_pass = []
        for i in data:
            if search.strip().lower() in i[1].lower():
                searched_pass.append(i)
    encrypt_data(username)
    if searched_pass == []:
        return None
    else:
        return searched_pass

def change_data(username, new_data):
    decrypt_data(username)
    with open(f'./Data/{username}.csv', 'w', newline='') as data_file:
        writter = csv.writer(data_file)
        writter.writerows(new_data)
    encrypt_data(username)

def data_exist(username, website, email):
    de = False
    decrypt_data(username)
    with open(f'./Data/{username}.csv', 'r', newline='') as data_file:
        datas = csv.reader(data_file)
        for data in datas:
            if data[1].lower() == website.lower() and data[2].lower() == email.lower():
                de = True
    encrypt_data(username)
    return de

def change_theme_to(theme):
    with open('./Resource/setting.json','r') as settings_file:
        data = json.load(settings_file)
    data["appearance_mode"] = theme
    with open('./Resource/setting.json', 'w') as settings_file:
        json.dump(data, settings_file)

def get_theme():
    with open('./Resource/setting.json') as settings_file:
        data = json.load(settings_file)
    print(data["appearance_mode"])
    return data["appearance_mode"]