#Python code for implementing Caesar Cipher

def encryptData(Plaintext,key):
    ctext = ""
    for i in range(Plaintext.__len__()):
        char = Plaintext[i]
        if (char.isupper()):
            ctext += chr((ord(char) + key - 65) % 26 + 65)
        else:
            ctext += chr((ord(char) + key - 97) % 26 + 97)

    print("The Cipher text is ", ctext)




def decryptData(Ciphertext,key):
    ptext = ""
    for i in range(Ciphertext.__len__()):
        char = Ciphertext[i]
        if (char.isupper()):
            ptext += chr((ord(char) - key - 65) % 26 + 65)
        else:
            ptext += chr((ord(char) - key - 97) % 26 + 97)

    print("The Plain text is ", ptext)

#Program Execution starts from here..............

Username = input("Enter username:-")
Password = input("Enter your password:-")


if Username=="Scooby" and Password=="Shaggy":

    print("Press 1 for encrypting a plaintext")
    print("Press 2 for decrypting a ciphertext")
    choice = int(input("Enter your choice:"))
    if choice==1:
        Plaintext = input("Enter your plaintext:-")
        key = int(input("Please enter the key value:-"))
        encryptData(Plaintext,key)



    elif choice==2:
        Ciphertext = input("Enter your ciphertext:-")
        key = int(input("Please enter the key value:-"))
        decryptData(Ciphertext,key)

else:
    print("Invalid User!Not allowed to execute this program!")







