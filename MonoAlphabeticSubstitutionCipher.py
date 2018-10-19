print("Press 1 if you are Admin")
print("Press 2 if you are another user")
choice = int(input("Enter your choice:"))


if choice==1:
    smallFile = open("smallAlpha.txt",mode='w',encoding='utf-8')
    capitalFile = open("capsAlpha.txt", mode='w', encoding='utf-8')
    print("Enter Substitution Letters for Small Alphabets:")

    for i in range(26):
        char = input("Enter for "+ chr(97+i)+":")
        smallFile.write(char)


    print("Enter Substitution Letters for Capital Alphabets:")

    for i in range(26):
        char = input("Enter for "+ chr(65+i)+":")
        capitalFile.write(char)



    print("All alphabets coded successfully!")
    smallFile.close()
    capitalFile.close()

elif choice==2:
    Sfile = open("smallAlpha.txt",mode='r',encoding='utf-8')
    Cfile = open("capsAlpha.txt",mode='r',encoding='utf-8')
    CList = []
    Slist = []

    for i in range(26):
        CList.append(Cfile.read(1))
        Slist.append(Sfile.read(1))



    #print(CList)
    #print(Slist)
    print("Press 1 for encrypting the Plaintext")
    print("Press 2 for decrypting the Ciphertext")
    choice=int(input("Enter your choice:"))

    if choice==1:
        Ctext = ""
        Ptext = input("Enter your plaintext:")

        for i in range(Ptext.__len__()):
            char = Ptext[i]

            if(char.isupper()):
                pos = ord(char)-65
                Ctext+=CList[pos]

            else:
                pos = ord(char)-97
                Ctext+=Slist[pos]



        print("The cipher text is ",Ctext)



    elif choice==2:
        Ptext=""
        Ctext = input("Enter your ciphertext:")


        for i in range(Ctext.__len__()):
            char = Ctext[i]

            if(char.isupper()):
                Cfile.seek(0)
                count=0
                read = Cfile.read(1)
                while char!=read:
                    count+=1
                    read = Cfile.read(1)

                Ptext+=chr(count+65)

            else:
                Sfile.seek(0)
                count=0
                read = Sfile.read(1)
                while char!=read:
                    count+=1
                    read = Sfile.read(1)

                Ptext+=chr(count+97)

        print("The Plaintext is ",Ptext)
        Sfile.close()
        Cfile.close()










