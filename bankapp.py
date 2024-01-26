usersData = {}
import pwinput as pw
import getpass

def land():
    print("'Welcome to Solo'net Microfinance bank.".title().center(100, "#"))
    home()

    
def home():
    print(f'\nLogin or Register')
    user = input('> ').strip().lower() 
    if user == 'login':
        login()
    elif user == 'register':
        register()
    else:
        print('Invalid entry. Try Again')
        home()
    
    
def login():
    # print('Login')
    '''Login Page'''
    username = input('Username: ')
    pword = pw.pwinput(mask='^')
    password = getpass.getpass()
    if username != info['Username'] and pword != info['Password']:
        print('Invalid Login Details')
    else:
        print(f'Welcome back, {info["Name"]}')
    
def register():
    print('register')
    

    
    
    
    #  info = {
    #     'Name': input('Name: ').strip().capitalize(),
    #     'Department': input('Department: ').strip().upper(),
    #     'Email': input('Email: ').strip().lower(),
    #     'Password': input('Password: ').strip(),
    #    }
    
    
    
    
    
    
    
land()