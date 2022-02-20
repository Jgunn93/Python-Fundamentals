class User:
    def __init__(self, name, pin, password):
        self.name = name
        self.pin = pin
        self.password = password
    def change_name(self, name):
        self.name = name
    def change_pin(self, pin):
        self.pin = pin
    def change_password(self,password):
        self.password = password

class BankUser(User):
    def __init__(self, name, pin, password):
        super().__init__(name, pin, password)
        self.balance = 0
    def show_balance(self):
        print(self.name,"has an account balance of: $", float(self.balance))
    def withdraw(self,withdraw):
        self.balance -= withdraw
    def deposit(self,deposit):
        self.balance += deposit
    def transfer_money(self,user,amount):
        print("You are transferring $",amount,"to",user.name)
        print("Authentication required")
        correct_pin = int(input("Enter your PIN:"))
        if self.pin == correct_pin:
            print("Transfer Authorized")
            print("Transferring $",amount,"to",user.name)
            self.balance -= amount
            user.balance += amount
            return True
        else:
            print("Invalid PIN. Transaction cancelled.")
            return False

    def request_money(self,user,amount):
        print("You are requesting $",amount,"from",user.name)
        print("User authentication is required...")
        correct_pin = int(input("Enter your PIN: "))
        if correct_pin == user.pin:
            password = input("Enter your password: ")
            if password == self.password:
                print("Request Authorized")
                print(user.name,"sent $",amount)
                self.balance += amount
                user.balance -= amount
                return True
            else:
                print("Invalid password. Transaction cancelled.")
                return False
        else:
            print("Invalid PIN. Transaction cancelled.")
            return False

'''Drive Code for Task 1

user1 = User("Bob", 1234, "password")
print(user1.name, user1.pin, user1.password)

Driver Code for Task 2 

user2 = User("Bob",1234,"password")
print(user2.name,user2.pin,user2.password)
user2.change_name("Bobby")
user2.change_pin(4321)
user2.change_password("newpassword")
print(user2.name,user2.pin,user2.password)

Driver Code for Task 3

user3 = BankUser("Bob",1234,"password")
print(user3.name,user3.pin,user3.password,user3.balance)

Driver Code for Task 4

user3 = BankUser("Bob",1234,"password")
user3.show_balance()
user3.deposit(1000)
user3.show_balance()
user3.withdraw(500)
user3.show_balance()

Driver Code for Task 5'''

user3 = BankUser("Bob",1234,"password")
user4 = BankUser("Alice",5678,"alicepassword")
user4.deposit(5000)
user4.show_balance()
user3.show_balance()
transfer_flag= user4.transfer_money(user3,500)
user4.show_balance()
user3.show_balance()
if transfer_flag:
    user4.request_money(user3,250)
    user4.show_balance()
    user3.show_balance()