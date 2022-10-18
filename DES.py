from Functions import *
import Key
import Algorithm

def Encrypt(plainText, key):
    #Pad the plain text so it's keep on 64 bit (8 Char)
    plainText = padding(plainText)

    #Next is converting both to binary
    binaryPlain = str_to_binary(plainText)
    binaryKey = str_to_binary(key)

    print('Text (with Padded 0) :', plainText)
    print('Text (in Binary) :', binaryPlain)
    print('Key (in Binary) :', binaryKey)
    
    transformedKey = Algorithm.DES_Key(binaryKey)
    cipher = Algorithm.encrypt(binaryPlain, transformedKey) 
    return cipher

def Decrypt(cipherText, key):

    binaryCipher = str_to_binary(cipherText)
    binaryKey = str_to_binary(key)

    print('Key (in Binary): ', binaryKey)
    print('Encrypted (in Binary): ', binaryCipher)
    transformedKey = Algorithm.DES_Key(binaryKey)
    reversedKey = transformedKey[::-1]
    print("Key : ", transformedKey)
    print("Reversed Key : ", reversedKey)

    decryptmessage = Algorithm.encrypt(binaryCipher, reversedKey)
    return decryptmessage



    

