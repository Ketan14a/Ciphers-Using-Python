import numpy as np

Ptext = input("Enter your plain text:")

if Ptext.__len__()%3!=0:
    for i in range(0, 10000000, 3):
        if Ptext.__len__() < i:
            if i % 3 == 0:
                residue = i - Ptext.__len__()
                break
else:
    residue=0


for i in range(residue):
    Ptext = Ptext + "x"

print(Ptext)
key = [[],[],[]]

print("Now enter 9 values in key matrix:")

for i in range(3):
    for j in range(3):
        value=int(input("Enter value:"))
        key[i].append(value)


flag=0
Ctext=""


for i in range(0,Ptext.__len__(),3):
    Pmatrix = []
    char0=Ptext[i]
    char1=Ptext[i+1]
    char2=Ptext[i+2]


    Pmatrix.append(ord(char0))
    Pmatrix.append(ord(char1))
    Pmatrix.append(ord(char2))



    Ans = [[0],[0],[0]]

    for i in range(3):
        for j in range(1):
            for k in range(3):
                Ans[i][j]+=key[i][k]*Pmatrix[k]





    for i in range(3):
        Ans[i][0]=Ans[i][0]%26
        Cipher0 = chr(Ans[i][0]+97)
        Ctext = Ctext + Cipher0
        #print(Ans[i][0])
        #print(Cipher0)

print("The ciphertext is " + Ctext)





# Encryption Over! Now, decrypting the cipher text

Ctext = input("Enter your Cipher Text:")
Ptext = ""

Ckey = np.linalg.inv(key)
Det = np.linalg.det(key)

for i in range(3):
    for j in range(3):
        Ckey[i][j] = Ckey[i][j] * Det


i=0
print(Det)

while True:
    i=i+1
    Ans = (26*i)+1
    if Ans % Det==0:
        break
    else:
        continue




for i in range(3):
    for j in range(3):
        Ckey[i][j] = Ckey[i][j] * i






for i in range(0,Ctext.__len__(),3):
    Cmatrix = []
    char0=Ctext[i]
    char1=Ctext[i+1]
    char2=Ctext[i+2]

    Cmatrix.append(ord(char0))
    Cmatrix.append(ord(char1))
    Cmatrix.append(ord(char2))



    Ans = [[0],[0],[0]]

    for i in range(3):
        for j in range(1):
            for k in range(3):
                Ans[i][j]+=Ckey[i][k]*Cmatrix[k]





    for i in range(3):
        Ans[i][0]=Ans[i][0]%26
        Cipher0 = chr(Ans[i][0]+97)
        Ptext = Ptext + Cipher0


print("The plaintext is " + Ptext)








