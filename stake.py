import time
import re
import random
import mysql.connector as sql
import pwinput as pw

# ============================= SQL SERERERE
mycon = sql.connect(host = '127.0.0.1' , user = 'root', password = '',  database = 'Sporty_db')

mycursor = mycon.cursor()


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
        time.sleep(3)
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

            mycon.commit()
        
        except Exception as e:
            print(f"Registration Unsuccessful {e} \n. Kindly provide right information.")
            self.register()

        print('Account created successfully')
        self.login()


    def age_check(self, Agee):        
        if Agee < 18:
            print('You are not of legal age of acceptance')
            time.sleep(2)
            exit()
        else:
            print('Age inline with the range of Legal Acceptance.')
            print('Proceed to Register')    
            time.sleep(1)  
            print('.') 
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
            print('Your password has been created successfully.')
            time.sleep(3)
            

    def terms(self):
        print('''
            I, Adedokun Solomon, a Second Class Honors graduate of computer science from Ladoke Akintola University of Technology, want to express my profound desire to work with the ministry towards the betterment of the state and help her scale heights digitally. I have ideas I'm open or will love to share with the ministry top personnels incase they are willing to listen to me at any point in time.
            I belief Osun state under the leadership of this government has all it takes to be a pioneer state in the country in terms of innovation and TECH advancements which would not only bring peace but usher in a lot of jobs and a wide array of technological improvements in a lot of sector.
                    Thanks, I hope to hear from you soon. Osun oni baje o
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

        print('\nLogin your Sporty+ Account\n')

        login_mail = input('Email:  ').strip()
        login_pwd = pw.pwinput('Password: ').strip()
        print('Checking details...')
        time.sleep(2)

        try:
            query = 'SELECT * FROM Sport_bettor WHERE Email =%s AND Password =%s'

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
        Welcome {self.Name}. You are on course to be a winner.

        Your User ID is {self.userId} and your current balance is #{self.Balance}.

        1. Deposit          2. Withdraw
        3. Stake            4. Read Guidelines to stake.
        5. Log out

        ''')
        enter = input('Enter Your choice: ').strip()
        if enter == '1':
            self.deposit()
        elif enter == '2':
            self.withdraw()
        elif enter == '3':
            self.stake()
        elif enter == '4':
            self.guidelines()
        elif enter == '5':
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
                


        

            
















mysporty = SPORTY()
mysporty.home()
    

