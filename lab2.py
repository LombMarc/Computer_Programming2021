import math
from Homework1 import pythagoras

def graduate():
    cfu=int(input("Current CFU: "))
    min_cfu=120
    if cfu< min_cfu:
        print("Unfortunatly, you don't have enough credits")
    else:
        print("You can graduate")

def perimeter():
    inp=input("Is right angled(y/n): ")
    if inp=="y":
        L1=float(input("Lenght of first leg: "))
        L2=float(input("Lenght of second leg: "))
        L3=pythagoras(L1,L2)
        return L1+L2+L3
    else:
        L1=float(input("Lenght of one leg: "))
        return 3*L1

def A_sys(m,n):
    if m==0:
        return n+1
    elif m>0 and n==0:
        return A_sys(m-1,1)
    elif m>0 and n>0:
        return A_sys(m-1,A_sys(m,n-1))

def GCD(A,B):
    a=max(A,B)
    b=min(A,B)
    r=a%b
    if r==0:
        return b
    else:
        return GCD(b,r)

#print(GCD(33,56))

def int_Multiples(n,j):     #Find j multiples for n
    Multiples=[]
    for i in range(1,j+1):
        Multiples.append(n*i)
    return Multiples

def LCM(A,B):
    mA=int_Multiples(A,20)
    mB=int_Multiples(B,20)
    for i in mA:
        for j in mB:
            if i==j:
                return i
#print(LCM(4,6))
