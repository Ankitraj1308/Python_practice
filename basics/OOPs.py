class Atm:
    def __init__(self):
        print(id(self))
        self.pin = ""
        self.balance = 0
        #self.menu()
    def menu(self):
        user_input = int(input("""
        Hi how can I help you?
        1. Press 1 to create pin
        2. Press 2 to change pin
        3. Press 3 to check balance
        4. Press 4 to withdraw
        5. anythis else to exit
        """))

        if user_input==1:
            #creatPin
            self.Create_Pin()
        elif user_input==2:
            #change pin
            self.Change_Pin()
        elif user_input==3:
            #check balance
            self.Check_Balance()
        elif user_input==4:
            #witdraw
            self.Withdraw()
        else:
            exit()

    def Create_Pin(self):
        user_pin = int(input("enter your pin: "))
        self.pin = user_pin

        user_balnce = int(input("enter your balance: "))
        self.balance = user_balnce

        print("pin created sucessfuly")
        self.menu()

    def Change_Pin(self):
        check = int(input("enter your last pin: "))

        if(self.pin==check):
            new_pin = int(input("enter new pin: "))
            self.pin = new_pin
        else:
            print("can't change the pin !!")

        self.menu()

    def Check_Balance(self):
        user_pin = int(input("enter your current pin: "))

        if(user_pin==self.pin):
            print("your current balance: ",self,self.balance)
        else:
            print("Wrong Pin!!")

    def Withdraw(self):
        user_pin = int(input("enter your pin: "))

        if(user_pin == self.pin):
            amount = int(input("Enter the amount to withdraw: "))
            if(amount<=self.balance):
                self.balance -= amount
                print("Withdrawl Sucessful. balance: ",self.balance)
            else:
                print("Insufficient Bslsnce")
        else:
            print("Wrong pin!!")

class main:
    obj = Atm()
    obj2 = Atm()
    