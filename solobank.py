import time
import pwinput as pw
import re


bankUser = {}
userName = []
pass_word = []

def home():
    print('''
          
          SOLOBANK 
            APP\n'''.center(110, '_'))
    land()
    
def land():
    print('\nWelcome, you are to create an account as a first time user.')
    user = input("""
    Press '1' to create an account: """.strip())
    if user != '1':
        print('\nError. Try again')
        land()
    else:
        register()

def register():
    print('\nCreate Username and Password\n')
    info_tab()
    login()
    
    
def info_tab():
    userId = input('Username:  '.strip())
    match = re.findall(r'\w+\d+@\w+\.\w+', mail)
    if match:
        print('Email created')
    else:
        print('Inc`orrect email pattern.')
    userName.append(userId)
    time.sleep(1)
    
    passId = pw.pwinput(mask='*').strip()
    time.sleep(1)
    
    pword = pw.pwinput(mask='*').strip()
    time.sleep(2)
    if passId != pword:
        print('Error. Try Again.\n')
        time.sleep(1)
        info_tab()
    else:
        pass_word.append(pword)
        print('Username and Password created successfully.\n')
        time.sleep(3)
        print('Kindly provide the following information to complete your account creation.')
        info = {
            'Name': input('Name: '.strip().title()),
            'Age': int(input('Age: ').strip()),
            'BVN': int(input('BVN: ').strip()),
            'E-mail': input('email: '.strip()),
            'Secret Key': input('Enter your secret key: '.strip().lower()),
            'City': input('Your city: '.strip().capitalize()),
            'State': input('State: '.strip().capitalize()) 
        }
        bankUser[userId] = info 
        bankUser.update({userId:info})
        # print(f'\n {bankUser}')
        # print(pass_word)
        time.sleep(2)
        print('\n redirecting...\n\n')
        time.sleep(3)

    
def login():
    print('Welcome. Kindly enter your Login details.'.center(80, "_"))
    name_check()
    password_check()
    bank()
    
def name_check():
    loginName = input('Username: ')
    if loginName not in userName:
        print('Invalid Username')
        name_check()      
def password_check():
    loginPW = pw.pwinput('Password: ')
    if loginPW not in pass_word:      
        print('Invalid Password')
        password_check()
    else:
        print('Login Successful. Redirecting...')
        time.sleep(3)
        bank()
        
def bank():
    print(f'Welcome {userName[0]}. What do you want to do today?')
    print(f"""
          1. Check Balance
          2. Transfer
          3. Update details
          4. Check transfer records
          5. Logout.
          
          """)
    home()
  
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


