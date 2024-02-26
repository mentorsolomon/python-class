# JANUARY 24TH 2024
# OOP === OBJECT ORIENTED LANGUAGE//// ALWAYS INITIALIZE YOUR CLASS

# numbers = list()
# numbers.sort
# print(numbers)


# class Dust:
#     def __init__(self, firstName):  #SELF here is a tag that references the clas
        
#         self.creation = 'Human'
#         self.lastName = 'Martin'
#         self.firstName = firstName
        
#         self.walk()
    
#     def walk(self):
#         '''what i do is WALK'''
#         print(f'{self.creation} can walk')

# Solomon = Dust()

# Solomon.walk()

# ====================================================================
class USSD:
    def __init__(self):
        
        # self.home()

    def home(self):
        self.ussd = input('Enter USSD here > ').strip()
        while self.ussd != "*312#":
            print('Invalid Code!')
            self.home()
        self.landingPage()
        
    def landingPage(self):
        print('''
              1. Buy Data
              2. Check Balance
              ''')

ussd = USSD()
self.home()