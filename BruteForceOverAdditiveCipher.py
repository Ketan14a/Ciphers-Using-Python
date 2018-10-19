#Python code for implementing Caesar Cipher

def encryptData(Plaintext,key):
    ctext = ""
    for i in range(Plaintext.__len__()):
        char = Plaintext[i]
        if (char.isupper()):
            ctext += chr((ord(char) + key - 65) % 26 + 65)
        else:
            ctext += chr((ord(char) + key - 97) % 26 + 97)

    print("The generated Cipher text is " + ctext)
    return ctext





def bruteForce(Ciphertext,key):
    ptext = ""
    for i in range(Ciphertext.__len__()):
        char = Ciphertext[i]
        if (char.isupper()):
            ptext += chr((ord(char) - key - 65) % 26 + 65)
        else:
            ptext += chr((ord(char) - key - 97) % 26 + 97)

    return ptext


# Program execution starts here
Ptext = input("Enter your plain text:")
key = int(input("Enter your key:"))

Ctext = encryptData(Ptext,key)

trialKey=0

print("Now, performing brute force attack:-")

while(True):
    print("Trying key = " + str(trialKey))
    TRY = bruteForce(Ctext,trialKey)
    if TRY==Ptext:
        print("Attack successful with key = " + str(trialKey))
        print("The plaintext is " + TRY)
        break
    else:
        print("Attack unsuccessful with key = " + str(trialKey))
        trialKey = trialKey + 1



























