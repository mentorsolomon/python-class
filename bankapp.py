import pwinput as pw
import getpass
usersData = {}


def land():
    print("'Welcome to Solo'net Microfinance bank.".title().center(100, "#"))
    home()

    
def home():
    print(f'\nRegistration Form. Kindly fill the form')
    register()
       
    
def register():
    print('Enter your Details.\n')
    info()
    

def info():
    info = {
        'Name': input('Name: ').strip().capitalize(),
        'Phone': input('Telephone: ').strip(),
        'Age': int(input('Age:  ').strip()),
        'Email': input('Email: ').strip().lower(),
        'Password': input('Password: ').strip(),
        'Secret Key': input('Enter your secret key: ').strip().lower(),
        'City': input('Your city: ').strip().capitalize(),
        'State': input('State: ').strip().capitalize()
       }
    print('Registration Successful. Redirecting...')
    usersData.update(info)
    print(usersData)
    login()


def login():
    print('login')
    '''Login Page'''
    Email = input('Email: ')
    pword = pw.pwinput(mask='^')
    password = getpass.getpass('Enter Password > ')
    if Email != info['Email'] and pword != info['Password']:
        print('Invalid Login Details.Try Again')
        login()
    else:
        print(f'Welcome, {info["Name"]}')
        


    
    
   
    
    
    
    
    
land()