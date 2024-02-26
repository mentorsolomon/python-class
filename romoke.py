import re
import random
import pwinput
import time
import datetime as dt
import mysql.connector as sql

mycon = sql.connect(host = '127.0.0.1', user = 'root', password = '', database = 'Romoke_db') #HUPD

mycursor = mycon.cursor()

# mycursor.execute('CREATE DATABASE Romoke_db')

# mycursor.execute('SHOW DATABASES')
# for databases in mycursor:
#     print(databases)

# mycursor.execute('''CREATE TABLE bank_user
#                  (
                
#                  bank_user_id INT AUTO_INCREMENT PRIMARY KEY, 
#                  Fullname VARCHAR(40),
#                  Email VARCHAR(25) UNIQUE,
#                  Account_number VARCHAR(11) UNIQUE,
#                  Account_Balance FLOAT,
#                  bvn VARCHAR(11) UNIQUE,
#                  date_joined DATETIME DEFAULT CURRENT_TIMESTAMP
                 
#                  )
#                  ''')

# mycursor.execute('''
#                  ALTER TABLE bank_user ADD
#                  (
#                      age VARCHAR(2),
#                      password VARCHAR(15) UNIQUE
#                  )
                 
#                  ''')

# mycursor.execute('''
#                  ALTER TABLE bank_user 
#                  ADD(
#                     username VARCHAR(15) UNIQUE
                     
#                  )
#                  ''')

# mycursor.execute('SHOW DATABASES')
# for databases in mycursor:
#     for x in databases:
#         print(x)


class BANKAPP():
    
    
    def __init__(self):
        self.name = 'Romoke BANK'
        self.code = '*904#'
        
             
    def landing_page(self):
        print(f''' 
              
              Welcome to {self.name} 
              
              1. Sign Up
              2. Login
              3. Exit
              
              ''')
        user = input('Select Option: ').strip().lower()
        
        if user == '1' or user == 'sign up':
            self.sign_up()
            
        elif user == '2' or user == 'login':
            self.log_in()
            
        elif user == '3' or user == 'exit':
            exit()
            
        else:
            print('Invalid Entry. Try again')
            self.landing_page()
        
        
    def sign_up(self):
        print(f'''\nProvide your details for registration in the panel below.\n''')
        time.sleep(2)
        
        name = input('Name: ').strip().title()
        age = input('Age: ').strip()
        account_number = random.randint(5000000000, 5099999999)
        account_balance = 0
        bvn = input('BVN: ').strip()
        username = input('Username: ')
        self.mail()
        password1 = input('Password: ').strip()
        password2 = input('Confirm Password: ').strip()
        self.password_check(password1, password2)
        print(f'Your account number is {account_number}. Kindly write it down or save it somewhere.')
        print(f'''\nAccount Creation successful. 
              {self.name} welcomes to you on board.
              
              Login to save any amount or perform other transactions.
              
              ''')
        
        self.log_in()
       
        
    
    
    def mail(self):
        email = input('Email: ')
        match = re.findall(r'\w+\d+@\w+\.\w+', email)
        if not match:
            print('Email Mismatch. Try Again(e.g "ssss12@gmail.com")')
            self.mail()
        else:
            time.sleep(2)   
        
        
        
    def password_check(self, pass1, pass2):
        if pass1 != pass2:
            print('Password Mismatch')
            self.password_check()
        else:
            print('Password Created')
            
            
        
        
    
    def log_in(self):
        pass



mybankapp = BANKAPP()
mybankapp.landing_page()