import math

class Bodymass:
    def __init__(self,weight,height):
        self.weight=weight
        self.height=height
    def BMI(self):
        return self.weight/pow(self.height,2.0)


try:
    w=float(input("Weight is: "))
    h=float(input("Height is: "))
except:
    print("Input must be a number")
person=Bodymass(w,h)
#print(person.weight)
#print(person.height)
print("Your BM index is: ",round(person.BMI(),2))
