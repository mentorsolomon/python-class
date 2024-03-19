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