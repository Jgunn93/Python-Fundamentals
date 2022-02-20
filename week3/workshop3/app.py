from donations_pkg.homepage import show_homepage
from donations_pkg.user import login
from donations_pkg.user import register
from donations_pkg.homepage import donate
from donations_pkg.homepage import show_donations

database = {'admin': 'password123'}
donations = []
authorized_user = ""

while True:
    show_homepage()

    if authorized_user == "":
        print("You must be logged in to donate.")
    else:
        print("Logged in as: ", authorized_user)

    menu_input = input("Choose an option: ")
    if menu_input == "1":
        username = input("\nEnter Username: ").lower()
        password = input("Enter Password: ")
        authorized_user = login(database, username, password)
    if menu_input == "2":
        username = input("Enter Username: ").lower()
        password = input("Enter Password: ")
        if len(password) > 4:
            authorized_user = register(database, username)
            if authorized_user != "":
                database[username] = password
        else:
            print("Password must be at least 5 characters!")
    if menu_input == "3":
        if authorized_user == "":
            print("You are not logged in.")
        else:
            donation = donate(authorized_user)
            donations.append(donation)
    if menu_input == "4":
        show_donations(donations)
    if menu_input == "5":
        print("")
        print("Leaving DonateMe...")
        break