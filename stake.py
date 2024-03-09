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
            print('You are not of legal age of Acceptance'.title().splitlines())
            time.sleep(2)
            exit()
        else:
            print('Age inline with the range of Legal Acceptance.'.title())
            print('Proceed to Register')    
            time.sleep(3)  
            print('\n')   

            
    def mail_checker(self, ee_mail):   
        pattern = (r'\d+\w+@\w+\.\w+') or (r'\w+\d+@\w+\.\w+')
        find = re.findall(pattern,ee_mail)
        if not find:
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
            # print(details) ======= PRINTS ALL IN A ROW FORMAT AND ENSURES ALL THE ENTRIES ARE IN A TABLE FORMAT

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
        8. Correct details.
        

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
        elif enter == '8':
            self.correct_details()
        else:
            print('Invalid selection')
            self.dashboard()
    
    def stake(self):
        print('''
        
                PLAY THE STAKE GAMES

                The following are the available games
                1. Secret Number                2. High and Low
                3. WHO IS?... QUESTIONS AND ANSWER
                4. LEFT OR RIGHT                5. GUESS THE NAME/ RANDOM

                If you have what it takes, enter the dragon.. 
        
        ''')
        user = input('Game to play: ').strip()
        if user == '1':
            self.game_1()
        elif user == '2':
            self.game_2()
        elif user == '3':
            self.game_3()
        elif user == '4':
            pass
        elif user == '5':
            pass
        else:
            print('Wrong input.')
            self.stake()




    def game_1(self):
        query_g = ('SELECT * FROM Sport_bettor where Email = %s')
        value_g = (self.Email,)
        mycursor.execute(query_g,value_g)

        details_game = mycursor.fetchone()
        Balance = details_game[6]

        print(f'''
            {self.Name} you are about to play {self.name} secret Number:

            Below are the rules:
            1. You have to stake an amount to play
            2. This is a game of 5 odds
            3. The number is random integer between 1 and 15

            ...stake responsibly...
        
        ''')
        try:
            amount = float(input('''
            Amount to stake from balance 
                        OR 
            Press "0" to exit>> '''))
            if (amount > Balance) or (amount<0):
                print('''
                You cannot play this round. 
                Kindly deposit and try again or stake accordingly.
                Press "1" to deposit
                Press "2" to stake amount higher than zero(0)
                ''')
                user = input('Enter choice: ').strip()
                if user == '1':
                    self.deposit()
                elif user == '2':
                    self.game_1()
            elif (amount==0):
                self.dashboard()
            else:
                try:           
                    x = random.randint(1, 15)
                    user = int(input('Guess the Secret Number: '))
                    print(f'\n{x} is the correct number')
                    if user == x:
                        print('\nCongratulations, you are amazing.'.title())
                        Balance+=amount*5
                        print('#',{amount*5},"added to Balance")
                    else:
                        print('\nWrong answer. Try again')
                        Balance-=amount

                    query = ('UPDATE Sport_bettor SET Balance = %s WHERE Email = %s')  
                    value = (Balance, self.Email)     
                    mycursor.execute(query, value)


                    if Balance <= (Balance/4):
                        print('You have a quarter of your starting funds left.')
                        option = input('''
                        Do you want to continue?
                        Yes, No
                        
                        ''').strip().lower()
                        if option == 'yes':
                            self.game_1()
                        elif option == 'no':
                            self.dashboard()
                        else:
                            print('Invalid Option')
                            self.terms()
                    elif Balance == 0:
                        print('''
                        You exhausted your money.
                        Press "1" to deposit
                        Press "2" to exit
                        ''')
                        user = input('Option: ').strip()
                        if user == '1':
                            self.deposit()
                        elif user == '2':
                            print('Do come back')
                            sleep(4)
                            exit()
                        else:
                            print('Enter a valid command')
                            self.terms()
                    else:
                        self.game_1()
                except ValueError:
                    print('Integer expected.')
        except Exception as e:
            print(f'Wrong Entry, {e}. Try a number (1,2,3... 50) ')
            self.game_1()
                
    def game_2(self):
        query_high = ('SELECT * FROM Sport_bettor WHERE Email = %s')
        value_high = (self.Email,)

        mycursor.execute(query_high, value_high)

        # mycon.commit()

        details_game_2 = mycursor.fetchone()
        Balance = details_game_2[6]


        print(f'''
              {self.Name}, {self.name} presents HIGH and LOW
                        Rules
                1. You will be given a number, and you will be provide with another number.
                2. You have to guess if the number to be provided on a scale of inequality is:
                    a. Higher than the number.
                    b. Lower than the number.
                    c. Equal to the number.

                Are you ready to play?
        
        ''')
        user = input('Yes or No >>'  ).strip().lower()
        if user == 'no':
            sleep(2)
            self.dashboard()
        elif user == 'yes':
            try:
                wager = float(input('Stake amount OR Press "0" to exit>>  '))
                if (wager>Balance) or (wager<0):
                    print('''
                    You cannot play this round. 
                    Kindly deposit and try again or stake accordingly.
                    Press "1" to deposit
                    Press "2" to stake amount higher than zero(0)
                    ''')
                    user = input('Enter choice: ').strip()
                    if user == '1':
                        self.deposit()
                    elif user == '2':
                        self.game_2()
                elif (wager==0):
                    self.dashboard()
                else:
                    try:         
                        number = random.randint(1,999)
                        print("\n")
                        print(number,"is your the number\n")
                        number_2 = random.randint(1, 999)
                        guess = input('''
                        Select
                        1. Higher
                        2. Lower
                        3. Equal to

                        >> 
                        
                        ''').strip()
                        if guess == '1':
                            print(f'The first number is {number} and the second number {number_2}.')
                            if (number_2 > number):
                                Balance += wager*2
                                print("#",wager*2, "was added to your Balance")
                            else:
                                Balance -= wager
                                print('You lost your Wager')

                        elif guess == '2':
                            print(f'The first number is {number} and the second number {number_2}.')
                            if (number_2 < number):
                                Balance += wager*2
                                print(wager*2, "was added to your Balance")
                            else:
                                Balance -= wager
                                print('You lost your Wager')
                        
                        elif guess == '2':
                            print(f'The first number is {number} and the second number {number_2}.')
                            if (number_2 < number):
                                Balance += wager*2
                                print(wager*2, "was added to your Balance")
                            else:
                                Balance -= wager
                                print('You lost your Wager')
                        elif guess == '3':
                            print(f'The first number is {number} and the second number {number_2}.')
                            if (number_2 == number):
                                Balance += wager*5
                                print(wager*5, "was added to your Balance")
                            else:
                                Balance -= wager
                                print('You lost your Wager')
                        else:
                            print('RETRY')                            

                        query_wager = ('UPDATE Sport_bettor SET Balance = %s WHERE Email = %s')
                        value_wager = (Balance, self.Email)
                        mycursor.execute(query_wager, value_wager)
                        # mycon.commit()

                        if Balance <= (Balance/4):
                            print('You have a quarter of your starting funds left.')
                            option = input('''
                            Do you want to continue?
                            Yes, No
                            
                            ''').strip().lower()
                            if option == 'yes':
                                self.game_2()
                            elif option == 'no':
                                self.dashboard()
                            else:
                                print('Invalid Option')
                                self.terms()
                        elif Balance == 0:
                            print('''
                            You exhausted your money.
                            Press "1" to deposit
                            Press "2" to exit
                            ''')
                            user = input('Option: ').strip()
                            if user == '1':
                                self.deposit()
                            elif user == '2':
                                print('Do come back')
                                sleep(4)
                                exit()
                            else:
                                print('Enter a valid command')
                                self.terms()
                        else:
                            self.game_2()
                        

                    except Exception as e:
                        print(f"{e}. Retry")
                        self.game_2()
            except Exception as e:
                    print(f"{e}")
                    self.game_2()
        else:
            print('Invalid Command')
            self.game_2()

    
    def game_3(self):
        query_who = ('SELECT * FROM Sport_bettor WHERE Email =%s')
        value_who = (self.Email,)

        mycursor.execute(query_who, value_who)
        # mycon.commit()
         
        details_who = mycursor.fetchone()
        Balance = details_who[6]

        print(f'{self.Name} proceed to play {self.name} WHO IS...?')
        user = input('Play or Quit? ').lower().strip()
        if user == "quit":
            self.dash



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
        print('Transaction Successful.')
        self.deposit_again()




    def deposit_again(self):
        sleep(2)
        user = input('Deposit More?.Yes or No: ').strip().lower()
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
        

    def correct_details(self):
        user = input('''
        What do you want to change
        1. name
        2. Age
        3. Email
        >> ''').strip()
        if user == '1':
            new_name = input('Input Name: ').strip()
            try:
                querys = 'UPDATE Sport_bettor SET Name = %s WHERE Email = %s'
                values = (new_name, self.Email)

                mycursor.execute(querys,values)
                print('Changes Successfully.')
                sleep(2)
                self.login()
            except Exception as e:
                print(f'{e}')
        elif user == '2':
            new_age = input('Input Age: ').strip()
            try:
                querys = 'UPDATE Sport_bettor SET Age = %s WHERE Email = %s'
                values = (new_age, self.Email)

                mycursor.execute(querys,values)
                print('Changes Successfully.')
                sleep(2)
                self.login()
            except Exception as e:
                print(f'{e}')
        elif user == '3':
            new_email = input('Input Email: ')
            try:
                querys = 'UPDATE Sport_bettor SET Email = %s WHERE Name = %s'
                values = (new_email, self.Name)

                mycursor.execute(querys,values)
                print('Changes Successfully. Login Again')
                sleep(2)
                self.login()
            except Exception as e:
                print(f'{e}')
        else:
            print('Invalid prompt')
            self.dashboard()


    
mysporty = SPORTY()
mysporty.home()