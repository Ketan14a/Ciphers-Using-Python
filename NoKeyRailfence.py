Ptext = input("Enter your plaintext:")
Plist = list(Ptext)

L1=[]
L2=[]
L3=[]
L4=[]

count=0
varcount=4

for i in Plist:
    if varcount==4:

        if count == 0:
            L1.append(i)
            count = 1
        elif count == 1:
            L2.append(i)
            count = 2
        elif count == 2:
            L3.append(i)
            count = 3
        elif count == 3:
            L4.append(i)
            varcount = 3
            count=0

    elif varcount==3:
        if count == 0:
            L1.append(i)
            count = 1
        elif count == 1:
            L2.append(i)
            count = 2
        elif count == 2:
            L3.append(i)
            count = 0

        elif count == 3:
            L4.append("")
            varcount = 2
            count=0

    elif varcount==2:
        if count == 0:
            L1.append(i)
            count = 1
        elif count == 1:
            L2.append(i)
            count = 0
            varcount=4
        elif count == 2:
            L3.append("")
            count = 3

        elif count == 3:
            L4.append("")
            varcount = 2
            count = 0




Clist=[]
for i in L1:
    Clist.append(i)

for i in L2:
    Clist.append(i)

for i in L3:
    Clist.append(i)

for i in L4:
    Clist.append(i)

Ctext = ''.join(Clist)

print("The ciphertext is " + Ctext)

pos=0
varcount=4
Plist=[]

L1len = L1.__len__()
L2len = L2.__len__()
L3len = L3.__len__()
L4len = L4.__len__()



for i in range(Ctext.__len__()):
    if varcount==4:
        if pos < L1len:
         Plist.append(L1[pos])
        if pos < L2len and L2[pos]!="":
         Plist.append(L2[pos])
        if pos < L3len and L3[pos]!="":
         Plist.append(L3[pos])
        if pos < L4len and L4[pos]!="":
         Plist.append(L4[pos])
        pos=pos+1
        varcount=3
    elif varcount==3:
        if pos < L1len:
         Plist.append(L1[pos])
        if pos < L2len and L2[pos]!="":
         Plist.append(L2[pos])
        if pos < L3len and L3[pos]!="":
         Plist.append(L3[pos])
        varcount=2
        pos = pos + 1

    elif varcount==2:
        if pos < L1len:
            Plist.append(L1[pos])
        if pos < L2len and L2[pos]!="":
            Plist.append(L2[pos])
        varcount=4
        pos = pos + 1



Ptext = ''.join(Plist)
print("The plain text is " + Ptext)















