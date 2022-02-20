from banking_pkg import account

def atm_menu(name):
    print("")
    print("          === Automated Teller Machine ===          ")
    print("User: " + name)
    print("------------------------------------------")
    print("| 1.    Balance     | 2.    Deposit      |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Withdraw    | 4.    Logout       |")
    print("------------------------------------------")
print("          === Automated Teller Machine ===          ")
while True:
    name = input("Enter name to register: ")
    if len(name) >= 10:
        print("Name is too long, try to keep it short.")
        continue
    if len(name) <= 1:
        print("Please enter your name.")
        continue
    else:
        break
while True:
    pin = input("Enter PIN: ")
    if len(pin) != 4:
        print("Pin length must be 4 digits long")
        continue
    else:
        break
balance = 0
print(name + " has been registered with a starting balance of $" + str(balance))
print("")

while True:
    name_to_validate = input("Enter name: ")
    pin_to_validate = input("Enter PIN: ")
    if name_to_validate == name and pin_to_validate == pin:
        print("Login successful!")
        break
    else:
        print("Invalid credentials!")
while True:
    atm_menu(name)
    option = input("Choose an option: ")
    if option == "1":
        account.show_balance(balance)
    elif option == "2":
        balance = account.deposit(balance)
        account.show_balance(balance)
    elif option == "3":
        balance = account.withdraw(balance)
        account.show_balance(balance)
    elif option =="4":
        account.logout(name)
        break
    else:
        print("Please select a valid option")