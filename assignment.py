# calculator
# e = 10
# a = float(input('enter first number: '))
# b = float(input('enter second number: '))
# calc = (input('what operation would you like to perform? sum, minus, multi, divide, EXP, sqr: ')).lower()
# if calc == 'sum':
#     print(a + b)
# elif calc == 'minus':
#     print(a - b)
# elif calc == 'multi':
#     print(a * b)
# elif calc == 'divide':
#     print(a / b)
# elif calc == 'exp':
#     print(a * (e**b))
# elif calc == 'sqr':
#     print(a**b)
# else:
#     print('Try Again')

# ====================================================
#SQI WELCOME
# fname = ['Solomon','Gabriel', 'Samuel', 'Pelumi', 'James', 'Tolashe', 'Tehya', 'Ota', 'Sheyi']
# surname = ['Adedokun','Tossu', 'Obilade', 'Adewumi', 'Simeon', 'Tanimola', 'Olaiya', 'Olodude', 'Afolabi']
# dataScience = '#400,000'
# AI = '#230,000'
# javascripts = '#200,000'
# digMarket = '#125,000'

# nameOne = input("Enter your First name: ").capitalize()
# nameTwo = input("Enter your Surname: ").capitalize()

# if (nameOne not in fname) and (nameTwo not in surname):
#     print('Error: No admission into SQI COLLEGE OF ICT given yet')
    
# else:
#     print(f"""
#           Welcome to SQI COLLEGE OF ICT
          
#           {nameOne} {nameTwo} you have gained admission into SQI COLLEGE OF ICT.
#           Kindly proceed to checkout our available courses pay for fees on or before the due date.
#           1. DATA SCIENCE
#           2. AI
#           3. JAVASCRIPTS
#           4. DIGITAL MARKETING          
          
#           """)
#     user = input('Kindly select course of choiCe?: ').lower()
#     if user == 'data science':
#         print(f'''
#               The tuition of data science is {dataScience}
#               ''')
#         courses = input('Will you like to pay now? Yes or No: ').lower()
#         if courses == 'yes':
#             print('You will be redirected to the payment gateway')
#         elif courses == "no":
#             print('That will be all for now')
#         else:
#             print('Kindly enter the correct prompt')   
            
#     elif user == 'ai':
#         print(f'''
#             AI is available at {AI}
#               ''')
#         courses = input('Will you like to pay now? Yes or No: ').lower()
#         if courses == 'yes':
#             print('You will be redirected to the payment gateway')
#         elif courses == "no":
#             print('That will be all for now')
#         else:
#             print('Kindly enter the correct prompt')  
            
#     elif user == 'javascripts':
#         print(f'''
#             JAVASCRIPTS is available at {javascripts}
#               ''')
#         courses = input('Will you like to pay now? Yes or No: ').lower()
#         if courses == 'yes':
#             print('You will be redirected to the payment gateway')
#         elif courses == "no":
#             print('That will be all for now')
#         else:
#             print('Kindly enter the correct prompt')  
        
#     elif user == 'DIGITAL MARKETING':
#         print(f'''
#             DIGITAL MARKETING is available at {digMarket}
#               ''')
#         courses = input('Will you like to pay now? Yes or No: ').lower()
#         if courses == 'yes':
#             print('You will be redirected to the payment gateway')
#         elif courses == "no":
#             print('That will be all for now')
#         else:
#             print('Kindly enter the correct prompt')  
        
#     else:
#         print('Kindly enter a valid course')
                   
# ========================================================
# studentFname = ['Aishat', 'Solomon', 'Kayode', 'Damilare', 'Emmanuel', 'Tehya']
# staffsFname = ['Joke', 'Richard', 'Ige', 'Damola', 'Kemi', 'Oyindamola']

# print('Welcome to SQI COLLEGE of ICT'.center(100,'_'))
# user = input('''
#              Who are you?
#              1. Staff
#              2. Student
#              3. Visitor
#              4. Exit
#              Kindly Select: 
    
#              ''').lower().strip()
# if user == '1' or user == 'staff':
#     firstName = input('Kindly input your name: ').strip().capitalize()
#     if firstName in staffsFname:
#         print(f'You are welcome back, {firstName}')
#     else:
#         print('Record not found, Try Again')
# # ==========================================================
# elif user == '2' or user == 'student':
#     fName = input('Kindly input your First name: ').strip().capitalize()
#     if fName in studentFname:
#         print(f'You are welcome back to school, {fName}')
#          # ==========================================================
#          # payment gateway check
#         user = input(f'''
#                     Payment Status
                    
#                         Have you paid your fees?
                        
#                     1. Yes, I have paid my fees fully
#                     2. Yes, but I have only paid part.
#                     3. No, I have not.
                    
#                     ''')
#         if user == '1'.strip():
#             print(f'Congratulations, Welcome to SQI College  of ICT {fName}')
#         elif user == '2'.strip():
#             print(f'Access granted. Congratulations {fName} on your admission. Kindly note you have until the end of the month to balance your fees.')
#         elif user == '3'.strip():
#             print(f'Congratulations on your admission {fName}. Kindly note you have until the end of the month to pay your fees')
#         else:
#             print(f'Invalid prompt {fName}. Try Again')
#     else:
#         print('Record not found')
# #    ===============================================================
# elif user == '3' or user == 'visitor':
#     surName = input('Kindly enter your surname: ')
#     print(f'You are welcome to the college of SQI {surName}. Do enjoy your stay and the tour around the facilities.')
    
# elif  user == '4' or user == 'exit':
#     exit()
# else:
#     print('INVALID COMMAND TRY AGAIN')
# ===========================================================

# Assignment for the new year
data1 = ['Solomon','Gabriel', 'Samuel', 'Pelumi', 'James', 'Tolashe', 'Blessing', 'Ota', 'Sheyi', 'Oyindamola', 'Precious']
data2 = ['Adedokun','Tossu', 'Obilade', 'Adewumi', 'Simeon', 'Tanimola', 'Olaiya', 'Ayoade', 'Afolabi', 'Olodude']
answer = []

print('JAMB UTME EXAMINATION PAGE.'.center(100,'_'))
print('''Welcome to the UTME examination portal 2023.
         Kindly fill in the required forms
      ''')
fName = input('First name: ').strip().capitalize()
sName = input('Surname: ').capitalize().strip()
if (fName in data1) and (sName in data2):
    print('Welcome, input registration number.')
    regNo = input('JAMB Registration Number: ').upper().strip()
    user = input('''
            Kindly pick class
             1. Science
             2. Art
             3. Commercial
             
             ''')
    if user.strip() == '1' or user.strip().lower() == 'science':
        print(f"""
            NAME: {fName} {sName}
            REG NO: {regNo}
            SCIENCE OPTION      
            Examination Year: 2023cl
            Your subjects combinations are:
                - English Language
                - Physics
                - Chemistry
                - Mathematics*
                - Biology*
            Note: Pick your courses with respect to the choice of your course of study.
                            
                """)
        exam = input("Press 'START' or 'S' to start: ").lower()
        if exam == 'start' or exam == 's':
            print(f'You examination starts now {fName}. Goodluck')
            user = input("""1. The two major types of culture are____________?
                            (A) material and non material
                            (B) aesthetic and non_esthetic
                            (C) temporary and permanent
                            (D) positive and negative.
                            : 
                            
                            """).upper()
            if user != ('a') or user !=('b') or user !=('c') or user !=('d'):
                print('Invalid answer selected')
            else:
                print(f'Your answer is, {user}')
                
            user = input("""2. What strategy works best with early childhood education?
                        (A) Singing and dancing
                        (B) Toys and drawing
                        (C) Play way
                        (D) Reading and writing
                            : 
                            
                            """).upper()
            print(f'Your answer is, {user}')
                
            user = input("""3. According to national minimum standards the teacher pupil ratio at ECCD is?
                        (A) 1:40
                        (B) 1:45
                        (C) 1:25
                        (D) 1:35
                            : 
                            
                            """).upper()
            print(f'Your answer is, {user}') 
            # examination menu
        else:
            print(f'Invalid response; TRY AGAIN {fName}')
        
    elif user.strip() == '2' or user.strip().lower() == 'art':
        print(f"""
            NAME: {sName} {fName}
            REG NO: {regNo}
            ART OPTION      
            Examination Year: 2023
            Your subjects combinations are:
                - English Language
                - Literature in English
                - CRS
                - Yoruba*
                - Government*
            Note: Pick your courses with respect to the choice of your course of study.
                            
            """)
        exam = input("Press 'START' or 'S' to start: ").lower()       
        if exam == 'start' or exam == 's':
                print(f'You examination starts now {fName}. Goodluck')
                user = input("""1. The two major types of culture are____________?
                            (A) material and non material
                            (B) aesthetic and non_esthetic
                            (C) temporary and permanent
                            (D) positive and negative.
                            : 
                            
                            """).upper()
                print(f'Your answer is, {user}')
                
                user = input("""2. What strategy works best with early childhood education?
                        (A) Singing and dancing
                        (B) Toys and drawing
                        (C) Play way
                        (D) Reading and writing
                            : 
                            
                            """).upper()
                print(f'Your answer is, {user}')
                
                user = input("""3. According to national minimum standards the teacher pupil ratio at ECCD is?
                        (A) 1:40
                        (B) 1:45
                        (C) 1:25
                        (D) 1:35
                            : 
                            
                            """).upper()
                print(f'Your answer is, {user}')
                          
                # examination menu
        else:
                print(f'Invalid response; TRY AGAIN {fName}')
        
    elif user.strip() == '3' or user.strip().lower() == 'commercial':
        print(f"""
                NAME: {fName} {sName}
                REG NO: {regNo}
                COMMERCIAL OPTION      
                Examination Year: 2023
                Your subjects combinations are:
                - English Language
                - Accounting
                - Mathematics
                - Government*
                - Economics*
            Note: Pick your courses with respect to the choice of your course of study.
                            
            """)       
        
        exam = input("Press 'START' or 'S' to start: ").lower()
        if exam == 'start' or exam == 's':
            print(f'You examination starts now {fName}. Goodluck!!')
            user = input("""1. The two major types of culture are____________?
                            (A) material and non material
                            (B) aesthetic and non_esthetic
                            (C) temporary and permanent
                            (D) positive and negative.
                            : 
                            
                            """).upper()
            print(f'Your answer is, {user}')
                
            user = input("""2. What strategy works best with early childhood education?
                        (A) Singing and dancing
                        (B) Toys and drawing
                        (C) Play way
                        (D) Reading and writing
                            : 
                            
                            """).upper()
            print(f'Your answer is, {user}')
                
            user = input("""3. According to national minimum standards the teacher pupil ratio at ECCD is?
                        (A) 1:40
                        (B) 1:45
                        (C) 1:25
                        (D) 1:35
                            : 
                            
                            """).upper()
            print(f'Your answer is, {user}')    
            # examination menu
        else:
            print(f'Invalid response; TRY AGAIN {fName}')
            
    # picking a class closing tag 
    else:
        print('Kindly pick a class, to enhance your examination combination ')
         
# name not in database else
else:
    print('Name not in Database. Kindly confirm registration credentials.')