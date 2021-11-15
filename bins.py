def bins(num:int):
    b=[]
    while num!=0:
        bn= round(num%2)
        b.append(bn)
        num=num//2
    b.reverse()
    return b

print("Hello world")