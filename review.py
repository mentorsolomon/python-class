
import mysql.connector as sql
import random
import time
import pwinput
import pandas as pd

mycon = sql.connect(host='127.0.0.1', user='root', passwd='', database = 'MTP_db')

mycursor = mycon.cursor()

# mycursor.execute('CREATE DATABASE MTP_db ')
# mycursor.execute('SHOW DATABASES')
# for db in mycursor:
#     print(db)

# mycursor.execute('CREATE TABLE customer_table (id INT(4) AUTO_INCREMENT PRIMARY KEY, fullname VARCHAR(50), email VARCHAR(50) UNIQUE, account_no VARCHAR(10) UNIQUE, account_balance FLOAT, date_joined DATETIME DEFAULT CURRENT_TIMESTAMP  )')

# mycursor.execute('ALTER TABLE customer_table ADD password VARCHAR(20)')
# mycursor.execute('ALTER TABLE customer_table CHANGE id customer_id INT AUTO_INCREMENT')

# mycursor.execute('CREATE TABLE transact_history(id INT AUTO_INCREMENT PRIMARY KEY, type VARCHAR(10), amount FLOAT , sender_name VARCHAR(50), reciever_name VARCHAR(50), reciever_no VARCHAR(10),sender_no VARCHAR(10),  date_time DATETIME )')

mycursor.execute('ALTER TABLE transact_history CHANGE date_time date_time DATETIME DEFAULT CURRENT_TIMESTAMP')


class Bank:
    def __init__(self):
        self.name = 'MTP'
        self.rc_no = '2345667BA'

    def home(self):
        print(f'''
                Welcome to {self.name}
        1. Sign up
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
        if pass1 == pass2:
            print('✅')
        else:
            print('Password miss matched!')
            self.signup()

    def signup(self):
        print('''       
                Signup
              ''')
        fullname = input('Full-name: ').strip()
        email = input('Email: ').strip()
        account_number = random.randint(1000000000,1999999999)
        account_balance = 0
        bvn = input('BVN: ').strip()
        password1 = input('Password: ').strip()
        password2 = input('Confirm Password: ').strip()
        self.password_checker(password1, password2)

        print('Proccessing...')
        time.sleep(2)
        try: 
            query = 'INSERT INTO customer_table(fullname, email, account_no, account_balance, bvn, password) VALUES(%s,%s,%s,%s,%s,%s)'

            values = (fullname, email, account_number, account_balance, bvn, password2)
            mycursor.execute(query, values)

            mycon.commit()
        except Exception as e:
            print(f'Registration unsuccessful\n{e}.\n Kindly input valid informations')
            self.signup()

        print('Account created successfully.')
        self.login()

        
    def login(self):
        print('''       
                Login
              ''')
        
        lg_email = input('Email: ')
        lg_password = pwinput.pwinput()

        print('Proccessing...')
        time.sleep(2)

        try: 
            query = 'SELECT * FROM customer_table WHERE email=%s AND password =%s'
            values = (lg_email, lg_password)
            mycursor.execute(query, values)

            details = mycursor.fetchone()
            self.email = details[2]
            # print(details)
           
            if details:
                print('Login successfull✅')
                self.dashboard()
            else:
                print(f'Invalid Login details. Try again')
                self.login()

        except Exception as e:
            print(f'An error occured\n{e}. \nTry again')
            self.login()



    def dashboard(self):
        query = 'SELECT * FROM customer_table WHERE email=%s'
        values = (self.email,)
        mycursor.execute(query, values)

        details = mycursor.fetchone()
        print(details)
        self.account_no = details[3]
        self.account_balance = details[4]
        self.name = details[1]
        self.email = details[2]

        print(f'''
        Welcome {self.name}
        Account number: {self.account_no}
        Account balance: {self.account_balance}

        1. Deposit                  2. Withdraw
        3. Transfer                 4. Airtime/Data
        5. Transaction history      *. Exit
        
        ''')
        user = input('Option: ')
        if user == '1':
            self.deposit()
        elif user == '5':
            self.transactions()
        elif user == '*':
            exit()
    
    def deposit(self):
        amount = float(input('Amount: '))

        query1 = 'SELECT account_balance FROM customer_table WHERE email=%s'
        values1 = (self.email,)
        mycursor.execute(query1, values1)
        details = mycursor.fetchone()

        balance = details[0] 

        balance += amount

        query2 = ('UPDATE customer_table SET account_balance = %s WHERE email = %s')
        values2 = (balance, self.email)
        mycursor.execute(query2, values2)
        mycon.commit()

        query3 = 'INSERT INTO transact_history (type, amount, sender_name, reciever_name, reciever_no, sender_no) VALUES(%s,%s,%s,%s,%s,%s)'
        values3 = ('Deposit', amount, self.name, self.name, self.account_no, self.account_no)
        mycursor.execute(query3,values3)
        mycon.commit()

        print('Proccessing...')
        time.sleep(2)

        user = input('Transaction successfull. \nPress 1 to perform another transaction or 2 to exit.').strip()
        if user == '1':
            self.dashboard()
        elif user == '2':
            exit()
        else:
            print('Invalid Option.')
            self.dashboard()

    def transactions(self):
        
        query =  'SELECT * FROM transact_history WHERE sender_no = %s'
        val = (self.account_no,)
        mycursor.execute(query,val)
        histories = mycursor.fetchall()
        
        _types = [history[1] for history in histories]
        amounts = [history[2] for history in histories]
        sender_name = [history[3] for history in histories]
        reciever_name = [history[4] for history in histories]
        date_time = [history[-1] for history in histories]


        df = pd.DataFrame({
            'Type':_types,
            'Amount':amounts,
            'Sender name': sender_name,
            'reciever_name':reciever_name,
            'Date&Time':date_time

        })

        print('Proccessing...')
        time.sleep(2)
        
        print(df)

mybank = Bank()
if __name__ == '__main__':
    mybank.home()


