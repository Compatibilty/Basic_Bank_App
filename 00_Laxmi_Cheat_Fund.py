from time import sleep

# Bank Base
class BankAccount:
    '''
    ========================\n
    Welcome to Laxmi Cheat Fund Bank
    1. Create New Account 
    2. Login to Your Account
    3. Check Balance
    4. Exit
    '''
    def __init__(self, user_name, balance = 0):
        self.user_name = user_name
        self.balance = balance

    def withdraw(self, amount):
        self.amount = amount
        if self.amount > self.balance: print("❌ Insufficient Balance!")
        else: 
            self.balance -= self.amount 
            print(f"✅ Withdrawn ₹{self.amount}")
        return self.balance
    
    def deposite(self, d_amount):
        self.d_amount = d_amount
        if self.d_amount > 0: 
            self.balance += self.d_amount
            print(f"✅ Withdrawn ₹{self.d_amount}")
        else:
            print("❌ Invalid deposit amount!")
        return self.balance


# Saving Account Code
class savingAccount(BankAccount):
    def __init__(self, user_name, balance, s_interest=0.05):
        super().__init__(user_name, balance)
        self.interest = s_interest

    def add_interest(self):
        interest_amt = self.balance * self.interest
        self.deposite(interest_amt)
        print(f"💰 Interest Added: ₹{interest_amt:.2f}")


# Currrent Account Code
class currentAccount(BankAccount):
    def __init__(self, user_name, balance, interest=0.1):
        super().__init__(user_name, balance)
        self.interest = interest

    def add_interest(self):
        interest_amt = self.balance * self.interest
        self.deposite(interest_amt)
        print(f"💰 Interest Added: ₹{interest_amt:.2f}")


# New Account Page
class newAcc(BankAccount):
    def __init__(self, user_name, balance=0):
        super().__init__(user_name, balance)


#===========================================
while True:
    try:
        print(BankAccount.__doc__)
        user_data = int(input("Selet your option: "))
        # Option 1 (Create New Account) 
        if user_data == 1:
            name = input("Enter User Name: ").lower()
            first_amount = float(input("Deposit First Amount: "))
            acc_type = input("Enter Account type (Current/Saving): ").lower()
            new_user = newAcc(name, first_amount)
            print("\n✅ Account Created Successfully!")
            print(f"👤 Name: {new_user.user_name}")
            print(f"👤 Account Type: {acc_type}")
            print(f"💰 Balance: ₹{new_user.balance}\n")
            sleep(2)

        # Option 2 (Login to Your Account) 
        elif user_data == 2:
            user_name = input("Enter the User Name: ").lower()
            print("1. Saving Account \n""2. Current Account")
            acc_detail = int(input("Select your Account type: "))
            # Saving Account
            if (acc_detail == 1) and (acc_type == acc_type) and (user_name == name):
                print("Saving Account \n" 
                "1. Withdraw Amount \n" 
                "2. Deposite Amount ")
                acc_detail_data = int(input("Enter the Data: "))
                if acc_detail_data == 1:
                    print("Withdraw Amount")
                    amt = float(input("Enter the Amount: ₹"))
                    new_user.withdraw(amt)
                elif acc_detail_data == 2:
                    print("Deposite Amount")
                    amt = float(input("Enter the Amount: ₹"))
                    new_user.deposite(amt)
                else: print("❌ Invalide data, Enter the correct data || TRY AGAIN!!") 
                sleep(1)

            # Current Account
            elif  (acc_detail == 1) and (acc_type == acc_type) and (user_name == name):
                print("Current Account \n" \
                "1. Withdraw Amount \n" \
                "2. Deposite Amount ")
                acc_detail_data = int(input("Enter the Data: "))
                if acc_detail_data == 1:
                    print("Withdraw Amount")
                    amt = float(input("Enter the Amount: ₹"))
                    new_user.withdraw(amt)
                elif acc_detail_data == 2:
                    print("Deposite Amount")
                    amt = float(input("Enter the Amount: ₹"))
                    new_user.deposite(amt)
                else: print("❌ Invalide data, Enter the correct data") 
                sleep(1)
            
            # Login Error
            else: print("❌ Invalide data, Enter the correct data") 
            sleep(1)

        # Option 3 (Check Balance) 
        elif user_data == 3:
            login = input("Enter User Name: ")
            if login == name:
                print(f"Account Holder: {name} \n Balance: ₹{new_user.balance}")
                sleep(1)
            else: print("❌ Invalide data, Enter the correct User Name") 
            sleep(1)

        # Option 4 (Exit)  
        elif user_data == 4:
            print("👋 Thank you! for using our service")
            sleep(1)
            break

        # Error
        else: print("❌ Invalide data, Enter the correct data") 
        sleep(1)
    
    except:
        print("Input Error!!!")
        sleep(1)