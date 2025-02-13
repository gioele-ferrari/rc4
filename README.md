# Cifrario RC4

Questa implementazione in Python del **cifrario RC4** include funzionalità di **cifratura** e **decifratura**. RC4 è un cifrario a flusso simmetrico che genera un keystream pseudo-casuale combinato con il testo in chiaro tramite operazione XOR. Sebbene RC4 non sia più considerato sicuro per applicazioni moderne, è utile per capire il funzionamento dei cifrari a flusso.

---

## **Struttura del Progetto**

1. **Key Scheduling Algorithm (KSA):** Inizializza il vettore `scheduler` in base alla chiave.
2. **Pseudo-Random Number Generator (PRNG):** Genera il keystream usato per la cifratura e la decifratura.
3. **Funzioni di Cifratura e Decifratura:** Applicano l'operazione XOR tra il testo e il keystream.
4. **Test:** Verifica il corretto funzionamento del cifrario.

---

## **Funzionalità principali**

### **1. Decifratura**

L'utente può interagire con il programma per decifrare con il seguente comando: `python3 rc4.py -d`.

### **2. Cifratura**

L'utente può interagire con il programma per cifrare con il seguente comando: `python3 rc4.py -c`.

---

## **Testing**

Sono stati eseguiti test sul funzionamento del cifrario, attraverso esempi proposti da Wikipedia, nella sezione [Test vectors]("https://en.wikipedia.org/wiki/RC4").

## **Note**

RC4 non è più considerato sicuro a causa di vulnerabilità note. Come la presenza di regolarità
