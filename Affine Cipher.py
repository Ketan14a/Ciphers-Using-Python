a = int(input("Enter the value of slope:"))
b = int(input("Enter the value of intercept:"))

Ptext = input("Now, enter your plaintext:")
Clist = []

for i in Ptext:
    if i.isupper():
        AXPB = a * (ord(i)-65) + b
        Ans = AXPB % 26

        letter = chr(Ans+65)
        #print(letter)
        Clist.append(letter)
    else:
        AXPB = a * (ord(i) - 97) + b
        Ans = AXPB % 26

        letter = chr(Ans+97)
        #print(letter)
        Clist.append(letter)




Ctext = ''.join(Clist)

print("The Corresponding cipher text is " + Ctext)

