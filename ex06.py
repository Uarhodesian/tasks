# 6.Define a function caesar_cipher that takes string and key(number), whuch returns encrypted string
def caesar(string, key):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    cipher = " "
    for i in string:
        if i in alphabet:
                    cipher = cipher + alphabet[(alphabet.index(i) + key) % len(alphabet)]
    return cipher


