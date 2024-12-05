# Secure-File-Transfer-and-Encryption-System
 
 #### Python program for secure file transfer and RSA-based encryption.


This README file provides an overview of the code for a simple file encryption and secure file transfer system using Python, the rsa library for encryption, and the paramiko library for SSH communication. The system allows you to generate encryption keys, encrypt files, and send them securely to a recipient's machine over SSH. You can also decrypt files using your private key.

## Prerequisites
Before using this code, ensure you have the following prerequisites in place:

 Python: Make sure you have Python installed on your system.

 Required Libraries: Install the necessary libraries using the following commands:  
```bash      
pip install rsa paramiko
```
## Usage

#### 1. Generate Keys: 
* The generate_keys() function generates a pair of public and private RSA keys (1024 bits) and saves them to 'pubkey.pem' and 'privkey.pem' files. You only need to call this function once when running the program for the first time.

#### 2. Load Keys: 
* The load_keys() function loads the previously generated keys from the 'pubkey.pem' and 'privkey.pem' files. This is essential for both encryption and decryption.

#### 3. Encrypt a File:
* The encrypt(file, key) function takes the name of a file to be encrypted and the recipient's name as input.
* It checks if the recipient's public key exists in a file named 'Kali_pubkey.pem' (you can replace 'Kali' with the recipient's name). If found, it encrypts the file using the recipient's public key and saves it as 'encrypted.txt'.
* If the recipient's public key is not found, it displays an error message.

### 4. Decrypt a File:
* The decrypt(file, key) function takes the name of the file to be decrypted and the private key as input.
* It attempts to decrypt the file using the private key and returns the decrypted content as plain text.
* If decryption fails (e.g., due to an incorrect key), it returns False.

#### 5. Send a File:

* The send_file(file, host) function is used to securely upload the encrypted file to a recipient's machine over SSH.
* It connects to the recipient's machine using SSH with the provided IP address, username, and password.
* It uses SFTP (Secure File Transfer Protocol) to transfer the 'encrypted.txt' file to the recipient's machine.

#### 6. Main Menu:

* The main menu allows you to choose between two options:
Option 1: Send an encrypted file.
Option 2: Decrypt a specific file.
* You need to enter the name of the file you wish to process, including the file extension.

#### 7. Example Usage:

* When selecting option 1, you can enter the name of the file and the recipient's name. The file will be encrypted and securely sent to the recipient's machine.
* When selecting option 2, you can enter the name of the file you wish to decrypt. If the private key is valid, it will display the plain text content.


## Important Notes
* Ensure that you have the recipient's public key saved in a file with a name like 'Kali_pubkey.pem' (replace 'Kali' with the recipient's name) to successfully encrypt and send files.
* The provided SSH connection details in the send_file() function are hardcoded. Update the hostname, username, and password according to your needs.

## Disclaimer
This code is a basic example of file encryption and secure file transfer. It is not suitable for production use as it lacks error handling and proper key management. For production-level security, consider using well-established encryption and key management solutions.
