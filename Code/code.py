import time

print("Welcome to the Inventory Counter!")
time.sleep(1.5)
print("Please enter your username.")



name = input()
username = 'Employee'
username2 ='Customer'



if name == (username):
    print('Please wait...')
    time.sleep(1)
    print('')
    password = input('Correct, please enter your password:\n')   
    
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
    
         

    else:
        print("Incorrect Password...Goodbye")
        exit


elif name == (username2):
    print('Please wait...')
    time.sleep(1)
    print('')
    print('Welcome '+username2)
    print ("Press 2: To check stock. ")
    print ("Press q: To quit the program. ")

else:
    print('Please wait')
    time.sleep(1)
    print('')
    print('Unauthorized personnel, please enjoy looking through our products!')
    time.sleep(1)
    exit

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
    pants_stock = [10, 10, 20, 6]
    hats_stock = [5, 15, 10, 9]
    add_to = input("What item are you restocking?")
    up_add = add_to.upper()
   
    if up_add=="S":
        def menu():
            print ("Press S: Small Shirt.")
            print ("Press M: Medium Shirt.")
            print ("Press L: Large Shirt.")
            print ("Press XL: xLarge Shirt.")
            print("Press q: To quit the program.")
        run=menu()    
        wht_size1=input("What size shirt would you like to restock: ")
        wht_size = wht_size1.upper()
        if wht_size=='S':     
            amount= int(input("How many shirts would you like to add?:" ))
            shirts_stock[0]= shirts_stock[0] + amount
            print("Your updated inventory is",shirts_stock[0])
        elif wht_size=='M':
            amount= int(input("How many shirts would you like to add?:" ))
            shirts_stock[1]= shirts_stock[1] + amount
            print("Your updated inventory is",shirts_stock[1])
        elif wht_size=='L':
            amount= int(input("How many shirts would you like to add?:" ))
            shirts_stock[2]= shirts_stock[2] + amount
            print("Your updated inventory is",shirts_stock[2])
        elif wht_size=='XL':
            amount= int(input("How many shirts would you like to add?:" ))
            shirts_stock[3]= shirts_stock[3] + amount
            print("Your updated inventory is",shirts_stock[3])
        else:
            print("Invalid Input!")
            exit
            
    elif up_add=="P":
        def menu():
            print ("Press S: Small Pants.")
            print ("Press M: Medium Pants.")
            print ("Press L: Large Pants.")
            print ("Press XL: xLarge Pants")
            print("Press q: To quit the program.")
        run=menu()    
        wht_size1=input("What size pants would you like to restock: ")
        wht_size = wht_size1.upper()
        if wht_size=='S':     
            amount= int(input("How many pants would you like to add?:" ))
            pants_stock[0]= pants_stock[0] + amount
            print("Your updated inventory is",pants_stock[0])
        elif wht_size=='M':
            amount= int(input("How many pants would you like to add?:" ))
            pants_stock[1]= pants_stock[1] + amount
            print("Your updated inventory is",pants_stock[1])
        elif wht_size=='L':
            amount= int(input("How many pants would you like to add?:" ))
            pants_stock[2]= pants_stock[2] + amount
            print("Your updated inventory is",pants_stock[2])
        elif wht_size=='XL':
            amount= int(input("How many pants would you like to add?:" ))
            pants_stock[3]= pants_stock[3] + amount
            print("Your updated inventory is",pants_stock[3])
    elif up_add =="H":
        def menu():
            print ("Press R: Red Hats.")
            print ("Press B: Black Hats.")
            print ("Press O: Orange Hats.")
            print ("Press W: White Hats.")
            print("Press q: To quit the program.")
        run=menu()    
        wht_color1=input("What color would you like to restock: ")
        wht_color = wht_color1.upper()
        if wht_color=='R':     
            amount= int(input("How many hats would you like to add?:" ))
            hats_stock[0]= hats_stock[0] + amount
            print("Your updated inventory is",hats_stock[0])
        elif wht_color=='B':
            amount= int(input("How many hats would you like to add?:" ))
            hats_stock[1]= hats_stock[1] + amount
            print("Your updated inventory is",hats_stock[1])
        elif wht_color=='O':
            amount= int(input("How many hats would you like to add?:" ))
            hats_stock[2]= hats_stock[2] + amount
            print("Your updated inventory is",hats_stock[2])
        elif wht_color=='W':
            amount= int(input("How many hats would you like to add?:" ))
            hats_stock[3]= hats_stock[3] + amount
            print("Your updated inventory is",hats_stock[3])
    elif up_add == "Q":
        print ("Quitting the program...Goodbye")
        exit 
    else:
        print("Invalid Input!")
        exit

elif choice=='2':
    print ("Check stock has been selected: ")
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
    print ("Remove stock has been selected:")
    def menu():
        print ("Press S: Remove inventory from Shirts.")
        print ("Press P: Remove inventory from Pants.")
        print ("Press H: Remove inventory from Hats.")
        print("Press q: To quit the program.")
        

    run = menu()
    shirts_stock = [10, 12, 15, 5]
    pants_stock = [10, 10, 20, 6]
    hats_stock = [5, 0, 10, 9]
    add_to = input("What item are you removing?")
    up_add = add_to.upper()
   
    if up_add=="S":
        def menu():
            print ("Press S: Small Shirt.")
            print ("Press M: Medium Shirt.")
            print ("Press L: Large Shirt.")
            print ("Press XL: xLarge Shirt.")
            print("Press q: To quit the program.")
        run=menu()    
        wht_size1=input("What size shirt would you like to remove: ")
        wht_size = wht_size1.upper()
        if wht_size=='S':     
            amount= int(input("How many shirts would you like to remove?:" ))
            shirts_stock[0]= shirts_stock[0] - amount
            print("Your updated inventory is",shirts_stock[0])
        elif wht_size=='M':
            amount= int(input("How many shirts would you like to remove?:" ))
            shirts_stock[1]= shirts_stock[1] - amount
            print("Your updated inventory is",shirts_stock[1])
        elif wht_size=='L':
            amount= int(input("How many shirts would you like to remove?:" ))
            shirts_stock[2]= shirts_stock[2] - amount
            print("Your updated inventory is",shirts_stock[2])
        elif wht_size=='XL':
            amount= int(input("How many shirts would you like to remove?:" ))
            shirts_stock[3]= shirts_stock[3] - amount
            print("Your updated inventory is",shirts_stock[3])
        else:
            print("Invalid Input!")
            exit
            
    elif up_add=="P":
        def menu():
            print ("Press S: Small Pants.")
            print ("Press M: Medium Pants.")
            print ("Press L: Large Pants.")
            print ("Press XL: xLarge Pants")
            print("Press q: To quit the program.")
        run=menu()    
        wht_size1=input("What size pants would you like to remove: ")
        wht_size = wht_size1.upper()
        if wht_size=='S':     
            amount= int(input("How many pants would you like to remove?:" ))
            pants_stock[0]= pants_stock[0] - amount
            print("Your updated inventory is",pants_stock[0])
        elif wht_size=='M':
            amount= int(input("How many pants would you like to remove?:" ))
            pants_stock[1]= pants_stock[1] - amount
            print("Your updated inventory is",pants_stock[1])
        elif wht_size=='L':
            amount= int(input("How many pants would you like to remove?:" ))
            pants_stock[2]= pants_stock[2] - amount
            print("Your updated inventory is",pants_stock[2])
        elif wht_size=='XL':
            amount= int(input("How many pants would you like to remove?:" ))
            pants_stock[3]= pants_stock[3] - amount
            print("Your updated inventory is",pants_stock[3])
    elif up_add =="H":
        def menu():
            print ("Press R: Red Hats.")
            print ("Press B: Black Hats.")
            print ("Press O: Orange Hats.")
            print ("Press W: White Hats.")
            print("Press q: To quit the program.")
        run=menu()    
        wht_color1=input("What color would you like to remove: ")
        wht_color = wht_color1.upper()
        if wht_color=='R':     
            amount= int(input("How many hats would you like to remove?:" ))
            hats_stock[0]= hats_stock[0] + amount
            print("Your updated inventory is",hats_stock[0])
        elif wht_size=='B':
            amount= int(input("How many hats would you like to remove?:" ))
            hats_stock[1]= hats_stock[1] + amount
            print("Your updated inventory is",hats_stock[1])
        elif wht_size=='O':
            amount= int(input("How many hats would you like to remove?:" ))
            hats_stock[2]= hats_stock[2] + amount
            print("Your updated inventory is",hats_stock[2])
        elif wht_size=='W':
            amount= int(input("How many hats would you like to remove?:" ))
            hats_stock[3]= hats_stock[3] + amount
            print("Your updated inventory is",hats_stock[3])
    elif up_add == "Q":
        print ("Quitting the program...Goodbye")
        exit 
    else:
        print("Invalid Input!")
        exit
elif choice=='q':
    print ("Quitting the program...Goodbye")
    exit 
else:
    print("Invalid Input!")
    exit

    

