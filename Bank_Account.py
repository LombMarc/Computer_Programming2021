class Account:
    def __init__(self,name:str,pin:str,amount:float):
        self.name=name
        self.pin=pin
        self.amount=amount
        self.account= [name,pin,amount]



def init_bank(N):
    BANK=[Account("Admin","Admin",0).account]
    for i in range(N):
        name = input("Add name: ")
        pin = input("insert Pin: ")
        amount = float(input("Insert amount: "))
        bank=Account(name,pin,amount)
        BANK.append(bank.account)
    return BANK

#BANK=addAccount(3)

BANK=[['Marco', '123', 10000.0], ['Mauro', '456', 15000.0], ['Pippo', '789', 30000.0]]
#BANK ={"name":["admin"],"pin":["admin"],       "amount":[0]}

def Add_Account_dict():
    i=0
    while i==0:
        if input("Add account [y/n]? ")=="y":
            BANK["name"].append(input("Add name: "))
            BANK["pin"].append(input("Add pin: "))
            BANK["amount"].append(float(input("Insert amount: ")))
        else:
            i=1

def add_account():
    name=input("Name: ")
    pin=input("Pin: ")
    amount=float(input("Amount: "))
    temp=Account(name,pin,amount)
    return temp.account

def atm():
    name = input("Insert name: ")
    paswd=""
    if name=="Admin" and input("Password: ") == "Admin":
        inp=input("Management Interface. \n 1 to add account\n 2 to navigate accounts\n")
        i=0
        while i==0:
            if inp=="1":
                add_account()
                add=input("Add another account? [y/n]")
                if add=="y":
                    pass
                else:
                    i=1
            if inp=="2":
                print(BANK)
                i=1
        print("Closing ATM...")
        print("Restart")
        return atm()
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
