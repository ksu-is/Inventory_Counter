import time

print("Welcome to the Inventory Counter!")
time.sleep(1.5)
print("Please enter your username.")

shirts_stock = {'small':10, 'medium':10, 'large':15, 'xlarge':5}
pants_stock = {'small':10, 'medium':10, 'large':20, 'xlarge':6}
hats_stock = {'red':5, 'orange':0, 'yellow':2, 'black':10, 'white':9}

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
    input ("What would you like to do? ")

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

#add next step
def menu():
    print ("Press S: Check inventory of Shirts.")
    print ("Press P: Check inventory of Pants.")
    print ("Press H: Check inventory of Hats.")
    print("Press q: To quit the program.")
   

run = menu()
shirts_stock = ("small:10, medium:10, large:15, xlarge:5")
pants_stock = ("small:10, medium:10, large:20, xlarge:6")
hats_stock = ("red:5, orange:0, yellow:2, black:10, white:9")
entry=input("What would you like to do? ")
cap_entry = entry.upper()

if cap_entry=="S":
    print(shirts_stock)
elif cap_entryy =="P":
    print(pants_stock)
elif cap_entry =="H":
    print(hats_stock)
elif cap_entry == "q":
    quit
else:
    print("Invalid Input!")