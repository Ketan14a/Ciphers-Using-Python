key = input("Enter key:")
mylist = list(key)

index=0
count=0
for i in mylist:

    for j in mylist:
        if i==j and index!=count:
            mylist.pop(count)

        count+=1


    index+=1
    count=0



matrix = []

for i in range(5):
    matrix.append([])


count=0
index=0
flag=0
for i in mylist:
    matrix[index].append(i)
    count+=1
    if count==5:
        count=0
        index+=1


for i in range(26):
    alpha = chr(97+i)
    if alpha=='j':
        continue
    for j in mylist:
        if alpha==j:
            flag=1


    if flag!=1:
        matrix[index].append(alpha)

        count+= 1
        if count == 5:
            count=0
            index+=1
    flag=0


for i in matrix:
    print(i)





if 1==1:

    Ptext = input("Enter your plaintext:")
    Ctext=""
    r1=r2=c1=c2=0
    flag=0


    for i in range(0,Ptext.__len__(),2):
        char1 = Ptext[i]
        if i+1<Ptext.__len__():
          char2 = Ptext[i+1]
        else:
            char2 = ""
            flag=1


        for j in range(5):
            for k in range(5):
                if matrix[j][k]==char1:
                    r1=j
                    c1=k
                if matrix[j][k]==char2 and  flag==0:
                    r2=j
                    c2=k



        #case-1] shape=column

        if c1==c2:
            if r1==4:
                r1=-1
            if r2==4:
                if flag==0:
                    r2=-1
            char1 = matrix[r1 + 1][c1]
            if flag==0:
              char2 = matrix[r2 + 1][c2]
            Ctext += char1
            Ctext += char2




        #case-2] shape = row
        elif r1==r2:
            if c1==4:
                c1=-1
            if c2==4 and flag==0:
                c2=-1

            char1=matrix[r1][c1+1]
            char2=matrix[r2][c2+1]
            Ctext+=char1
            if flag==0:
              Ctext+=char2



        #case-3] shape = rectangle
        else:
            char1=matrix[r1][c2]
            Ctext+=char1
            if flag==0:
              char2 = matrix[r2][c1]
              Ctext+=char2




    print("The ciphertext is ",Ctext)

    Ctext = input("Enter your ciphertext:")
    Ptext = ""
    r1 = r2 = c1 = c2 = 0
    flag = 0

    for i in range(0, Ctext.__len__(), 2):
        char1 = Ctext[i]
        if i + 1 < Ctext.__len__():
            char2 = Ctext[i + 1]
        else:
            char2 = ""
            flag = 1

        for j in range(5):
            for k in range(5):
                if matrix[j][k] == char1:
                    r1 = j
                    c1 = k
                if matrix[j][k] == char2 and flag == 0:
                    r2 = j
                    c2 = k

        # case-1] shape=column

        if c1 == c2:
            if r1 == 0:
                r1 = 5
            if r2 == 0:
                if flag == 0:
                    r2 = 5
            char1 = matrix[r1 - 1][c1]
            if flag == 0:
                char2 = matrix[r2 - 1][c2]
            Ptext += char1
            Ptext += char2




        # case-2] shape = row
        elif r1 == r2:
            if c1 == 0:
                c1 = 5
            if c2 == 0 and flag == 0:
                c2 = 5

            char1 = matrix[r1][c1 - 1]
            char2 = matrix[r2][c2 - 1]
            Ptext += char1
            if flag == 0:
                Ptext += char2



        # case-3] shape = rectangle
        else:
            char1 = matrix[r1][c2]
            Ptext += char1
            if flag == 0:
                char2 = matrix[r2][c1]
                Ptext += char2

    print("The plaintext is ", Ptext)
















