toDo = []

print('Here you have your TO-DO LIST'.center(70,'_'))
def home():
    print('''
          1. Create a List
          2. Exit
          ''')
    user = input(' What is it you want to do > ')
    if user == '1':
        add()
    elif user == '2':
        exit()
    else:
        print('Try Again.')
        home()


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
    
home()

# ==========================correctio==========================
# def toDo():
#     print('''
#           My ToDo APP
          
#     1. Create ToDo
#     2. Exit
          
#           ''')
#     choice = input('Option: ')
#     if choice == '1':
#        todoList = []
#        create(todoList)
#     elif choice == '2':
#         exit()
#     else:
#         print('Invalid Input. Try Again')
#         toDo()
    
# def create(value:list):
#     # global todoList
#     # todoList = []
#     while True:
#         user = input("Input Task. (Press '1' to stop adding task): ").strip()
#         if user == '1':
#             home(value)
            
#         value.append(user)
    

# def home(values:list):
#     print('''
#           1. View Todo
#           2. Edit Item in Todo
#           3. Delete Item in Todo
#           4. Delete Todo
#           5. Add to Todo
                    
#           ''')    
#     user = input('Option > ')
#     if user == '1':
#         for num, value in enumerate(values, start=1):
#             print(f'''
#                   {num}. {value}
#                   ''')
#         home(values)
#     elif user == '5':
#         create(values)  
        
#     elif user =='00':
#         exit()
    
# toDo()