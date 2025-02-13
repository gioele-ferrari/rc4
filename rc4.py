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
    La funzione usa .encode() che trasformare in un oggetto bytes
'''
def encrypt(plain_text, key):
    plain_text = plain_text.encode()
    key = key.encode()

    scheduler = KSA(key)
    keystream = PRNG(scheduler)

    cipher_bytes = bytes([byte ^ next(keystream) for byte in plain_text])
    cipher_text = cipher_bytes.hex().upper()
    
    return cipher_text


'''
    Decifratura del testo cifrato usando RC4.
'''
def decrypt(cipher_text, key):
    cipher_bytes = list(bytes.fromhex(cipher_text))
    key = key.encode()

    scheduler = KSA(key)
    keystream = PRNG(scheduler)
    plain_text = ''.join([chr(byte ^ next(keystream)) for byte in cipher_bytes])
    
    return plain_text


'''
    Funzione principale per testare la cifratura e decifratura.
'''
if __name__ == "__main__":
    if sys.argv[1] in options:
        input_text = input("[Text]: ")
        input_key = input("[Key]: ")

        if sys.argv[1] == "-d":
            print(f'[Plain Text]: {decrypt(cipher_text=input_text, key=input_key)}')    
        else:
            print(f'[Cipher Text]: {encrypt(plain_text=input_text, key=input_key)}')    
    else:
        print("Specifica una opzione valida (-d, -e)")