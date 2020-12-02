import time

print("Welcome to the Inventory Counter!")
time.sleep(1.5)
print("Please enter your username.")



name = input()

username = 'Employee'
username2 = 'Shopper'

if name == (username):
    print('Please wait...')
    time.sleep(1)
    print('')
    print('Correct, please enter your password.')    
    
password = input()

password1 = 'Admin'

if password == (password1):
    print('Please wait...')
    time.sleep(1)
    print('')
    print('Correct, logging in.')
    time.sleep(1)
    print('Welcome '+username)    
    print ("Press 1: To add stock. ")
    print ("Press 2: To check stock. ")
    print ("Press 3: To remove stock. ")
    print ("Press q: To quit the program. ")
    
    
    

if name != (username):
    print('Please wait')
    time.sleep(1)
    print('')
    print('Unauthorized personnel, please enjoy looking through our products!')
    time.sleep(1)
    exit

if name == (username2):
    print('Please wait...')
    time.sleep(1)
    print('')

choice = input("What would you like to do? ")
     
if choice=='1':     
    print ("Add stock has been selected:")
    def menu():
        print ("Press S: Add inventory to Shirts.")
        print ("Press P: Add inventory to Pants.")
        print ("Press H: Add inventory to Hats.")
        print("Press q: To quit the program.")
        

    run = menu()
    shirts_stock = [10, 12, 15, 5]
    pants_stock = {'small':10, 'medium':10, 'large':20, 'xlarge':6}
    hats_stock = {'red':5, 'orange':0, 'yellow':2, 'black':10, 'white':9}
    add_to = input("What item are you restocking?")
    up_add = add_to.upper()
   
    if up_add=="S":
        def menu():
            print ("Press S: Small Shirt.")
            print ("Press M: Medium Shirt.")
            print ("Press L: Large Shirt.")
            print ("Press XL: xLarge Shirt.")
            print("Press q: To quit the program.")
            
        wht_size1=input("What size shirt would you like to restock: ")
        wht_size = wht_size1.upper()
        if wht_size=='S':     
            amount= int(input("How many shirts woould you like to add?:" ))
            shirts_stock[0]= shirts_stock[0] + amount
            print("Your updated inventory is",shirts_stock[0])
        elif wht_size=='M':
            amount= int(input("How many shirts woould you like to add?:" ))
            shirts_stock[1]= shirts_stock[1] + amount
            print("Your updated inventory is",shirts_stock[1])
        elif wht_size=='L':
            amount= int(input("How many shirts woould you like to add?:" ))
            shirts_stock[2]= shirts_stock[2] + amount
            print("Your updated inventory is",shirts_stock[2])
        elif wht_size=='XL':
            amount= int(input("How many shirts woould you like to add?:" ))
            shirts_stock[3]= shirts_stock[3] + amount
            print("Your updated inventory is",shirts_stock[3])
        else:
            print("Invalid Input!")
            exit
            
    elif up_add=="P":
        def menu():
            print ("Press S: Small Shirt.")
            print ("Press M: Medium Shirt.")
            print ("Press L: Large Shirt.")
            print ("Press XL: xLarge Shirt.")
            print("Press q: To quit the program.")
            
        wht_size=input("What size shirt would you like to restock: ")
        if wht_size=='S':     
            amount= int(input("How many shirts woould you like to add?:" ))
            
        elif wht_size=='M':
            print ("Menu 2 has been selected")
            ## You can add your code or functions here
        elif wht_size=='L':
            print ("Menu 3 has been selected")
            ## You can add your code or functions here
        elif wht_size=='XL':
            print ("Menu 4 has been selected")
            ## You can add your code or functions here
    elif up_add =="H":
        def menu():
            print ("Press S: Small Shirt.")
            print ("Press M: Medium Shirt.")
            print ("Press L: Large Shirt.")
            print ("Press XL: xLarge Shirt.")
            print("Press q: To quit the program.")
            
        wht_size=input("What size shirt would you like to restock: ")
        if wht_size=='S':     
            amount= int(input("How many shirts woould you like to add?:" ))
            shirts_stock[wht_size] += amount
        elif wht_size=='M':
            print ("Menu 2 has been selected")
            ## You can add your code or functions here
        elif wht_size=='L':
            print ("Menu 3 has been selected")
            ## You can add your code or functions here
        elif wht_size=='XL':
            print ("Menu 4 has been selected")
            ## You can add your code or functions here
    elif up_add == "Q":
        print ("Quitting the program...Goodbye")
        exit 
    else:
        print("Invalid Input!")
        exit

elif choice=='2':
    print ("check stock has been selected: ")
    def menu():
        print ("Press S: Check inventory of Shirts.")
        print ("Press P: Check inventory of Pants.")
        print ("Press H: Check inventory of Hats.")
        print("Press q: To quit the program.")
        

    run = menu()
    shirts_stock2 = ("small:10, medium:10, large:15, xlarge:5")
    pants_stock2 = ("small:10, medium:10, large:20, xlarge:6")
    hats_stock2 = ("red:5, orange:0, yellow:2, black:10, white:9")
    entry=input("What would you like to do? ")
    cap_entry = entry.upper()

    if cap_entry=="S":
            print(shirts_stock2)
    elif cap_entry =="P":
            print(pants_stock2)
    elif cap_entry =="H":
            print(hats_stock2)
    elif cap_entry == "Q":
            print ("Quitting the program...Goodbye")
            exit 
    else:
            print("Invalid Input!")
            exit
elif choice=='3':
    print ("remove stock has been selected")
        ## add remove stock functions here
elif choice=='q':
    print ("Quitting the program...Goodbye")
    exit 
else:
    print("Invalid Input!")
    exit

    

