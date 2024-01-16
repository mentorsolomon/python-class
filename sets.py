# sets
# JANUARY 2024 CLASS ONE
# =========================================================

# set: A SET IS A COLLECTION WHICH IS UNORDERED, UNINDEXED, IMMUTABLE/UNCHANGEABLE AND DOES NOT ACCEPT DUPLICATE VALUE
# set {} or ()

# name = {"james", "sade", "larry", "gaga", "jerry", "ige"}

# setNames = set(('Muazeem', 'Ige', 'Lado'))

# setNames = ('Muazeem', 'Ige', 'Lado')

sets = set()
print('welcome to set calculator')
print('how many sets are you working with?')
numSets= int(input('no of sets > '))
for name_of_set in range(numSets):
    setItems = input(f'Your set Items {name_of_set + 1}: ')
    sets.update(setItems)
    # 
print(sets)
    


# no_of_setItems = int(input('how many item are in your set?: '))
#     # for setItems in no_of_setItems:
#     #     setItem = int(input('list the numbers in your set: '))
#     # print(setItem)