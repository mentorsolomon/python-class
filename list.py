# import random
# ==========================LIST CLASS===================================

# LIST IS A COLLECTION WHICH IS
# ORDERED, 
# CHANGEABLE,
# ALLOWS DUPLICATE VALUE
# ITEMS ARE INDEXED.

# symbol for a list is []

# my_list1 = ['Tunde', 'Azeez', 'Boluwatife', 'Temitayo', 'Bukunmi', 'Solomon']

# print(my_list1)
# print('\n')

# my_list2 = [1,2,3,4,5,6]

# my_list_copy = []
# my_list3 = ['Tunde', 'Emmanuel', [1,2,3], 'James']

# print(my_list1[1:5])
# print(my_list1[::-1])
# print(my_list1[0][4])

# CHANGING ENTRIES ON A LIST
# my_list1[0:3] = ['Emmanuel','Shade', 'James']
# print(my_list1)

# functions we can perform on list
# my_list1.append('AYOMIDE LATE COMER')
# my_list1.insert(1, 'DAMILARE')
# print(my_list1.index('Solomon'))
# my_list1.remove('Solomon')
# my_list1.clear()
# my_list1.append(my_list2)
# print(my_list1)
# print("\n")
# my_list_copy = my_list1.copy()
# print(my_list_copy)

# my_list1.extend(my_list2)
# print(my_list1)

# palindrome cheecker:

user = input('Enter Palindrome: ').strip()
check = "".join(user.split())
if check == check[::-1]:
    print("Word is a palindrome")
else:
    print("'Word entered is not a palindrome")
# =======================================================================================
# word = input('PALINDROME CHECKER: ').strip().lower()
# word_split = word.split()
# word_join = "".join(word_split)
# print(word_join, word_split)
# if word_join != word_join[::-1]:
#     print('Not a palindrome')
# else:
#     print('PAlindrome')















# my_list = ['White Rice', 'beans', 'bread','White Rice', 'Meat', 'egg', 'fried rice', 'jollof rice', 'pounded yam and egusi', 'fanta', 'water', 'chi exotic', 'wine', True, 2 + 1j, ['Bukunmi', 'Solomon'], (343, 67)]

# my_list2 = [100, 200, 400, 700]

# print(my_list[0][0]) 
'''
INDEX STARTS COUNT FROM (0)
'''
'''A MAN A PLAN A CAR A CANAL PANAMA'''
# print(type(my_list))
'''
Prints the making component of the object. Where Object() is my_list
'''

# print(len(my_list))
'''
LEN STARTS COUNT FROM (1)
'''  
# # print(my_list[5])

"""Below is an example of slicing in python"""
# print(my_list[::-1])
# print(my_list[-1][1])
# print(my_list[2:7])
# print(my_list[:7])

""" Changing list item"""
# my_list[3] = 'Egusi'
# print(len(my_list))
# print(my_list)
# print('\n')
# my_list[0:3] = ['french fries', 'chicken and chips', 'EFO RIRO']
# print(my_list)

'''Test'''
# my_list[0:3] = ['french fries', 'chicken and chips', 'quakammoli', 'LEMONADE', 'EFO RIRO', 'BANGA SOUP']
# print(len(my_list))
# print(my_list)

# functions of a list
# append
# my_list.append('favor')
# print(my_list)
# my_list.append(my_list2)
# print(my_list)

# insert
# my_list.insert(3, 'Solomon King')
# print(len(my_list))
# print(my_list)

# extend
# print(my_list.count('White Rice'))
# print(my_list)

# .copy()
# .insert(0, 'enter value here')
# .remove('enter value here')
# .clear()

# my_list = [1,2,3,4,5,6,1]
# for item in my_list:
#     print()



# ============================================================== 
# x = list(range(1,21))
# print(random.choice(x))

# y_list = []
# for y in range(1,21):
#     y_list.append(y)
# print(y_list)


# name_of_students = ['Solomon','Gabriel', 'Samuel', 'Pelumi', 'James', 'Tolashe', 'Blessing', 'Ota', 'Sheyi', 'Oyindamola', 'Precious']

# x = random.choice(name_of_students)
# print(x)


# for student in name_of_students:
#     print(f'{student}, Welcome back to School')
    
# numbers = []
# for num in range(1,21):
#     # print(num)
#     numbers.append(num) #append adds a range of value or values to an empty list already created
# print(numbers)

# for num in range(1, 13):
#     print(f'\n{num} times table') #\n gives us space before or in between our entries
#     for num2 in range(1, 13):
#         calc = num * num2
#         print(f'{num} X {num2} = {calc}')

# =======================================================================================
# CBT APPLICATION

# ques1 = 'What is the capital of Ghana a.) Accra b.) Utanbatoor'
# print(ques1)
# user = input('Enter your answer: ').strip().lower()
# if user == 'a':
#     print('Correct')
# elif user == 'b':
#     print('Wrong')
# else:
#     print('Invalid selection')
        

# real way ======================== using list for cbts
# questions = [
#     "1. What is the capital of Ghana a.) Accra b.) Utanbatoor", 
#     "2. What is the capital of Nigeria a.) Abuja b.) Rivers", 
#     "3. What is the capital of Tunisia a.) Jebba b.) Leona", 
#     "4. What is the capital of Togo a.) Lome b.) Gertha",  
#     "5. What is the capital of Germany a.) Munchen b.) Berlin", 
#     "6. What is the capital of Sweden a.) Heilsinki b.) Stockholm", 
#     "7. What is the capital of Cape Verde a.) Praia b.) Ladta", 
#     "8. What is the capital of South Africa a.) Cape Town b.) Johannesburg", 
#     "9. What is the capital of Oyo a.) Ibadan b.) Oyo", 
#     "10. What is the capital of Lagos a.) Ikeja b.) Alimosho", 
    
# ]
# answers = ['a', 'a', 'b', 'a', 'b', 'b', 'a', 'a', 'a', 'a' ]
# score = 0

# for questions, ans in zip(questions, answers):
#     print(questions)
#     user = input('Input Answer: ')
#     if user.strip().lower()== ans:
#         print('Correct')
#         score+=10
#     else:
#         print('wrong')
# print(f'Your total score is {score}%')
    
    
    # ====================================================================
    # list Comprehension JANUARY 16TH 2024
    
# num = []
# for x in range(10):
#     num.append(x)
# print(num)

# num = [x for x in range(10)]
# print(num)
# ==============================
    
    
# def getAns(entry):
#     if entry == 1:
#         return('Lord of the rings')
#     elif entry == 2:
#         return('Lord of the caves')
#     elif entry == 3:
#         return('Lord of the gyms')
#     elif entry == 4:
#         return('Lord of the rockets')
#     elif entry == 5:
#         return('Lord of the flies')


# r = random.randint(1,5)
# give = getAns(r)
# print(give)

# ========================

# password_checker = input('Enter password: ')
# if (len(password_checker) >= 8):
#     print("Password accepted")
    
# elif password_checker == '':
#     print('Field cannot be empty. Try Again.')

# else:
#     print('''
#     Password must not be less than 8 character set.
#     Try again....................................
#     ''')
# ===============================================
# try:   
#     name = 'sunday'
#     # print(name[2::])
#     print(name[7])
# except IndexError:
#     print('Character does not reach 7. Try again')

# ================ MARCH 12TH 2024 ============================

# comment = 'solomon@gmail.com'

# # startswith and #endswith

# print(comment.startswith(",,"))
# print(comment.endswith("@gmail.com"))

# name = input('name: ').strip()
# print(name)

# word = 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Hic earum consectetur delectus numquam nihil expedita eveniet enim saepe perferendis provident commodi molestias deserunt nostrum, soluta vel maxime amet neque suscipit'
# name = 'issokay'
# x = word.split()
# print('\n')
# print('x'.join(x))
