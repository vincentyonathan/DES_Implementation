import secrets
import DES
from Functions import get_random_string

if __name__ == '__main__':
    
    print("Single DES\n\n")
    plaintext = input("Enter plaintext: ")

    key = get_random_string(8)

    print("Key: ", key)
    ciphertext = DES.Encrypt(plaintext, key)
    print("Ciphered Text (Encrypted): ", ciphertext)

    decrypted = DES.Decrypt(ciphertext, key)
    print("Decrypted: ", decrypted)