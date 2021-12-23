#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 23 16:51:30 2021

@author: marcolombardi
"""

s1= "abcdefghil"
s2="pippopluto"

def merge(s1,s2):
    l=""
    if len(s1)!=len(s2):
        print("The string does not have same length")
    else:
        for i in range(len(s1)):
            l=l+s1[i]+s2[i]
    return l

#print(merge(s1,s2))

def exp(base,exponent):
    e=[]
    if len(base)>len(exponent):
        base=base[0:len(exponent)]
    if len(base) < len(exponent):
        exponent=exponent[0:len(base)]
    for i in range(len(base)):
        e.append(base[i]**exponent[i])
    return e

#print(exp([2,3,5,5,7],[2,0,9,2,3,4]))

def verify(L,N,R):
    c=0
    for i in L:
       if i==N:
           c+=1
    if c==R:
        return True
    else:
        return False

#print(verify([2,3,5,3],3,2))


class Account:
    def __init__(self,name:str,pin:str,amount:float):
        self.name=name
        self.pin=pin
        self.amount=amount
        self.account= [name,pin,amount]



def addAccount(N):
    BANK=[]
    for i in range(N):
        name = input("Add name: ")
        pin = input("insert Pin: ")
        amount = float(input("Insert amount: "))
        bank=Account(name,pin,amount)
        BANK.append(bank.account)
    return BANK

#BANK=addAccount(3)

BANK=[['Marco', '123', 10000.0], ['Mauro', '456', 15000.0], ['Pippo', '789', 30000.0]]
print(BANK)


def atm():
    name = input("Insert name: ")
    paswd=""
    for i in BANK:
        if i[0]==name:
            print("Hello, ", name)
            paswd = i[1]
            amount= i[2]
        else:
            pass
    if paswd=="":
        print("There is no account named ", name+".")
        return 0
    c = 0

    while  c < 3:
        
        if input("Insert password: ") != paswd:
            c += 1
            t = 3-c
            print("wrong password, " + str(t) +" remaining attempt")
            if c>=3:
                print("Max number of attempt reached")
        else:
            c=3
            withdraw = float(input("Hello " + name + ", what is the amount to withdraw? "))
            if withdraw<=amount:
                amount = amount-withdraw
                print("Done")
                print("Balance: ", amount)
            else:
                print("Transaction cancelled. ")



atm()













