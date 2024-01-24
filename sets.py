# sets
# JANUARY 2024 CLASS ONE
# =========================================================

# set: A SET IS A COLLECTION WHICH IS UNORDERED, UNINDEXED, IMMUTABLE/UNCHANGEABLE AND DOES NOT ACCEPT DUPLICATE VALUE
# set {} or ()

# name = {"james", "sade", "larry", "gaga", "jerry", "ige"}
# # setNames = set(('Muazeem', 'Ige', 'Lado'))
# setNames = ('Muazeem', 'Ige', 'Lado')
# name.add('jide')
# name.update([6,7,8], setName)
# print(name)

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
    print('Welcome to set calculator'.title().center(100,'*'))
    # sets = set(1, 9, 10, 2, 20, )
    # user = int(input('How many sets are you working with > '))
    # for sets in range(user):
    #     set_entry = input(f'Enter name of Set{sets + 1} >: ')
    #     for set_entries in set_entry:
    #         name = int(input(f'Enter your Set data >: '))
    #         print(name)
    # set().update(set_entries)
    # print(sets)
    
    universalSet = {}
    inputs = int(input('universal set entries are: '))
    for user in range(inputs):
        user = int(input('Enter the items in the Universal set: > '))
        universalSet.update(user)
    print(universalSet)
    data_Items = int(input('How many data Items do you have >: '))
    while data_Items  > 0:
        user = int(input('data entry: '))
        data_Items -= 0
        print(data_Items)
        
        
    
    
home()