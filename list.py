# x = list(range(1,20))
# print(x)

# name_of_students = ['Solomon','Gabriel', 'Samuel', 'Pelumi', 'James', 'Tolashe', 'Blessing', 'Ota', 'Sheyi', 'Oyindamola', 'Precious']
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
print(f'Your total score is {score}%')
    