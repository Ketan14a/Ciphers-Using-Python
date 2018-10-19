#generating the Vigenere Square

VsquareSmall = []
VsquareCapital = []
count=0
Alphacount=0

for i in range(26):
    VsquareSmall.append([])
    VsquareCapital.append([])




for i in range(26):
    for j in range(26):
        VsquareSmall[i].append(chr(97+count))
        VsquareCapital[i].append(chr(65+count))
        count+=1
        if count>=26:
            count=0
    Alphacount+=1
    count=Alphacount

print("Press 1 for encrypting the Plaintext")
print("Press 2 for decrypting the Ciphertext")
choice=int(input("Enter your choice:"))

if choice==1:
    Ptext=input("Enter your plaintext:")
    keystream = input("Enter your Keystream:")
    Ctext=""
    ksptr = 0

    for i in range(Ptext.__len__()):
        char = Ptext[i]

        if char.isupper():
            keychar = keystream[ksptr]
            if keychar.islower():
                keychar = keychar.upper()

            posI = ord(char)-65
            posJ = ord(keychar)-65

            Ctext+=VsquareCapital[posI][posJ]
            ksptr+=1
            if ksptr==keystream.__len__():
                ksptr=0

        else:
            keychar = keystream[ksptr]
            if keychar.isupper():
                keychar = keychar.lower()

            posI = ord(char) - 97
            posJ = ord(keychar) - 97

            Ctext += VsquareSmall[posI][posJ]
            ksptr += 1
            if ksptr ==keystream.__len__():
                ksptr = 0


    print("The Ciphertext is ",Ctext)

elif choice==2:
    Ctext=input("Enter your Ciphertext:")
    keystream=input("Enter your keystream:")
    ksptr=0
    Ptext=""

    for i in range(Ctext.__len__()):
        char=Ctext[i]
        keychar=keystream[ksptr]
        count=0

        if(char.islower()):

            if(keychar.isupper()):
                keychar=keychar.lower()

            column = ord(keychar)-97
            check = VsquareSmall[count][column]
            print("The count value is " + str(count))
            print("The column value is " + str(column))
            print(VsquareCapital)

            while check!=char:
                count+=1
                check=VsquareCapital[count][column]

            Ptext+=chr(count+97)
            ksptr+=1
            if(ksptr==keystream.__len__()-1):
                ksptr=0

        else:
            if (keychar.islower()):
                keychar = keychar.upper()

            column = ord(keychar) - 65

            check = VsquareSmall[count][column]

            while check != char:
                count+= 1
                check = VsquareCapital[count][column]

            Ptext += chr(count + 65)
            ksptr += 1
            if (ksptr == keystream.__len__()):
                ksptr = 0


    print("The PlainText is ",Ptext)












