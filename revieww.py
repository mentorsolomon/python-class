"""
 number (object) = int() [class integer] / 34 = integer class 
"""

import mysql.connector as sql
import random 

mycon = sql.connect(host = '127.0.0.1', user = 'root', password = '',)

mycursor = mycon.cursor()

# mycursor.execute('CREATE Database ASK_db')
# mycursor.execute('SHOW Databases')
# for db in mycursor:
#     print(db)

mycursor.execute('CREATE TABLE Bank_USERs(user_id INT UNIQUE AUTO_INCREMENT) ')



class Bank:
    def __init__(self):
        self.name = 'ASK'
        self.rc_no = '2345678CS'
        
        #self.home()
    
    def home(self):
        print(f'''
              Welcome to {self.name} 
                           
              1. Sign Up
              2. Login
              3. Exit
              
              ''')
        
        user = input('Option: ')
        if user == '1':
            self.signup()
        elif user == '2':
            self.login()
        elif user == '3':
            exit()  
        else:
            print('Invalid Option')
            self.home()    
                  
    
    def password_checker(self, pass1, pass2):
        if pass1 != pass2:
            print('Password Mismatch')
        else:
           print('Correct. Saved') 
    
    def signup(self):
        Fullname = input('Fullname: '.strip())
        Age = int(input('Age: ').strip())
        e_mail = input('Email: '.strip())
        account_balance = 0
        BVN = int(input('BVN: '.strip()))
        account_number = random.randint(1000000000, 1999999999)
        password1 = input('Password: '.strip())
        password2 = input('Confirm Password: '.strip())
        self.password_checker(password1, password2)
        
        # query = 'INSERT INTO customer_table(fullname, e_mail, account_number, account_balance, bvn, password2, age) VALUES(%s, %s, %s, %s, %s, %s, %s)'
        
        # values = (Fullname, , account_number, account_balance, BVN, password, Age)
        # mycursor.execute(query, values)
        
        
    
    def login(self):
        pass
    
    def dashboard(self):
        pass



mybank = Bank()

if __name__ == '__main__':
    # mybank.home()
    pass
    
#print(mybank.home)