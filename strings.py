# name = '     Solomon and the guys are always so fun and awesome to much. They are dope and reliable.    '.strip()

# # print(name)
# # print(name[6])
# # print(name[0:4])
# # print(name[0:4:2])
# # print('The length of the senhtence is ', len(name))
# # print(len(name.strip()))
# # print(name.upper())
# # print(name.title())
# # print(name.split('.', 2))

# # _split = name.split()
# # print(_split)

# # _join = '_'.join(_split)
# # print(_join)
# # print(name.replace('guys', 'goons'))
# print(name.center(70,'_'))


# ===================================================

# non parametized function
# def addition():
#     x = int(input('valueone: '))
#     y = int(input('valuetwo: '))
#     print(x + y)
    
# addition()

# parametized
# def addition(x:int, y:int): #:int is for documenttation purpose
#     print(x+y)
# addition(x = 23, y = 13)

# =============================================================
# user = input('ussd code: ').strip()

# if user.strip() == '*131#':
#     print('Welcome')
# else:
#     print('Invalid prompt')

# __________________________________________________________________________________

# ques = input('are you happy? yes or no: ').strip().lower
# if ques == 'yes':
#     print('Opor oooo')
# else:
#     print("Don't give up")

# ______________________________

# assignment
# calculator
# sqi entrance software   school fees and chill

# do for student staffs database
# # first check and then check if they are who they say they are:

# cbt application
#  shows the qqquestions collect answer and gives Results.

# -----------------------------
# =====================================================1
# regNo = input('JAMB Registration Number: ').upper().strip()
# user = input('''
#             Kindly pick class
#              1. Science
#              2. Art
#              3. Commercial
             
#              ''')
# if user == '1'.strip() or user == 'science'.strip().upper():
#         print(f"""
#         NAME: {fName} {sName}
#         REG NO: {regNo}
#         SCIENCE CLASS      
#         Examination Year: 2023
            
#         """)
# elif user == '2'.strip() or user == 'art'.strip().upper():
#         print(f"""
#             NAME: {fName} {sName}
#             REG NO: {regNo}
#             ART CLASS      
#             Examination Year: 2023
#             """)
# elif user == '3'.strip() or user == 'commercial'.strip().upper():
#         print(f"""
#                 NAME: {fName} {sName}
#                 REG NO: {regNo}
#                 COMMERCIAL CLASS      
#                 Examination Year: 2023
#             """)
# else:
#         print('Kindly pick a class')

# exam = input('Proceed to START exam: Yes or No ').capitalize
# if exam == 'Yes':
#         print('Your time starts now')
# elif exam == 'No':
#         print('Take a minute but stand  for the next candidate')        
# else:
#     print('Invalid response; TRY AGAIN')




# # ========================================================    
# # (if name in data1...)
# else:
#     print('Name not in Database. Kindly confirm registration credentials.')


# ==============
# comb1 = ['''
#          English Language
#          Physics
#          Chemistry
#          Mathematics
#          Biology
#         Note: Pick your courses with respect to the choice of your course of study
#          '''.strip()]
# comb2 = ['''
#          English Language,
#          Literature in English,
#          CRS,
#          Yoruba,
#          Government.
         
#         Note: Pick your courses with respect to the choice of your course of study
#          '''.strip()]

# comb3 = ['''
#          English Language
#          Accounting
#          Government
#          Economics
         
#         Note: Pick your courses with respect to the choice of your course of study
#          ''']

# WHILE LOOPS
# =================================================
# print('You can have a go at guessing our secret Number')
# secretNumber = 9
# gCount = 0
# gLimit = 3

# while gCount < gLimit:
#     guess = int(input('NUM: '))
#     gCount += 1
#     if guess == secretNumber:
#         print('You won!')
#         break
#     else:
#         print('Try Again')
# else:
#         print('Sorry, you failed😒')

# i = 1
# while i <= 12:
#     print('#' * i)
#     i = i + 1
# print('DONE!')

