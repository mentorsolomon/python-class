toDo = []
import datetime as dt
# import pygame
import time

# song = (r"C:\python-level-two\music\plf.mp3")
# pygame.init()
# pygame.mixer.music.load(song)
# pygame.mixer.music.play()
# time.sleep(60)
# pygame.mixer.music.stop()



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
    elif user == '4' or user == 'delete item':
        del_item()
    elif user == '5' or user == 'delete':
        delete()
    elif user == '6' or user == 'exit':
        exit()
    else:
        print('Invalid selection. Try Again')
        land()
        
def add():
    # no_of_items = int(input('How many items do you want todo today. [1,2,3...10]> '))
    # toDo =[input(f'Enter Tasks. Task {num +1}>> ') for num in range(no_of_items)]
    # # for num in range(no_of_items):
    # #     tasks =  input(f'Enter Tasks. Task {num +1}  > ').strip().title()
    # #     toDo.append(tasks)
    # land()
    # ================
    while True:
        tasks = input(f"Input Task. (Press 'S' to stop adding task): ").strip().lower()          
        if tasks == 's':
            land()
        
        toDo.append(tasks)           
           
def edit():
    print(toDo)
    nums = int(input('Change your to do list at number. > '))
    place = nums - 1
    toDo[place] = input('Enter new task to do: ').lower()
    print(f'You edited your ToDo successfully.')
    land()
   
   
def display():
    for every in toDo:
        print(f'\n{every}')
    land()

def del_item():
    print(toDo)
    user = input('What do you want to remove? : ').strip()
    toDo.remove(user)
    print(f'Item removed successfully. List Update to date.')
    land()

def delete():
    toDo.clear()
    print(f"Cleared Successfully. List is now empty. {toDo}")
    print("Select 'add' or '1' to add new tasks to your TODO.")
    land()
    
home()

# ==========================correction==========================
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