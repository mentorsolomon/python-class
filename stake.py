from time import sleep
import colorama
import time
import re
import random
import mysql.connector as sql
import pwinput as pw

# ============================= SQL PROMPT ===================================
mycon = sql.connect(host = '127.0.0.1' , user = 'root', password = '',  database = 'Sporty_db')

mycursor = mycon.cursor()

mycon.autocommit = True


# mycursor.execute("""
                 
#                  CREATE DATABASE Sporty_db

# """)

# mycursor.execute("""
                
#                 CREATE TABLE Sport_bettor
#                 (
#                 bettor_id INT AUTO_INCREMENT PRIMARY KEY,
#                 Name VARCHAR(40),
#                 userId VARCHAR(8) UNIQUE,
#                 Age INT(2),
#                 Email VARCHAR(35) UNIQUE,
#                 Password VARCHAR(35) UNIQUE,
#                 Balance FLOAT,
#                 City VARCHAR(25),
#                 State VARCHAR(25),
#                 Date_joined DATETIME DEFAULT CURRENT_TIMESTAMP
#                 )
#             """)


# mycursor.execute('''ALTER TABLE Sport_bettor ADD Pin VARCHAR(4) ''')
# mycursor.execute('ALTER TABLE Sport_bettor CHANGE bettor_id Bettor_ID INT(4) AUTO_INCREMENT')

# ==============================

class SPORTY():
    def __init__(self):
        self.name = "Sporty+"
        self.balance = 0
        
        
    def home(self):
        print(f'''
              
              Welcome to {self.name}
              REMEMBER.. STAKE RESPONSIBLY
              
              First time user... Kindly enter "1" to submit your details...

              1. Register
              2. Login
              3. Read T&C's
              
              ''')
        sleep(1)
        user = input('Select your choice: ')
        if user.strip() == '1':   
            self.register()
        elif user.strip() == '2':
            self.login()
        elif user.strip() == '3':
            self.terms()
            
        else:
            print('Enter a valid command')
            self.home()

    
    def register(self):
        age = int(input('Age: '))
        self.age_check(age)
        name = input('Fullname: ').strip().title()
        user_id = random.randint(70000000, 99999999)
        balance = 0
        city = input('City: ').strip()
        state = input('State: ').strip()
        e_mail = input("Enter mail: ").strip()
        self.mail_checker(e_mail)
        password1 = pw.pwinput('Enter Password: ')
        password2 = pw.pwinput('Confirm Password: ')
        self.password_check(password1, password2)
        time.sleep(2)

        try:
            query ="""
            INSERT INTO Sport_bettor(Age, Name, userId, Email, Password, Balance, City, State )
            VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"""

            values = (age, name, user_id, e_mail, password2, balance, city, state)

            mycursor.execute(query, values)

            # mycon.commit()
        
        except Exception as e:
            print(f"Registration Unsuccessful {e} \n. Kindly provide right information.")
            self.register()

        print('Profile created successfully')
        self.login()


    def age_check(self, Agee):        
        if Agee < 18:
            print('You are not of legal age of acceptance')
            time.sleep(2)
            exit()
        else:
            print('Age inline with the range of Legal Acceptance.')
            print('Proceed to Register')    
            time.sleep(3)  
            print('\n')   

            
    def mail_checker(self, ee_mail):   
        pattern = r'\w+\d+@\w+\.\w+'
        match = re.match(pattern,ee_mail)
        if not match:
            print('Email Mismatch.. TRY "ask11@gmail.com"')
            self.mail_checker()
        else:
            time.sleep(2)   
        
    def password_check(self, pass1, pass2):
        if pass1 != pass2:
            print('Password mismatch Try again')
            self.password_check()
        else:
            time.sleep(3)
            



    def terms(self):
        print('''
           Lorem ipsum dolor sit amet consectetur, adipisicing elit. Ipsum beatae totam distinctio omnis illo culpa cumque veniam tempore quibusdam ipsa! Voluptatem ipsa reprehenderit, a excepturi dolore quibusdam quia minus dolorum.
           Lorem ipsum dolor sit amet consectetur adipisicing elit. Hic earum consectetur delectus numquam nihil expedita eveniet enim saepe perferendis provident commodi molestias deserunt nostrum, soluta vel maxime amet neque suscipit?Lorem ipsum dolor sit amet consectetur adipisicing elit. Ullam doloremque alias culpa quae commodi possimus! Dignissimos non molestiae delectus officia mollitia assumenda veniam repudiandae sint rem, magnam eos laborum illo?Lorem, ipsum dolor sit amet consectetur adipisicing elit. Sit odio maxime, dicta similique ratione id, in architecto provident esse aspernatur delectus numquam dignissimos debitis. Similique dolorem expedita minus qui repudiandae!Loremlorem

           Lorem, ipsum dolor sit amet consectetur adipisicing elit. Aliquam alias, exercitationem eaque non molestias eius nisi libero sapiente labore nobis laborum sint, facilis nam sed, doloribus magnam a voluptatem magni?

        ''')
        time.sleep(2)
        user = input('Press "1" to go home or "s" to exit. ').strip()
        if user == '1':
            self.home()
        elif user == 's':
            exit()
        else:
            self.terms()
    



    def login(self):

        print('''

                Login your Sporty+ Account
        ''')

        login_mail = input('Email:  ').strip()
        login_pwd = pw.pwinput('Password: ').strip()
        print('Checking details...')
        time.sleep(2)

        try:
            query = 'SELECT * FROM Sport_bettor WHERE Email = %s AND Password = %s'

            values = (login_mail,login_pwd)

            mycursor.execute(query,values,)

            details = mycursor.fetchone()
            self.Email = details[4]
            # print(details)

            if details:
                print('Login Successful.')
                time.sleep(3)
                self.dashboard()
            else:
                print('Login Credentials not accurate. Try again.')
                self.login()

        except Exception as e:
            print(f'{e}')
            self.login()
    



    def dashboard(self):
        query = 'SELECT * FROM Sport_bettor WHERE Email =%s'
        value = (self.Email,)
        mycursor.execute(query, value)

        details = mycursor.fetchone()
        # print(details) 

        self.Name = details[1]
        self.userId = details[2]
        self.Email = details[4]
        self.Balance = details[6]

        print(f'''
        Welcome {self.Name}. 
        Your User ID is {self.userId} and balance is #{self.Balance}.

        Remember stake responsibly...

        1. Deposit          2. Withdraw
        3. Check Balance    4. Stake       
        5. Log out          6. Create Transaction Pin
        7. Read Guidelines to stake.
        

        ''')
        enter = input('Enter Your choice: ').strip()
        if enter == '1':
            self.deposit()
        elif enter == '2':
            self.withdraw()
        elif enter == '3':
            self.check_balance()
        elif enter == '4':
            self.stake()
        elif enter == '5':
            self.logout()
        elif enter == '6':
            self.pin_create()
        elif enter == '7':
            self.guidelines()
        else:
            print('Invalid selection')
            self.dashboard()
    
    def stake(self):
        print('''
        
                PLAY THE STAKE GAMES

                The following are the available games
                1. Secret Number
                2. High and Low
                3. WHO IS?... QUESTIONS AND ANSWER
                4. LEFT OR RIGHT
                5. GUESS THE NAME/ RANDOM

                If you have what it takes, enter the dragon.. 
        
        ''')
        user = input('Game to play: ').strip()
        if user == '1':
            pass
        elif user == '2':
            pass
        elif user == '3':
            pass
        elif user == '4':
            pass
        elif user == '5':
            pass
        else:
            print('Wrong input.')
            self.stake()




    def guidelines(self):
        print('''
           Lorem ipsum dolor sit amet consectetur, adipisicing elit. Ipsum beatae totam distinctio omnis illo culpa cumque veniam tempore quibusdam ipsa! Voluptatem ipsa reprehenderit, a excepturi dolore quibusdam quia minus dolorum.
           Lorem ipsum dolor sit amet consectetur adipisicing elit. Hic earum consectetur delectus numquam nihil expedita eveniet enim saepe perferendis provident commodi molestias deserunt nostrum, soluta vel maxime amet neque suscipit?Lorem ipsum dolor sit amet consectetur adipisicing elit. Ullam doloremque alias culpa quae commodi possimus! Dignissimos non molestiae delectus officia mollitia assumenda veniam repudiandae sint rem, magnam eos laborum illo?Lorem, ipsum dolor sit amet consectetur adipisicing elit. Sit odio maxime, dicta similique ratione id, in architecto provident esse aspernatur delectus numquam dignissimos debitis. Similique dolorem expedita minus qui repudiandae!Loremlorem

           Lorem, ipsum dolor sit amet consectetur adipisicing elit. Aliquam alias, exercitationem eaque non molestias eius nisi libero sapiente labore nobis laborum sint, facilis nam sed, doloribus magnam a voluptatem magni?

        ''')
        time.sleep(2)
        user = input('Press "1" to go to dashboard or "s" to exit. ').strip()
        if user == '1':
            self.dashboard()
        elif user == 's':
            exit()
        else:
            self.guidelines()




    def deposit(self):
        print(f'How much do you want to deposit into your {self.name} account.')
        amount =float(input('Amount: '))

        query1 = ('SELECT * FROM Sport_bettor WHERE Email = %s')
        value1 = (self.Email,)
        mycursor.execute(query1, value1)
        details = mycursor.fetchone()

        Balance = details[6]

        Balance += amount

        # ================ SECOND QUERY TO DATABASE TO UPDATE THE ACCOUNT BALANCE WITH DEPOSIT =================

        query2 = ('UPDATE Sport_bettor SET Balance = %s WHERE Email =%s')
        value2 = (Balance, self.Email)
        mycursor.execute(query2,value2)
        # mycon.commit()
        self.payagain()




    def payagain(self):
        print('Transaction Successful.')
        sleep(2)
        user = input('Do you want to deposit another amount now?: ').strip().lower()
        if user == 'yes':
            sleep(1)
            self.deposit()
        elif user == 'no':
            sleep(2)
            self.dashboard()
        else:
            print('Invalid Command.')
    



    def withdraw_again(self):
        print('Withdrawal successful')
        sleep(2)
        user = input('Do you want to withdraw another amount now?: ').strip().lower()
        if user == 'yes':
            sleep(1)
            self.withdraw()
        elif user == 'no':
            sleep(2)
            self.dashboard()
        else:
            print('Invalid Command.')




    def withdraw(self):
        amount = float(input('Amount to Withdraw: '))
        self.amount_checker(amount)
        account_no_receiver = input('Kindly provide the account to send the money: ')
        query = ('SELECT * FROM Sport_bettor WHERE Email = %s')
        value = (self.Email,)
        
        mycursor.execute(query,value)

        details = mycursor.fetchone()
        Pin = details[10]
        Balance = details[6]      

        prompt = input('''
        Enter transaction Pin. 
            Press "1" to create. 
                Press "s" to skip if you have already created >>  '''.strip())
        if prompt == '1':
            self.pin_create()
        elif prompt == 's':
            for num in range(1,6):
                pin = pw.pwinput('Enter your Secure transaction pin to confirm transaction: ').strip()
                if pin != Pin:
                    if num == 1:
                        if pin != Pin:
                            print('You have 4 attempts left')
                    elif num == 2:
                        if pin != Pin:
                            print('You have 3 attempts left')
                    elif num == 3:
                        if pin != Pin:
                            print('You have 2 attempts left')
                    elif num == 4:
                        if pin != Pin:
                            print('You have 1 attempt left. ')
                            time.sleep(2)
                            print('Account will be automatically logged out on final attempt.')
                            time.sleep(2)
                    elif num == 5:
                            if pin != Pin:
                                print('Account Logged out.')
                                time.sleep(2)
                                exit()
                else:
                    Balance -= amount
                    print('Transaction Approved')
                    break
        else:
            sleep(2)
            self.withdraw()
        
        query5 = ('UPDATE Sport_bettor SET Balance = %s WHERE Email = %s')
        value5 = (Balance, self.Email)

        mycursor.execute(query5,value5)
        # mycon.commit()

        self.withdraw_again()
    


    def amount_checker(self, amounnt):
        if amounnt > self.Balance:
            user = input('''
            Transaction Failed. 
            Amount in account Low.
            Press 1 to deposit, press 2 to check balance >> ''').strip()
            if user == '1':
                sleep(1)
                self.deposit()
            elif user == '2':
                time.sleep(1)
                self.check_balance()
            else:
                print('Invalid Command')
                self.amount_checker()
        elif amounnt <= 0:
            print('You can not withdraw #0.. Try Again.. ')
            self.withdraw()
        else:           
            time.sleep(1)




    def check_balance(self):
        print('Fetching Balance...')
        sleep(3)
        print(f'\nYour {self.name} balance is #{self.Balance}\n')
        user = input('Press "1" to return to dashboard or press "s" to EXIT: ').lower().strip()
        if user == '1':
            self.dashboard()
        elif user == 's':
            sleep(3)
            exit()
        else:
            self.check_balance()



    def logout(self):
        user = input('ARE YOU SURE YOU WANT TO LOGOUT? : ').strip().lower()
        if user == 'yes':
            print('Do come back')
            time.sleep(2)
            self.home()
        elif user == 'no':
            print('🎈🎈')
            self.dashboard()
        
        else:
            print('Command error')
            self.login()



    def pin_create(self):
        query_pin = ('SELECT * FROM Sport_bettor WHERE Email = %s')
        value_pin = (self.Email,)

        mycursor.execute(query_pin,value_pin)

        details = mycursor.fetchone()
        Pin = details[10]

        if not Pin: 
            print('Your PIN will be used to confirm transactions do keep it safe and away from thirdparty.')         
            user1 = pw.pwinput('ENTER 4 unique Transaction pin: ').strip()
            user2 = pw.pwinput('Confirm pin: ').strip()
            if user1 != user2:
                print('Pin mismatch. Check and try again.')
                self.pin_create()
            else:
                query = 'UPDATE Sport_bettor SET Pin=%s WHERE Email=%s'
                value = (user2, self.Email)
                mycursor.execute(query,value)
                # mycon.commit()   


                print('Pin created successfully')
                sleep(2)
                self.transact_pin()
        else:
            print('You already created a PIN')
            self.dashboard()



    
    def transact_pin(self):
        user = input('Press "1" to return to dashboard and press "s" to logout: ').strip().lower()
        if user == '1':
            sleep(3)
            self.dashboard()
        elif user == 's':
            sleep(2)
            exit()
        else:
            print('Wrong entry.')  
            self.transact_pin() 
        

    
mysporty = SPORTY()
mysporty.home()