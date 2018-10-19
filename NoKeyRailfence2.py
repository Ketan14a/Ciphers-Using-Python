Ptext = input("Enter your plaintext:")
NLists = int(Ptext.__len__()/3)
Plist = list(Ptext)
Plen = Ptext.__len__()

L=[]
EvenL = []

for i in range(NLists):
    L.append([])

count=0

for i in Plist:
    if count!=0:
        EvenL.append(i)
        Plist.remove(i)
        count=0
    else:
        count=1





print(Plist)
print(EvenL)



