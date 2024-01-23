# JANUARY 22ND BE MOVING WITH MAD SPEED
# functionS

# ALLOWS SOURCE TO REPEAT ITSELF MULTIPLE TIMES , # object: has a property anc can perform a function

# God[creator], man[creation/object], dust[mode/class].

# you create a function with def i.e function or definition 
# types of functionS
# parametized and unparametized 
# arguments occur inside the parenthesis (argument comes in here)
# ====================================SOLVED EXAMPLES===========================================================
# unparametized
# def addition():
#     """Yo, I add thing up!!"""
    
# addition() #invocation : calling of the created func
# # parametized
# def addition(val1, val2):
#     """Yo, I add thing up!!"""
#     print(val1 + val2)
# # addition(90, 99)

# val1 = int(input("> "))
# val2 = int(input("> "))

# def addition():
    
    
#     print(val1 + val2)
#     subt()
    
# def subt():
#     print(val1 - val2)
    
# addition()
    
# ===========================================
numList = []
def land():
    print('Welcome, what would you like to do?')
    choice = input('add, sub, div, mult, exit: ')
    print(f'you selected the {choice} funtion')
    if choice == 'add':
        add()
    elif choice == 'sub':
        sub() 

    elif choice == 'div':
        div()
    
    elif choice == 'mult':
        mult()
        
    elif choice.lower().strip() == 'exit':
        exit()
        
    else:
        print('error')
        land()

def add():
    '''I add all entries'''
    entry = int(input('How many number do you want to add: '))       
    numList = [int(input(f'\n Enter the number {num + 1}> ')) for num in range(entry)]
    print(f'\n{numList}\n')
    print(sum(numList))
    land()
    
def sub():
    '''I subtract entry 2 from 1: make sure 1 is solely higher else'''
    entry = int(input('How many number do you want to sub: '))       
    numList = [int(input(f'\n Enter the number {num + 1}> ')) for num in range(entry)]
    print(f'\n{numList}\n')
    print((numList[0] - numList[1]))
    land()
def div():
    '''I divide entry 1 by entry 2'''
    entry = int(input('How many number do you want to divide: '))       
    numList = [int(input(f'\n Enter the number {num + 1}> ')) for num in range(entry)]
    print(f'\n{numList}\n')
    print((numList[0] / numList[1]))
    land()

def mult():
    '''I multiply entry 1 and 2'''
    entry = int(input('How many number do you want to multiply: '))       
    numList = [int(input(f'\n Enter the number {num + 1}> ')) for num in range(entry)]
    print(f'\n{numList}\n')
    print(numList[0] * numList[1])
    land()

land()

# tuple = ('james','DAVID','larry')
# print(tuple)
# *l, = tuple
# print(l)

# # ======================================lambda-------------------
# add = lambda x, y: print(x+y)
# add(2,4)

# =======ARGS ABD KWARGS=============================JANUARY 23RD 2024 CLASS WORK===============================
def dealer(product, *toppings, **details): #*args, **kwargs
    print(f'You are about to purchase {product}. You would also be going with:')
    for topping in toppings:
        print(f'--> {topping}')
    
    
    
dealer('Car', ' 2 Tyres', 'Extinguisher', 'Engine Oil', 'Windscreen', model = 'Lexus', Year = 2020, maker = 'Toyota companies')