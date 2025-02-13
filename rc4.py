import sys

MOD_VAL = 256
options = ["-d", "-e"]

'''
    Key Scheduling Algorithm (KSA)
    Inizializza il vettore S in base alla chiave.
    
    Algoritmo proposto da Wikipedia:
    for i from 0 to 255
        S[i] := i
    endfor
    j := 0
    for i from 0 to 255
        j := (j + S[i] + key[i mod keylength]) mod 256
        swap values of S[i] and S[j]
    endfor
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
    
    Algoritmo proposto da Wikipedia:
    i := 0
    j := 0
    while GeneratingOutput:
        i := (i + 1) mod 256
        j := (j + S[i]) mod 256
        swap values of S[i] and S[j]
        t := (S[i] + S[j]) mod 256
        K := S[t]
        output K
    endwhile
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
    # Prende i valori due a due dal testo e li trasforma in byte
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
    if sys.argv[1] in options:
        input_text = input("[Text]: ")
        input_key = input("[Key]: ")

        if sys.argv[1] == "-d":
            print(decrypt(cipher_text=input_text, key=input_key))    
        else:
            print(encrypt(plain_text=input_text, key=input_key))    
    else:
        print("Specifica una opzione valida (-d, -e)")