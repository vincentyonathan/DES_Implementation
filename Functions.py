import math
import random
import string

'''Using Hexadecimal Key because it's an easy representation'''

def subtitution(text,table):
    # return ''.join(text[i-1] for i in table)
    result = ""
    for i in table:
        result += text[i-1]
    return result 

def str_to_binary(text):
    return ''.join(format(ord(i), '08b') for i in text)

def binary_to_str(bin_val):
    return ''.join(chr(int(bin_val[i:i+8],2)) for i in range(0,len(bin_val),8))

def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

def hex_to_bin(text):
    return format(int(text, 16), "064b")

def bin_to_hex(bin_val):
    result = ""
    for i in range(0, len(bin_val), 4):
        result = result + hex(int(bin_val[i: i + 4], 2))[2:] 
    return result

def dec_to_bin(dec_val):
    return bin(dec_val)[2:].zfill(4)

def xor(text,key):
    return ''.join(str(int(a) ^ int(b)) for a,b in zip(text,key))

def t_split(text):
    return text[:32],text[32:]

def k_split(text):
    return text[:28],text[28:]

def sbox(bin_val,table):
    # row = int(bin_val[0] + bin_val[-1],2)
    # col = int(bin_val[1:-1],2)
    return dec_to_bin(table[int(bin_val[0] + bin_val[-1],2)][int(bin_val[1:-1],2)])

def padding(text):
    padding = math.ceil(len(text) / 8) * 8
    return text.ljust(padding, " ")

# print(str_to_binary("hello world"))