import random
from math import factorial

liczby=input().split()
n=int(liczby[0])
k=int(liczby[1])

def Newton(n,k):
        if k == 0 or k == n:
            return 1
        else:
            return (factorial(n)/(factorial(k)*factorial(n-k)))

print (Newton(n,k))
