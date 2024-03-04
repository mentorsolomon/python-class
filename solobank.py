from time import sleep
import pwinput as pw
import re
import random
import mysql.connector as sql

mycon = sql.connect(host = '127.0.0.1', user = 'root', password = '', database = 'solobank_db')

mycursor = mycon.cursor()

# mycursor.execute('CREATE Database SOLOBank_db')
# mycursor.execute('SHOW Databases')
# for db in mycursor:
#     print(db)
    
# mycursor.execute('CREATE TABLE customer_table(id INT(4) AUTO_INCREMENT PRIMARY KEY, Fullname VARCHAR(40),Age INT(2), Email VARCHAR(35) UNIQUE, BVN INT(11) UNIQUE)')

# mycursor.execute('ALTER TABLE customer_table ADD account_balance VARCHAR(35) UNIQUE')
# mycursor.execute('ALTER TABLE customer_table CHANGE id customer_id INT AUTO_INCREMENT')
# mycursor.execute('ALTER TABLE customer_table ADD password VARCHAR(10)')
mycursor.execute('ALTER TABLE customer_table ADD account_number VARCHAR(10) UNIQUE')

# # id INT(4) AUTO_INCREMENT PRIMARY KEY, fullname VARCHAR(40), Age VARCHAR(2),BVN VARCHAR(11) UNIQUE, Email VARCHAR(25) UNIQUE,  City VARCHAR(11),  state VARCHAR(11), account_num VARCHAR(10) UNIQUE,username VARCHAR(20) UNIQUE, password VARCHAR, accountbalance FLOAT, datejoined DATETIME DEFAULT CURRENT_TIMESTAMP

bankUser = {}
userName = []
pass_word = []
account_num = []


bankcode = 99
y = random.randint(0000000, 99999999)
# print(f'{bankcode}{y}')
    
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
    match = re.findall(r'\w+\d+', userId)
    if match:
        print('Id created')
    else:
        print('Id must not contain, symbols or sign.')
    userName.append(userId)
    sleep(1)
    
    passId = pw.pwinput(mask='*').strip()
    sleep(1)
    
    pword = pw.pwinput(mask='*').strip()
    sleep(2)
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
        sleep(2)
        print('\n redirecting...\n\n')
        sleep(3)

    
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
    loginPW =pw.pwinput('Password: ') 
    if loginPW not in pass_word:      
        print('Invalid Password')
        password_check()
    else:
        print('Login Successful. Redirecting...')
        sleep(3)
        bank()
        
def bank():
    print(f'Welcome {userName[0]}. Your account number is {bankcode}{y}. What do you want to do today?')
    print(f"""
          
          1. Check Balance
          2. Transfer
          3. Update details
          4. Check transfer records
          5. Logout.
          
          """)
    user = input('Your option:  ')
    if user.strip() == '1' or user.strip() == 'balance':
        balance()
         
    
    home()


def balance():
   global account_number
   account_number = random(0000000000, 999999999)
    
    
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


