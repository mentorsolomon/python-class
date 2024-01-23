toDo = []

print('Here you have your TO-DO LIST'.center(70,'_'))
def land():
    print('''
        1. add to list
        2. Edit Item
        3. Display list
        4. delete item
        5. delete list
            ''')
    user = input('What do you want to do?: >').strip().lower()
    if user == '1' or user == 'add':
        add()
    elif user == '2' or user == 'edit':
        edit()
    elif user == '3' or user == 'display':
        display()
    elif user == '4' or user == 'remove':
        del_item()
    elif user == '5' or user == 'delete':
        delete()
    
    
def add():
    user = input('Using Action words, what are you doing today > ')
    toDo.append(user)
    # print(toDo)
    land()

def edit():
    print(toDo)
    print('what will you like to edit')
    user = input()
    land()

def display():
    print(toDo)
    land()

def del_item():
    toDo.remove


def delete():
    toDo.clear()
    print(toDo)
    
    
land()