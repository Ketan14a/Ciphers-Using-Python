Ptext = input("Enter your plaintext:")
Plist = list(Ptext)
count=0

L1 = []
L2 = []
L3 = []

for i in Plist:
    if count==0:
        L1.append(i)
        count=1
    elif count==1:
        L2.append(i)
        count=2
    elif count==2:
        L3.append(i)
        count=0

Clist=[]
for i in L1:
    Clist.append(i)

for i in L2:
    Clist.append(i)

for i in L3:
    Clist.append(i)


Ctext = ''.join(Clist)
print(L1)
print(L2)
print(L3)
print("The cipherText is " + Ctext)
len1 = L1.__len__()
len2 = L2.__len__()
len3 = L3.__len__()

count=0
pos1=0
pos2=0
pos3=0


Plist=[]
for i in range(Ctext.__len__()):

    if count==0:
        Plist.append(L1[pos1])
        pos1=pos1+1
        count=1
    elif count==1:
        if pos2>len2:
            count=2

        else:
            Plist.append(L2[pos2])
            pos2=pos2+1
            count=2
    elif count==2:
        if pos3>len3:
            count=0

        else:
            Plist.append(L3[pos3])
            pos3=pos3+1
            count=0




Ptext = ''.join(Plist)


print("The plaintext is " + Ptext)







