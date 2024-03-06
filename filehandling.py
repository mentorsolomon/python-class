# Operations that can be performed on a file 

# file = open(r"C:\\words\\A", mode = "r")
# for line in file.readlines():
#     # val = line.split(',')
#     print(line)
# print(file.read())
# file.close() #Always close your file
# file_list.pop(0)

# ================ THE WAY TO OPEN A FILE =====================================

# how to open a file without worrying about closing it
# with open(r"") as file:
#     print(file.read())

# ====================CREATE =======================================

# myFile = open("c:\\python-level-two\\", mode='x')
# print('File created.')

# # APPEND MODE=========================
# myFile = open(r"C:\python-level-two\text.docx",mode = "a")
# myFile.write('James my boy')

# # WRITE MODE=========================
# myFile = open(r"C:\python-level-two\text.docx",mode = "w")
# myFile.write('James my boy')

# # delete

# myFile.

# =========================== FEBRUARY 2023, 13TH ====================
# ============================  OS  ===================
import os 
import time

# os.exists
# os.remove
# os.rmdir

# creatting a directory with os module
# os.mkdir = make directory and then you add the path in the parenthesis


# os.mkdir("C:\\python-level-two\\newWORK")
# myFile = open("C:\\python-level-two\\newWORK\\text.txt", mode = "x")
# new = open(r"C:\\python-level-two\\newWORK\\texts.py", mode = "x")
    
    
#===================== deleting a directory ===========================================

# try:
#     os.rmdir("C:\\python-level-two\\newWORK")
# except OSError:
#     print('The folder is not empty.')
#     # print(os.walk("C:\\python-level-two\\newWORK"))
#     for root, folder, files in os.walk("C:\\python-level-two\\newWORK"):
#         print(files)
        
#         for inside in (files):
#             print('Deleting', inside)
#             time.sleep(3)
#             os.remove("C:\\python-level-two\\newWORK\\" +inside)
    
#     print('Deleting Directory')
#     time.sleep(1)
#     os.rmdir("C:\\python-level-two\\newWORK")
    
# ================================ making directory =================================================
# os.mkdir("C:\\python-level-two\\ROOTdir")
# os.mkdir("C:\\python-level-two\\ROOTdir\\dir1")

# files = open("C:\\python-level-two\\ROOTdir\\text.txt", mode = "x")
# new = open("C:\\python-level-two\\ROOTdir\dir1\\texts.py", mode = "x")

try:
    os.rmdir("C:\\python-level-two\\ROOTdir") 
except OSError:
    print('The folder contains information.')
    # print(os.walk("C:\\python-level-two\\ROOTdir"))
    for root, folder, files in os.walk("C:\\python-level-two\\ROOTdir"):
        print(folder, files)
        
        for inside in folder:
            for outside in files:
                time.sleep(2)
                print(outside)
                os.rmdir("C:\\python-level-two\\ROOTdir\\" +inside)
            print('Deleting Directory')
            time.sleep(1)
            os.rmdir("C:\\python-level-two\\\\ROOTdir\\" +outside)
        
    print('Deleting Directory')
    time.sleep(1)
    os.rmdir("C:\\python-level-two\\ROOTdir")
            
        


# ======================== TO DO =========================

# print('Folder created successfully.')
# for root, folder, filess in os.walk("C:\\python-level-two\\ROOTdir"):   
#     print(filess)   


# print(os.path.exists(r"C:\python-level-two\words\president-height.csv"))

# ==================================ASSIGNMENT ===========================================================
# names = []
# numbers = []
# heights = []
# full = []
# try:
#     with open(r"C:\python-level-two\words\president-height.csv", mode = "rt") as myFile:
#         # print(myFile.read())
#         for line in myFile.readlines():
#             lines = line.split(",")
#             number = lines[0]
#             name = lines[1].strip()
#             height = lines[2].strip(r'\n')
#             numbers.append(number)
#             names.append(name)
#             heights.append(height)
#             full.append(lines)
#             print(lines) 
# except FileNotFoundError:
#     print('Check the name and retry.')

# numbers.pop(0)
# names.pop(0)
# heights.pop(0)
# full.pop(0)

# for x, y, z in full:
#     # print(x,y,z)
#     pass
 
# maxHeight = max(heights)
# minHeight = min(heights)

# indexMaxHeights = heights.index(maxHeight)
# indexMinHeights = heights.index(minHeight)

# # presidentMax = names[indexMaxHeights]

# index = 0
# for x in heights:
#     if x == maxHeight:
#         print(name[index])
#     index += 1
#     # print(f'\n{name[index]} is the president with max height of {maxHeight}')


# presidentMin = names[indexMinHeights]
# print(f'{presidentMin} is the president with min height of {minHeight}')


# ======================  STUDENTS AND GRADES  =====================
# import time
# names = []
# scores = []
# grades = []

# try:
#     with open(r"C:\python-level-two\words\students-grade.csv", mode = "rt") as my_file:
#         # print(my_file.readlines())
#         for entries in my_file.readlines():
#             # print(f"{entries}\n")
#             entry = entries.split(",")
#             name = entry[0].strip()
#             score = entry[1].strip()
#             grade = entry[2]. strip("\n")
            
#             names.append(name)
#             scores.append(score)
#             grades.append(grade)  
                                 
# except FileNotFoundError:
#     print('Check the locator and try again.')
    
# names.pop(0)
# print('Student Names'.center(50, "_"))
# for i in names:
#     # print(i)
#     pass
# print("\n")


# scores.pop(0)
# # print('Scores'.center(40, '_'))
# # for j in scores:
# #     print(j)
# # print("\n")
     

# grades.pop(0)
# print('Grades'.center(40, '_'))
# for k in grades:
#     # print(k)
#     pass
    
# # print("\n")

# for x,y,z in zip(names, scores, grades):
#     pass 
#     # print(y)
# print('\n')
# ===========================

# index = 0
# for x in heights:
#     if x == maxHeight:
#         print(name[index])
#     index += 1

# ================================ names of students ==============================

# max_score = max(scores)
# index_max = scores.index(max_score)
# min_score = min(scores)
# index_min = scores.index(min_score)

# print(f'{names[index_min]} score the lowest score of {min_score}')
# print('\n')
# print(f'{names[index_max]} score the highest score of {max_score}') 
# print('\n')




# ================ check results ========================
# def land():
#     print('You can now check your results.')
#     check()
    
    
# def check():
#     check = input('Enter Name of candidate: ').title()
#     if check not in names:
#         print('name not found')
#         check()
#     else:
#         indexCheck = names.index(check)
#         studentScore = scores[indexCheck]
#         studentScore = int(studentScore)
#         print('Getting info...')
#         time.sleep(2)
#         print(f"{check} scored {studentScore}")
        
#         if studentScore == 100:
#             print(f'''Excellent. Exceptional Performance {check}. Congratulations, You have secured yourself a place at the battle of the champions  \n''')
            
#         elif studentScore >= 70:
#             print(f'Excellent. Satisfactory Performance {check}. Congratulations  \n')
    
#         elif studentScore >=60:
#             print(f' Very Good. Satisfactory Performance {check}. Congratulations  \n')
            
#         elif studentScore >=50:
#             print(f'Good. Satisfactory Performance {check}. Congratulations  \n')
            
#         elif studentScore >=40:
#             print(f'Poor. Satisfactory Performance {check}. Congratulations \n')
            
#         elif studentScore >=0:
#             print(f'Fail. Satisfactory Performance {check}. BEST OF LUCK NEXT TIME  \n')
            
#         else:
#             print('Score record not found')
    
#         land()
                
# land()