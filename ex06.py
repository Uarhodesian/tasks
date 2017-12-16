# 6.Define a function caesar_cipher that takes string and key(number), whuch returns encrypted string

def caesar(st, key):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    cipher = ""
        for c in st:
            if c in alphabet:
                cipher += alphabet[(alphabet.index(c) + key) % len(alphabet)]
                return cipher


