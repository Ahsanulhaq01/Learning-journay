class Atm:
    def __init__(self):
        balance = 0
        pin = ''
        Atm.menu()


    def menu():
        print(f"Enter the Following Number according to your concern Operation ")
        print("Enter 1 to Create Pin");
        print("Enter 2 to Deposit Balance")
        print("Enter 3 to Withdraw Balance")
        print("Enter 4 to Check Balance")
        print("Enter 5 to exit the Operations")
        num = int(input("Enter the number : "))
        if(num ==1):
            Atm.create_pin()
        elif(num ==2):
            Atm.deposit_balance()
        elif(num == 3):
            Atm.withdraw()
        elif(num == 4):
            Atm.checkbalance()
        else:
            print("Operation Terminated Successfully ! ")
    
    def create_pin():
        enterpin = int(input("Enter You Pin "))
        Atm.pin = enterpin
        print("Pin Successfully Created ")
        Atm.menu()

    def deposit_balance():
        if(Atm.pin == Atm.checkPass()):
            Atm.balance = int(input("Enter the amount to deposit "))
            print("deposit Successful !")
        else:
            print("Incorrect Password !")
        Atm.menu()   
    
    def withdraw():
        if(Atm.pin == Atm.checkPass()):
            amount= int(input("Enter the amount to withdraw"))
            if(amount<Atm.balance):
                Atm.balance -= amount
                print("Amount Successfully Withdraw")
            else:
                print("Unsufficent Balance !")
        else:
            print("Incorrect Password !")
        Atm.menu()
    def checkbalance():
        if(Atm.pin == Atm.checkPass()):
            print(f"The amount of balance is : {Atm.balance}")
        else:
            print("Incorrect Password !")
        Atm.menu()
    def checkPass():
        pass1 = int(input("Enter Password to continue Operatoin"))
        return pass1
    

ahsan = Atm()