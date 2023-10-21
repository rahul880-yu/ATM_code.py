class ATM:
    def __init__(self):
        self.pin = ""
        self.balance = 1000
        self.menu()

    def menu(self):
        user_input = input("""
                    Hello, how would you like to proceed?
                    1.Enter 1 to create pin
                    2.Enter 2 to deposit
                    3.Enter 3 to withdraw
                    4.Enter 4 to check balance 
                    5.Enter 5 to exit
""")
        if user_input == "1":
            self.p_pin()
        elif user_input == "2":
            self.d_deposit()
        elif user_input == "3":
            self.w_withdraw()
        elif user_input == "4":
            self.b_balance()
        elif user_input == "5":
            self.e_exit()
        else:
            print("Please visit next time")

    def p_pin(self):
        self.pin = int(input("Please enter a pin here: "))
        print("your pin is sucessfully created")

    def d_deposit(self):
        temp = int(input("Enter your pin: "))
        if temp == self.pin:
            amount = int(input("Deposit your amount: "))
            self.balance = self.balance + amount
            print("Deposit successful")

    def w_withdraw(self):
        temp = int(input("Enter your pin: "))
        if temp == self.pin:
            amount = int(input("Enter your withdraw amount: "))
            if amount < self.balance:
                self.balance = self.balance-amount
                print("successful")
            else:
                print("insufficent pin")
        else:
            print('invalid pin')

    def b_balance(self):
        temp = int(input("Enter your pin: "))
        if temp == self.pin:
            print(self.balance)
        else:
            print("invalid pin")

    def e_exit(self):
        temp = int(input("Enter your pin"))
        if temp == self.pin:
            print("sucessfully exit")
        else:
            print("not exit")

a = ATM()

