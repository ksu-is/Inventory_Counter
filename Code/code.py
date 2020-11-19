#step 1: Greeting
print("Welcome to the Inventory Counter!")
#Step 2: Sign-in
user = input("Username: ")
pword = input("Password: ")
user_employee = ["Employee"]

if user in user_employee:
    password = ["store"]
    print(pword)
    if pword in password:
        print ("Press 1: To add stock. ")
        print ("Press 2: To check stock. ")
        print ("Press 3: To remove stock. ")
        print ("Press q: To quit the program. ")
        input ("What would you like to do? ")
else:
    print("Invalid username/password: ")


