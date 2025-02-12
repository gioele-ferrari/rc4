MOD_VAL = 256

'''
    Key Scheduling Algorithm (KSA)
    Inizializza il vettore S in base alla chiave.
'''
def KSA(key):
    scheduler = [i for i in range(MOD_VAL)]

    j = 0
    for i in range(MOD_VAL):
        j = (j + scheduler[i] + key[i % len(key)]) % MOD_VAL
        scheduler[i], scheduler[j] = scheduler[j], scheduler[i]

    return scheduler


'''
    Pseudo-Random Number Generator (PRNG)
    Genera il keystream per la cifratura/decifratura.
'''
def PRNG(scheduler):
    i = 0
    j = 0

    while True:
        i = (i + 1) % MOD_VAL
        j = (j + scheduler[i]) % MOD_VAL
        scheduler[i], scheduler[j] = scheduler[j], scheduler[i]

        t = (scheduler[i] + scheduler[j]) % MOD_VAL
        keystream = scheduler[t]
        yield keystream


'''
    Cifratura del testo in chiaro usando RC4.
'''
def encrypt(plain_text, key):
    plain_text = [ord(char) for char in plain_text]
    key = [ord(char) for char in key]

    scheduler = KSA(key)
    keystream = PRNG(scheduler)

    cipher_text = ''
    for byte in plain_text:
        cipher_byte = byte ^ next(keystream)
        cipher_text += f'{cipher_byte:02X}'

    return cipher_text


'''
    Decifratura del testo cifrato usando RC4.
'''
def decrypt(cipher_text, key):
    cipher_bytes = [int(cipher_text[i:i+2], 16) for i in range(0, len(cipher_text), 2)]
    key = [ord(char) for char in key]

    scheduler = KSA(key)
    keystream = PRNG(scheduler)

    plain_text = ''
    for byte in cipher_bytes:
        plain_char = chr(byte ^ next(keystream))
        plain_text += plain_char
    
    return plain_text


'''
    Funzione principale per testare la cifratura e decifratura.
'''
if __name__ == "__main__":

    # Test 1 proposto da Wikipedia
    plain_text = "Plaintext"
    key = "Key"

    print("Test RC4 Cipher Implementation")
    print(f"Plain Text: {plain_text}")
    print(f"Key: {key}")

    cipher_text = encrypt(plain_text, key)
    print(f"Cipher Text (Hex): {cipher_text}")
    
    assert cipher_text == "BBF316E8D940AF0AD3", "Errore nella cifratura!"

    decrypted_text = decrypt(cipher_text, key)
    print(f"Decrypted Text: {decrypted_text}")

    # Verifica
    assert plain_text == decrypted_text, "La decifratura non corrisponde al testo originale!"
    print("Test completato con successo!")
