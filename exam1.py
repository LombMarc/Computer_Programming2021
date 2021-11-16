import math

engNum={
    0:"zero",1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine"
    }
list1=[1,0,3,6]
list2=[2,5,0,7]
def list2matrx(l1,l2):
    maxL=max(max(l1,l2))
    matrix=[]
    for i in l2:
        array=[]
        for j in l1:
            if i==0 and j==0:
                sc=engNum[maxL]
            else:
                sc=engNum[j]+"_"+engNum[i]
            array.append(sc)
        matrix.append(array)
    return matrix
mat=list2matrx(list1,list2) 

for ar in mat:
    print(ar)
