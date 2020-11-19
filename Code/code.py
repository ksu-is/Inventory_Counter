#step 1
import time

print("Welcome to the Inventory Counter!")
time.sleep(1.5)
print("Please enter your username.")

name = input()

username = 'Employee'
username2 = 'Shopper'


if name == (username):
    print('Please wait')
    time.sleep(1)
    print('')
    print('Correct, please enter your password.')
    
if name == (username2):
    print('Please wait')
    time.sleep(1)
    print('')
    print('Welcome, what are you shopping for today?')
    print ("Press 1: Check inventory of Shirts.")
    print ("Press 2: Check inventory of Pants.")
    print ("Press 3: Check inventory of Hats.")
    print("Press q: To quit the program.")
    input ("What would you like to do? ")
        
password = input()

password1 = 'Admin'

if password == (password1):
    print('Please wait')
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
    print('Incorrect, closing program.')
    time.sleep(1)
    exit
