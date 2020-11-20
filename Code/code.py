import time

print("Welcome to the Inventory Counter!")
time.sleep(1.5)
print("Please enter your username.")

shirts_stock = {'small':10, 'medium':10, 'large':15, 'xlarge':5}
pants_stock = {'small':10, 'medium':10, 'large':15, 'xlarge':5}
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
def menu():
    print('Welcome, what are you shopping for today?')
    print ("Press 1: Check inventory of Shirts.")
    print ("Press 2: Check inventory of Pants.")
    print ("Press 3: Check inventory of Hats.")
    print("Press q: To quit the program.")
    return input ("What would you like to do? ")

run = menu()

while True:
    if run == "1":
        s_size = input('What size shirt are you looking for?')
    def menu():
        print("Press S: Small")
        print("Press M: Medium")
        print("Press L: Large")
        print("Press XL: Xlarge")
        run = menu()
      


