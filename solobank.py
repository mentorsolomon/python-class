import pwinput as pw
import getpass

bankUser = {}
userName = []

def home():
    print('''
          
          SOLOBANK 
            APP\n'''.center(110, '_'))
    land()
    
def land():
    print('\nWelcome, you are to register as a first time user.')
    user = input("Press '1' to open registration portal. > ".strip())
    if user != '1':
        print('\nError. Try again')
        land()
    else:
        register()

def register():
    print('\nWelcome to the registration panel. Kindly provide your details to get started')
    userId = input('Username > ').strip()
    info = {
        'Name': input('Name: ').strip().title(),
        'Age': int(input('Age: ').strip()),
        'E-mail': input('email: ').strip(),
        'Password': input('Password: ').strip(),
        'Secret Key': input('Enter your secret key: ').strip().lower(),
        'City': input('Your city: ').strip().capitalize(),
        'State': input('State: ').strip().capitalize()
    }
    userName.append(userId)
    bankUser[userId] = info 
    bankUser.update({userId:info})
         
    print(bankUser[userId])
#     # print(f'\n {info}')
    
#     # print(f'\n {bankUser}')
    print('\n redirecting...')
    land()
#     login()
    
    
# def login():
#     print('Login Page')
#     mail = input('Enter Username: ')
#     if mail not in userName:
#         print('Invalid Login Credentials. Try Again.')
#         login()
#     else:
#         print('correct')
        
#     pword = input('Enter Password: ')
#     print(f"Welcome. What will you like to do today ")
home()










# ==========================================
# vehicle = {
#     'Name': ('BMW','peugoet'),
#     'Year': 2020,
#     'Status': {'Brand New': True, 'Tokunbo':False},
#     'Bonus': {'2 extre tyres', 'Engine oil'},
#     'Price': {6_000_000: 89}
# }

# print(vehicle['Name'][1])
# x = vehicle['Bonus'].pop()  #pop selects a value at random
# print(x)

# vehicle['Name'] = 'Legsux'
# print(vehicle['Name'])
# print(vehicle)


