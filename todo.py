toDo = []

print('Here you have your TO-DO LIST'.center(70,'_'))
def land():
    print('''
        1. add to list
        2. Edit Item
        3. Display list
        4. delete item
        5. delete list
        6. exit
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
    elif user == '6' or user == 'exit':
        exit()
    else:
        print('Invalid selection. Try Again')
        land()
        
def add():
    no_of_items = int(input('How many items are you doing today. [1,2,3...10]. Think about it clearly > '))
    for num in range(no_of_items):
        tasks =  input(f'Using Action words, what are you doing today. Task {num + 1}  > ').strip().title()
        toDo.append(tasks)
    land()

def edit():
    print(toDo)
    nums = int(input('Change your to do list at number. > '))
    place = nums - 1
    toDo[place] = input('Enter new item to do: ').title()
    print(toDo)
    land()
    
    # OR 
    # print(toDo)
    # you_edit = input('What do you want to change > ')
    # toDo.index(you_edit) = input('The new entry: ')
    # print(toDo)
    # land()=

def display():
    for every in toDo:
        print(f'\n{every}')
    land()

def del_item():
    remove()
    
    
def remove():
    print(toDo)
    user = input('What will you be removing: ').title().strip()
    if user in toDo:
        toDo.remove(user)
        land()
    else:
        print('Entry not found on List')
        del_item()

def delete():
    toDo.clear()
    print(f"Cleared Successfully. List ({toDo}) is now empty. ")
    land()
    
land()