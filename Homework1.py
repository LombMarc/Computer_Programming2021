import math

def convert(tri: list):
	days= tri[0]*365+tri[1]*7+tri[2]
	hours= days*24
	minutes= hours*60
	seconds= mintues *60
	return days, hours, minutes, seconds

def pythagoras(l1,l2):
	hyp=((l1**2)+(l2**2))**0.5
	return hyp

def circ(D: float):
	l=D/(2**0.5)	
	r=l*2
	rr=pow(r,2)
	A= rr*math.pi
	return A

def convert(N):
        hours=N*24
        seconds=hours*60*60
        print(N," in hours: ", hours)
        print(N," in seconds: ", seconds)


def trigon(d):
        print(math.sin(math.radians(d)))
        print(math.cos(math.radians(d)))
        print(math.tan(math.radians(d)))


def y2s(Y):
        print(Y*365*24*60*60)

def hello(name):
        print("Hello ", name)
        print("How are you")

def pizza(C,d):
        r=d/2
        A=(r**2)*math.pi
        price=C/A
        return price
print(pizza(11,0.33))
