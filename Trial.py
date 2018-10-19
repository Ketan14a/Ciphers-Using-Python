def gcd(a,b):
    if(b==0):
        return a
    else:
        return gcd(b,a%b)





Ans = gcd(27,64)
print(Ans)