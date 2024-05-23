# ===========JANUARY 15TH===========================
# TUPPLE IS A COLLECTION WHICH IS ORDERED, UNCHANGEABLE, ALLOWS DUPLICATE VALUE, ITEMS ARE INDEXED.


# myTuple = ('shade', 'dare', 'james', 'emma', 'lanre', True, False, 12 )
# print(myTuple)

# myTuple2 = tuple(('shade', 'dare', 'magret', "femo"))
# print(myTuple2)

# it_is_a_tuple = ("yam",)
# print(type(it_is_a_tuple))

# it_is_not_a_tuple = ("yam")
# print(type(it_is_not_a_tuple))

# x = list(myTuple)
# x[3] = 'femi'
# myTuple = tuple(x)
# print(myTuple)

# (*x,) = myTuple #unpacking a tuple turns it into a LIST
# print(x)

# (y, *x,) = ('yemi', 'david', 'james', 'emma', 'lanre')
# print(y)
# (*x, y,) = ('yemi', 'david', 'james', 'emma', 'lanre')
# print(y)

# ========================================
# day two

# student_record = [
#                   ('G-Wagon', '$1M'),
#                   ('lexus 2012', '#2m'),
#                   ('ferrari', '$1.5m')
#                   ]

# print(student_record[0][1])
# for carName, carPrice in student_record:
#     print(carName, carPrice)


# =======================================

# list_items = (
#                 ('Blessing', 23, 'Kaduna'),
#                 ('Tehya', 21, 'Modakeke'),
#                 ('Tolashe', 20, 'Ogbomoso'),
#                 ('Solomon', 25, 'Osogbo')
#                 )

# for _, mango, _, _ in list_items:
#     pass
# item1, item2, item3, item4 = list_items  
# # print(item4)
# for name, age, place in list_items: #for _, mango, _, _ in list_items: shorthand way of calling LHS
#         print(f"{name} is God's.")

# ====================================================================================

list_set = list()
set_items = int(input('How many sets do you have: ').strip())

for sets in range(set_items):
    items =  int(input(f'How many item are in your Set{sets+1}: ').strip())
    item = list()
    item_count = 1

    for data in range(items):
        data_item = int(input(f'Item{item_count}: ').strip())
        item.append(data_item)
        item_count+=1
    
    list_set.append(set(item))

# print(list_set)

list_count = 1

for entries in list_set:
    print(f'''
    Set{list_count} = {entries}
    ''')
    list_count+=1

user = input('''
    What do you want to do?

    1. Union
    2. Intersection
    3. Difference
    4. Symmetric difference
    5. Others
    6. Exit

''').strip()

if user == '1':
    setA = list_set[(int(input('Which number is your setA: ').strip()))- 1]
    setB = list_set[(int(input('Which number is your setB: ').strip()))- 1]
    
    print(f'''
    {setA} union {setB} = {setA | setB}
    ''')


elif user == '2':
    setA = list_set[(int(input('Which number is your setA: ').strip()))- 1]
    setB = list_set[(int(input('Which number is your setB: ').strip()))- 1]
    
    print(f'''
    {setA} intersection {setB} = {setA & setB}
    ''')


elif user == '3':
    setA = list_set[(int(input('Which number is your setA: ').strip()))- 1]
    setB = list_set[(int(input('Which number is your setB: ').strip()))- 1]
    
    print(f'''
    {setA} difference {setB} = {setA - setB}
    ''')

elif user == '4':
    setA = list_set[(int(input('Which number is your setA: ').strip()))- 1]
    setB = list_set[(int(input('Which number is your setB: ').strip()))- 1]
    
    print(f'''
    {setA} symmmetric_difference {setB} = {setA ^ setB}
    ''')

elif user == '5':
    setA = list_set[(int(input('Which number is your setA: ').strip()))- 1]
    setB = list_set[(int(input('Which number is your setB: ').strip()))- 1]
    


elif user == '6':
    exit()

else:
    print('Invalid command.')