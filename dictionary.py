# DICTIONARY IS A COLLECTION THAT IS ORDERED, CHANGEABLE BUT DOES NOT ALLOW DUPLICATE, UNSUBSCRIPTABLE AND UNINDEXED DATA 
# JANUARY 17TH, 2024

# syntax 
# written using {key:value} or dict{key=value}

# vehicle = {
#     'Name': ('BMW','peugoet'),
#     'Year': 2020,
#     'Status': {'Brand New': True, 'Tokunbo':False},
#     'Bonus': {'2 extre tyres', 'Engine oil'},
#     'Price': {6_000_000: 89}
# }

# print(vehicle['Price'].get(89))

# print(vehicle['Name'][1])
# x = vehicle['Bonus'].pop()  #pop selects a value at random
# print(x)

# ============= CHANGE ENTRY ===================
# vehicle['Name'] = 'Legsux'
# print(vehicle['Name'])
# print(vehicle)


# print(vehicle.values())
# for x in vehicle.keys():
#     print(x)
# print(vehicle['Status'].values())
# print(vehicle.values())
# for x in vehicle.values():
#     print(x)

# print(vehicle.items())
# for x,y in vehicle.items():
#     print(f'{x}      --        {y}')

# print(vehicle['Year'])

# vehicle.popitem() #takes no argument
# vehicle.pop() #takes argument
# vehicle.update({'transmission':'automatic'})
# # vehicle['Engine'] = 'v6'
    
# *x, = vehicle
# print(x)
# print(vehicle.get('Price','Not found'))


'''Login'''
# username = input('Username: ')
# pword = pw.pwinput(mask='^')
# # password = getpass.getpass()
# if username != info['Username'] and pword != info['Password']:
#     print('Invalid Login Details')
# else:
#     print(f'Welcome back, {info["Name"]}')


# ===============================================
# classwork

# score = 0
# exam = {
#     "1. What is the capital of Ghana a.) Accra b.) Utanbatoor": "a",
#     "2. What is the capital of Nigeria a.) Abuja b.) Rivers": "a",
#     "3. What is the capital of Tunisia a.) Jebba b.) Leona": "b",
#     "4. What is the capital of Togo a.) Lome b.) Gertha": "a",
#     "5. What is the capital of Germany a.) Munchen b.) Berlin": "b",
#     "6. What is the capital of Sweden a.) Heilsinki b.) Stockholm": "b",
#     "7. What is the capital of Cape Verde a.) Praia b.) Ladta": "a",
#     "8. What is the capital of South Africa a.) Cape Town b.) Johannesburg": "a",
#     "9. What is the capital of Oyo a.) Ibadan b.) Oyo": "a",
#     "10. What is the capital of Lagos a.) Ikeja b.) Alimosho": "a",
# }

# for question, answers in exam.items():
#     print(question)
#     user = input('answer: ').strip().lower()
#     if user != answers:
#         print('wrong')
#     else:
#         print('correct')
#         score += 10
# print(score)

# ========================= CLASS WORK TWO ===================================================
# info = {}

# name = input('Name: ')
# dept = input('Department: ')
# matNo = input('Matric No: ')
# userName = input('Username: ')
# passWord = input('Password: ')

# info.update({
#     'Name': name,
#     'Department': dept,
#     'Matric Number': matNo,
#     'Username': userName,
#     'Password': passWord,
#     })




# '''Login'''
# username = input('Username: ')
# pword = pw.pwinput(mask='^')
# # password = getpass.getpass()
# if username != info['Username'] and pword != info['Password']:
#     print('Invalid Login Details')
# else:
#     print(f'Welcome back, {info["Name"]}')

# ==============================================================================

# import pwinput as pw
# import getpass 


# StudentsData = {}
# students = int(input('How many students are you registering: '))
# for eachStudent in range(students):
#     matricNum = input('Your Matric No: ').strip().capitalize(),
#     info = {
#         'Name': input('Name: ').strip().capitalize(),
#         'Department': input('Department: ').strip().upper(),
#         'Username': input('Username: ').strip().lower(),
#         'Password': input('Password: ').strip(),
#        }
    
#     StudentsData[matricNum] = info
#     StudentsData.update({matricNum:info})
#     print(info)

# print(StudentsData)


# {
#     'Student1': {'Name':'Ade', 'MatNo': '11'},
#     'Student2': {'Name':'James', 'MatNo': '12'}
# }    

# user = input('Kindly press "1" to register')
# if user == '1':
#     x = 1
    
# =======================================



# phone_no = int(input('Enter your number: '))
# numbers = {
#         '1':'One',
#         '2':'Two',
#         '3':'Three',
#         '4':'Four',
#         '5':'Five',
#         '6':'Six',
#         '7':'Seven',
#         '8':'Eight',
#         '9':'Nine',
#         '0': 'Zero'
#         }

# output = ""
# for characters in phone_no:
#     output += numbers.get(characters, "!") + " "
# print(output)



# set dictionary

# list_set = []
# sets = int(input('How many sets do you have: ').strip())


# for sett in range(sets):
#     items = int(input(f'How many items are in Set{sett+1}: ').strip())
#     set_items = []
#     set_items_count = 1

#     for item in range(items):
#         set_data = int(input(f'Data{set_items_count}: ').strip())
#         set_items.append(set_data)
#         set_items_count += 1
    
#     list_set.append(set(set_items))

# print(list_set)


# list_count = 1
# for setts in list_set:
#     print(f'''
#     Set{list_count} = {setts}    
#     ''')
#     list_count += 1

# print('You can now perform your operations')

# ========================================================================
class USSD:
    def __init__(self):
        self.name = 'MTN'
        self.airtime = '*310#'
        self.data = '*312#'
    
    def home(self):
        print(f'''
        {self.name},,, 
        EVERYWHERE YOU GO

        Press *310# for airtime
        Press *312# for data

        Press * for more information.
        ''')

        ussd_code = input('Enter USSD code: ').strip()
        while ussd_code != self.airtime:
            print('Try again.')
            ussd_code = input('Enter USSD code: ').strip()
        
        if ussd_code == self.airtime:
            print('''
            Press
            
            1. Buy airtime
            2. Check Balance''')
        
        elif ussd_code == self.data:
            print('''
            Press
            
            1. Buy Data
            2. Check Balance''')
        



        



       











ussd = USSD()
ussd.home()























