import math
from Homework1 import pythagoras
def fact_sum(N):
    Sig=[]
    for n in range(1,N+1):
        Sig.append(math.factorial(n))
    return sum(Sig)

def point_distance(x1,y1,x2,y2):
    return math.sqrt(pow(x2-x1,2)+pow(y2-y1,2))
    
def Grt_Crc(c1,c2,x1,y1,x2,y2):
    m1=point_distance(c1,c2,x1,y1)
    m2=point_distance(c1,c2,x2,y2)
    return 2*max(m1,m2)*math.pi

def semifactorial(n):
    nii=[]
    if n%2==0:
        for i in range(2,n+1):
            if i%2==0:
                nii.append(i)
    elif n%2 ==1:
        for i in range(3,n+1):
            if i%2==1:
                nii.append(i)
    sf=1
    for j in nii:
        sf=sf*j
    return sf
#print(semifactorial(7))
