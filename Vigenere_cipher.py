# vigenere_cipher.py

def vigenere(message, key, direction=1):
    key_index = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    final_message = ''

    for char in message.lower():
        if not char.isalpha():
            final_message += char
        else:
            key_char = key[key_index % len(key)]
            key_index += 1

            offset = alphabet.index(key_char)
            index = alphabet.find(char)
            new_index = (index + offset * direction) % len(alphabet)
            final_message += alphabet[new_index]

    return final_message

def encrypt(message, key):
    return vigenere(message, key)

def decrypt(message, key):
    return vigenere(message, key, -1)

if __name__ == "__main__":
    text = 'mrttaqrhknsw ih puggrur'
    custom_key = 'happycoding'

    print(f'\nEncrypted text: {text}')
    print(f'Key: {custom_key}')
    decrypted = decrypt(text, custom_key)
    print(f'\nDecrypted text: {decrypted}\n')
