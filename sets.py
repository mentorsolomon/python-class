# import random

# sets
# JANUARY 2024 CLASS ONE
# =========================================================

# set: A SET IS A COLLECTION WHICH IS UNORDERED, UNINDEXED, IMMUTABLE/UNCHANGEABLE AND DOES NOT ACCEPT DUPLICATE VALUE
# set {} or ()

name = {"james", "sade", "larry", "gaga", "jerry", "ige"}
setName = set(('Muazeem', 'Ige', 'Lado'))
setNames = ('Muazeem', 'Ige', 'Lado')
name.add('jide')
name.update([6,7,8], setName)
print(name)

# sets = set()
# print('welcome to set calculator')
# print('how many sets are you working with?')
# numSets= int(input('no of sets > '))
# for name_of_set in range(numSets):
#     setItems = input(f'Your set Items {name_of_set + 1}: ')
#     sets.update(setItems)
#     # 
# print(f'sets data = {sets}')
# for setItem in setItems:
#     print('how many data does each set item have?')
#     numOfEntriesPerSet = int(input(':> '))
#     setitem = [input(f'your setEntry are: ') for setEntry in setItem]
#     print(setItem)
# print(setItems)
    


# no_of_setItems = int(input('how many item are in your set?: '))
#     # for setItems in no_of_setItems:
#     #     setItem = int(input('list the numbers in your set: '))
#     # print(setItem)





# ===============================SET CALCULATOR==========================================
def home():
    
    # account = random.randint(011111111, 00999999)
    # print(account)
    # name = input(': ')
    # last = input(': ')
    # # for x in range(10):
    # #     y = random.shuffle(name)
    # #     z = random.shuffle(last)
    # email =  name.lower() + last.lower() + '@gmail.com'
    # print(email)

    # for x in range(10):
    #     value = random.randint(1,2)
    #     print(value)
        
    # numbers = [1, 2]
    # selet = random.choices(numbers, weights=[5,2], k=10)
    # print(selet)
    
    # deck = list(range(1, 53))
    # random.shuffle(deck)
    # print(deck)
    # selet = random.sample(deck, k=5)
    # print(selet)
        
        
        # greetings
        
    # greetings = ['Hi', 'Hello', 'Yo', 'Baba nla', 'Howdy', 'Chief', 'Legend', 'Amapiano']
    
    # pick = random.choice(greetings)
    # print(f'{pick} Samuel. Have you eaten?')
    
    # print('Welcome to set calculator'.title().center(100,'*'))
    # # sets = set(1, 9, 10, 2, 20, )
    # # user = int(input('How many sets are you working with > '))
    # # for sets in range(user):
    # #     set_entry = input(f'Enter name of Set{sets + 1} >: ')
    # #     for set_entries in set_entry:
    # #         name = int(input(f'Enter your Set data >: '))
    # #         print(name)
    # # set().update(set_entries)
    # # print(sets)
    
    # universalSet = {}
    # inputs = int(input('universal set entries are: '))
    # for user in range(inputs):
    #     user = int(input('Enter the items in the Universal set: > '))
    #     universalSet.update(user)
    # print(universalSet)
    # data_Items = int(input('How many data Items do you have >: '))
    # while data_Items  > 0:
    #     user = int(input('data entry: '))
    #     data_Items -= 0
    #     print(data_Items)
        
        
    # =========================== max number
    # numbers = [150, 70, 100, 2, 1, 87, 9]
    # max_ = numbers[2]
    # for number in numbers:
    #     if number > max_:
    #         max_ = number
    # print(max_)
    
    #  # =========================== min number
    # numbers = [150, 70, 100, 2, 1, 1, 87, 9]
    # min_ = numbers[2]
    # for number in numbers:
    #     if number < min_:
    #         min_ = number
    # print(min_)
            

    # one = random.randint(1,6)
    # two = random.randint(1,6)
    # roll = one, two
    # # print((roLl))  

    # x = 10
    # y = random.randint(0000000, 99999999)
    # print(f'{x}{y}')
    
    
    # set calculator     
    print('''
          
          Welcome to set Calculator
          
          ''')
    user = input('''
                 What will you like to do today?
                 1. union
                 2. intersection
                 3. difference
                 4. symmetric difference
                 5. Others
                 
                 > ''')
    
    
    if user.strip() == '1':
        union_op()
    elif user.strip() == '2':
        intersection_op()
    elif user.strip() == '3':
        difference_op()   
    elif user.strip() == '4':
        sym_difference()  
    elif user.strip() == '5':
        others()
    else:
        print('Invalid Entry') 
        # comment: 
        
    
    
def union_op():
    operations = int(input('How many sets do you want? '))
    for operation in range( operations):
        for entry in range(operation):
            user = int(input(f'How many data set do you have in {operation}: \n'))
            for num in range(user):
                sets = input(f'enter set{num+1}: ')
                
                
                
                
        
        
          
        
    
    
    
    
home()