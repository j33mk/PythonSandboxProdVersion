from cryptography.fernet import Fernet

def generate_key():
    key = Fernet.generate_key()
    with open("secret.key","wb") as key_file:
        key_file.write(key)
        print('key is generated')

def load_key():
    return open("secret.key","rb").read()

def encrypt_message(message):
    key = load_key()
    encoded_msg = message.encode()
    f = Fernet(key)
    encrypted_msg = f.encrypt(encoded_msg)
    return encrypted_msg

def decrypt_message(enc_msg):
    key = load_key()
    f = Fernet(key)
    dec_msg = f.decrypt(enc_msg)
    return dec_msg.decode()

enc = encrypt_message('hey i am jamal hussain')
print(enc)
dec = decrypt_message(enc)
print(dec)