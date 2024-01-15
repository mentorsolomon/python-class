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


# ==============
#numbers = []
# for num in range(1,21):
#     print(num)
#     numbers.append(num) #append adds a range of value or values to an empty list already created
# print(numbers)
 
# firstName = []
# surName = []
# fName = input('Firstname:  ')
# sName = input('Surname: ')
# firstName.append(fName)
# surName.append(sName)
# firstName.delete
                  
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

# # Assignment for the new year
# data1 = ['Solomon','Gabriel', 'Samuel', 'Pelumi', 'James', 'Tolashe', 'Blessing', 'Ota', 'Sheyi', 'Oyindamola', 'Precious']
# data2 = ['Adedokun','Tossu', 'Obilade', 'Adewumi', 'Simeon', 'Tanimola', 'Olaiya', 'Ayoade', 'Afolabi', 'Olodude']
# answer = []
# # dataa = zip(data1, data2)

# print('JAMB UTME EXAMINATION PAGE.'.center(100,'_'))
# print('''Welcome to the UTME examination portal 2023.
#          Kindly fill in the required forms
#       ''')
# fName = input('First name: ').strip().capitalize()
# sName = input('Surname: ').capitalize().strip()
# if (fName in data1) and (sName in data1):
#     print('Welcome, input registration number.')
#     regNo = input('JAMB Registration Number: ').upper().strip()
#     user = input('''
#             Kindly pick class
#              1. Science
#              2. Art
#              3. Commercial
             
#              ''')
#     if user.strip() == '1' or user.strip().lower() == 'science':
#         print(f"""
#             NAME: {fName} {sName}
#             REG NO: {regNo}
#             SCIENCE OPTION      
#             Examination Year: 2023cl
#             Your subjects combinations are:
#                 - English Language
#                 - Physics
#                 - Chemistry
#                 - Mathematics*
#                 - Biology*
#             Note: Pick your courses with respect to the choice of your course of study.
                            
#                 """)
#         exam = input("Press 'START' or 'S' to start: ").lower()
#         if exam == 'start' or exam == 's':
#             print(f'You examination starts now {fName}. Goodluck')
#             user = input("""1. The two major types of culture are____________?
#                             (A) material and non material
#                             (B) aesthetic and non_esthetic
#                             (C) temporary and permanent
#                             (D) positive and negative.
#                             : 
                            
#                             """).upper()
#             if user == ('A') or user ==('B') or user ==('C') or user ==('D'):
#                     print(f'Your answer is, {user}')
                    
#                     user = input("""2. What strategy works best with early childhood education?
#                         (A) Singing and dancing
#                         (B) Toys and drawing
#                         (C) Play way
#                         (D) Reading and writing
#                             : 
                            
#                             """).upper()
#                     print(f'Your answer is, {user}')
                
#                     user = input("""3. According to national minimum standards the teacher pupil ratio at ECCD is?
#                         (A) 1:40
#                         (B) 1:45
#                         (C) 1:25
#                         (D) 1:35
#                             : 
                            
#                             """).upper()
#                     print(f'Your answer is, {user}') 
                    
#             # examination menu
#         else:
#             print(f'Invalid response; TRY AGAIN {fName}')
        
#     elif user.strip() == '2' or user.strip().lower() == 'art':
#         print(f"""
#             NAME: {sName} {fName}
#             REG NO: {regNo}
#             ART OPTION      
#             Examination Year: 2023
#             Your subjects combinations are:
#                 - English Language
#                 - Literature in English
#                 - CRS
#                 - Yoruba*
#                 - Government*
#             Note: Pick your courses with respect to the choice of your course of study.
                            
#             """)
#         exam = input("Press 'START' or 'S' to start: ").lower()       
#         if exam == 'start' or exam == 's':
#                 print(f'You examination starts now {fName}. Goodluck')
#                 user = input("""1. The two major types of culture are____________?
#                             (A) material and non material
#                             (B) aesthetic and non_esthetic
#                             (C) temporary and permanent
#                             (D) positive and negative.
#                             : 
                            
#                             """).upper()
#                 print(f'Your answer is, {user}')
                
#                 user = input("""2. What strategy works best with early childhood education?
#                         (A) Singing and dancing
#                         (B) Toys and drawing
#                         (C) Play way
#                         (D) Reading and writing
#                             : 
                            
#                             """).upper()
#                 print(f'Your answer is, {user}')
                
#                 user = input("""3. According to national minimum standards the teacher pupil ratio at ECCD is?
#                         (A) 1:40
#                         (B) 1:45
#                         (C) 1:25
#                         (D) 1:35
#                             : 
                            
#                             """).upper()
#                 print(f'Your answer is, {user}')
                          
#                 # examination menu
#         else:
#                 print(f'Invalid response; TRY AGAIN {fName}')
        
#     elif user.strip() == '3' or user.strip().lower() == 'commercial':
#         print(f"""
#                 NAME: {fName} {sName}
#                 REG NO: {regNo}
#                 COMMERCIAL OPTION      
#                 Examination Year: 2023
#                 Your subjects combinations are:
#                 - English Language
#                 - Accounting
#                 - Mathematics
#                 - Government*
#                 - Economics*
#             Note: Pick your courses with respect to the choice of your course of study.
                            
#             """)       
        
#         exam = input("Press 'START' or 'S' to start: ").lower()
#         if exam == 'start' or exam == 's':
#             print(f'You examination starts now {fName}. Goodluck!!')
#             user = input("""1. The two major types of culture are____________?
#                             (A) material and non material
#                             (B) aesthetic and non_esthetic
#                             (C) temporary and permanent
#                             (D) positive and negative.
#                             : 
                            
#                             """).upper()
#             print(f'Your answer is, {user}')
                
                
#             user = input("""2. What strategy works best with early childhood education?
#                         (A) Singing and dancing
#                         (B) Toys and drawing
#                         (C) Play way
#                         (D) Reading and writing
#                             : 
                            
#                             """).upper()
#             print(f'Your answer is, {user}')
                
#             user = input("""3. According to national minimum standards the teacher pupil ratio at ECCD is?
#                         (A) 1:40
#                         (B) 1:45
#                         (C) 1:25
#                         (D) 1:35
#                             : 
                            
#                             """).upper()
#             print(f'Your answer is, {user}')    
#             # examination menu
#         else:
#             print(f'Invalid response; TRY AGAIN {fName}')
            
#     # picking a class closing tag 
#     else:
#         print('Kindly pick a class, to enhance your examination combination ')
         
# # name not in database else
# else:
#     print('Name not in Database. Kindly confirm registration credentials.')
    
    
    # =======================================================
    # 1. do a todo list
    
# x = []
# for y in range(3):
#     x.append(y)
# print(x)
        
    #     print('''
    #           1. add to list
    #           2. Edit Item
    #           3. Display list
    #           4. delete item
    #           5. delete list
    #           ''')
    # 2. a cbt exam for 50 people and do the exAM FOR THEM
    
    # answer to assignment 2024 python
     
# firstName = []
# secondName = []
# print('Welcome to AITECH ATMAN CBT CENTER'.center(115, '.'))
# print('Kindly confirm if the registration is for one person or more than one person.')
# user = input('''Personal / 1 or Corporate / 2:
#              > ''').lower()
# if user.strip() == 'personal' or user == '1':
#     print('Proceed to registration menu')
# elif user.strip() == 'corporate' or user == '2':
#     print('How many students do you want to register?')
# else:
#     print('Error')

# numberOfStudents = int(input('Enter a number here: '))
# students = list(range(numberOfStudents))
# studentsName = []
# user = input('students name are: ')


# name_of_students = ['Solomon','Gabriel', 'Samuel', 'Pelumi', 'James', 'Tolashe', 'Blessing', 'Ota', 'Sheyi', 'Oyindamola', 'Precious']
# for student in name_of_students:
#     print(f'{student}, Welcome back to School')

# students = []
# numberStudents = int(input('How many students are you with: '))
# studentslow = numberStudents - numberStudents
# studentshigh = numberStudents
# students = list(range(studentslow, studentshigh))
# for student in students:
#     user = input('Enter the name of student: ')
#     students.append(user)
#     print(students)
#     break
    
# ================================================================
# firstName = []
# secondName = [] 
studentsList = []
results = []

print('Welcome to AITECH ATMAN CBT CENTER'.center(115, '.'))
print('How many students are you registering and are sitting for this exam?')
studentNumber = int(input('> '))
students = range(studentNumber)
# print(students)

for inputName in students:
    studentName = input(f'Name of student {inputName + 1}: ').capitalize().strip()
    studentsList.append(studentName)
# print(f'{studentsList} \n')

for studentName in studentsList:
    print(f"It's time to take your test {studentName}")
    questions = [
        "1. What is the capital of Ghana a.) Accra b.) Utanbatoor", 
        "2. What is the capital of Nigeria a.) Abuja b.) Rivers", 
        "3. What is the capital of Tunisia a.) Jebba b.) Leona", 
        "4. What is the capital of Togo a.) Lome b.) Gertha",  
        "5. What is the capital of Germany a.) Munchen b.) Berlin", 
        "6. What is the capital of Sweden a.) Heilsinki b.) Stockholm", 
        "7. What is the capital of Cape Verde a.) Praia b.) Ladta", 
        "8. What is the capital of South Africa a.) Cape Town b.) Johannesburg", 
        "9. What is the capital of Oyo a.) Ibadan b.) Oyo", 
        "10. What is the capital of Lagos a.) Ikeja b.) Alimosho", 
        
    ]
    answers = ['a', 'a', 'b', 'a', 'b', 'b', 'a', 'a', 'a', 'a' ]
    score = 0

    for questions, ans in zip(questions, answers):
            print(questions)
            user = input('Input Answer: ')
            if user.strip().lower()== ans:
                print('Correct')
                score+=10
            else:
                print('wrong')
    print(f' \n Your total score is {score}%')
            
    # if score == 100:
    #     print(f'''Excellent. Exceptional Performance {studentName}. Congratulations, You have secured yourself a place at the battle of the champions  \n''')
    # elif score >= 70:
    #     print(f'Excellent. Satisfactory Performance {studentName}. Congratulations  \n')
    # elif score >=60:
    #     print(f' Very Good. Satisfactory Performance {studentName}. Congratulations  \n')
    # elif score >=50:
    #     print(f'Good. Satisfactory Performance {studentName}. Congratulations  \n')
    # elif score >=40:
    #     print(f'Poor. Satisfactory Performance {studentName}. Congratulations \n')
    # elif score >=0:
    #     print(f'Fail. Satisfactory Performance {studentName}. BEST OF LUCK NEXT TIME  \n')
    # else:
    #     print('Try again')
        
    results.append(score)  
    # print(results)
for finale in (studentsList, results): 
         print(finale)

print('The overall best student of the test is... drumroll')
print(max(finale))
print('The mean or average score')
print(sum(results)/len(results))
    

        
        

# correction of assignment============================2===================================
# studentList = []

# user = int(input('''How many students are taking the test?:
#              > '''))
# for students in range(user):
#     student = input(f'Name of student {student + 1}: ')
#     studentList.append(student)
# # print(studentList)
# for eachStudent in studentList:
#     print(f"{eachStudent} it's time for your test")
    
#     questions = [
#         "1. What is the capital of Ghana a.) Accra b.) Utanbatoor", 
#         "2. What is the capital of Nigeria a.) Abuja b.) Rivers", 
#         "3. What is the capital of Tunisia a.) Jebba b.) Leona", 
#         "4. What is the capital of Togo a.) Lome b.) Gertha",  
#         "5. What is the capital of Germany a.) Munchen b.) Berlin", 
#         "6. What is the capital of Sweden a.) Heilsinki b.) Stockholm", 
#         "7. What is the capital of Cape Verde a.) Praia b.) Ladta", 
#         "8. What is the capital of South Africa a.) Cape Town b.) Johannesburg", 
#         "9. What is the capital of Oyo a.) Ibadan b.) Oyo", 
#         "10. What is the capital of Lagos a.) Ikeja b.) Alimosho", 
        
#     ]
#     answers = ['a', 'a', 'b', 'a', 'b', 'b', 'a', 'a', 'a', 'a' ]
#     score = 0

#     for questions, ans in zip(questions, answers):
#         print(questions)
#         user = input('Input Answer: ')
#         if user.strip().lower()== ans:
#             print('Correct')
#             score+=10
#         else:
#             print('wrong')
#     print(f'Your total score is {score}%')
#     if score == 100:
#         print(f'Excellent. Exceptional Performance {eachStudent}. Congratulations, You have secured yourself a place at the battle of the champions')
#     elif score >= 70:
#         print(f'Excellent. Satisfactory Performance {eachStudent}. Congratulations')
#     elif score >=60:
#         print(f' Very Good. Satisfactory Performance {eachStudent}. Congratulations')
#     elif score >=50:
#         print(f'Good. Satisfactory Performance {eachStudent}. Congratulations')
#     elif score >=40:
#         print(f'Poor. Satisfactory Performance {eachStudent}. Congratulations')
#     elif score >=0:
#         print(f'Fail. Satisfactory Performance {eachStudent}. BEST OF LUCK NEXT TIME')