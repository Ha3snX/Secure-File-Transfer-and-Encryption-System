# -----------------------------------
# ------ Hasan Hamad Almalki --------
# -----------------------------------
import rsa
import paramiko

# Generate keys and save them to files
def generate_keys():
    pubKey, privKey = rsa.newkeys(1024)
    with open('pubkey.pem', 'wb') as f:
        f.write(pubKey.save_pkcs1('PEM'))

    with open('privkey.pem', 'wb') as f:
        f.write(privKey.save_pkcs1('PEM'))

# Load the keys from files
def load_keys():
    with open('pubkey.pem', 'rb') as f:
        pubKey = rsa.PublicKey.load_pkcs1(f.read())

    with open('privkey.pem', 'rb') as f:
        privKey = rsa.PrivateKey.load_pkcs1(f.read())

    return pubKey, privKey

# Encrypt a file using a recipient's public key
def encrypt(file, key):
    msg = open(file, "r").read()
    if key == "kali":
        with open('Kali_pubkey.pem', 'rb') as f:
            pub_Key = rsa.PublicKey.load_pkcs1(f.read())
    else:
        print(f"Sorry, We Don't Have The Public key for {key}")
        return

    cText = rsa.encrypt(msg.encode('ascii'), pub_Key)

    f = open("encrypted.txt", "wb")
    f.write(cText)

    return cText

# Decrypt a file using a private key
def decrypt(file, key):
    ciphertext = open(file, "rb").read()
    try:
        return rsa.decrypt(ciphertext, key).decode('ascii')
    except:
        return False

# Upload the file to a recipient's machine using SSH
def send_file(file, host):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    # Provide the recipient's IP address, username, and password for SSH connection
    ssh.connect(hostname="", username="", password="")
    
    # We are using SFTP to send files to the recipient's machine.
    ftp = ssh.open_sftp()
    ftp.put("encrypted.txt", "")
    ftp.close()
    ssh.close()
    print(f"The File {file} Was Uploaded Successfully to {host}")

# Generate keys (only needed to be called once when running the program for the first time)
generate_keys()

# Load the keys from the files
pubKey, privKey = load_keys()

# Main Menu
print("Please choose an option:")
print("1. Send A File")
print("2. Decrypt A File")
print("Please enter the name of the file you wish to open, including the file extension. For example, myfile.txt")
choice = input("")

# First Choice Is Send An Encrypted File
if choice == "1":
    # Provide the file name and recipient's name
    file = input('Enter a File name:')
    recipient = input("Enter the recipient name:")
    ciphertext = encrypt(file, recipient)
    send_file(file, recipient)

# Second Choice Is Decrypt A Specific File
if choice == "2":
    file = input('Enter a File name:')
    plaintext = decrypt(file, privKey)

    if plaintext:
        print(f'Plain text: {plaintext}')
    if plaintext == False:
        print("The Public Key Used To Encrypt Is Not Yours")

