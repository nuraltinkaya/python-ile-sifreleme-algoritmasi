# Vigenere tablosu
vigenere_table = []
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for i in range(26):
    row = alphabet[i:] + alphabet[:i]
    vigenere_table.append(row)

# Fonksiyonlar
def vigenere_encrypt(plaintext, key):
    ciphertext = ''
    key_index = 0
    for char in plaintext:
        if char.isalpha():
            row = alphabet.index(key[key_index].upper())
            col = alphabet.index(char.upper())
            ciphertext += vigenere_table[row][col]
            key_index = (key_index + 1) % len(key)
        else:
            ciphertext += char
    return ciphertext

def caesar_encrypt(plaintext, shift):
    ciphertext = ''
    for char in plaintext:
        if char.isalpha():
            shifted_char = chr((ord(char.upper()) - 65 + shift) % 26 + 65)
            ciphertext += shifted_char
        else:
            ciphertext += char
    return ciphertext

def caesar_decrypt(ciphertext, shift):
    plaintext = ''
    for char in ciphertext:
        if char.isalpha():
            shifted_char = chr((ord(char.upper()) - 65 - shift) % 26 + 65)
            plaintext += shifted_char
        else:
            plaintext += char
    return plaintext

# Ana program
plaintext = input('Metin girin: ')
key = input('Anahtar kelime girin: ')

# Vigenere şifreleme
vigenere_ciphertext = vigenere_encrypt(plaintext, key)

# Sezar şifreleme
shift = len(key)
caesar_ciphertext = caesar_encrypt(vigenere_ciphertext, shift)

print('Şifreli metin:', caesar_ciphertext)

# Deşifreleme
caesar_plaintext = caesar_decrypt(caesar_ciphertext, shift)

# Vigenere deşifreleme
vigenere_plaintext = ''
key_index = 0
for char in caesar_plaintext:
    if char.isalpha():
        row = alphabet.index(key[key_index].upper())
        col = vigenere_table[row].index(char.upper())
        vigenere_plaintext += alphabet[col]
        key_index = (key_index + 1) % len(key)
    else:
        vigenere_plaintext += char

print('Orijinal metin:', vigenere_plaintext)