def gcd(a,b):
    if(b==0):
        return a
    else:
        return gcd(b,a%b)


Pnum = int(input("Enter the plain text number:"))
P1 = int(input("Enter first prime number:"))
P2 = int(input("Enter second prime number:"))

n = P1 * P2
phi = (P1-1) * (P2-1)

for i in range(2,phi):
    if(gcd(i,phi)==1):
        e = i
        break
    else:
        continue

sum = 1
while(True):
    sum = sum + phi
    if(sum%e==0):
        d = sum/e
        break
    else:
        continue



Cnum = (Pnum**e) % n
print("The generated Cipher text number is " + str(Cnum))

Pnum = (Cnum**d) % n
print("The decrypted Plain Text at receiver side is " + str(Pnum))




