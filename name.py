def pgcd(a,b):
    if b==0:
        return a
    else:
        return  a,b= b,pgcd(a%b)
print(pgcd(48,18))