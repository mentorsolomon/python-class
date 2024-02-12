# Operations that can be performed on a file 

# file = open(r"c:")
# for line in file.readlines():
#     val = line.split(',')
#     print(line)
# print(file.read())
# file.close() #Always close your file
# file_list.pop(0)

# how to open a file without worrying about closing it ++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# with open(r"") as file:
#     print(file.read())

# ====================CREATE =======================================

# myFile = open("c:\\python-level-two\\", mode='x')
# print('File created.')

# APPEND MODE=========================
myFile = open(r"C:\python-level-two\text.docx",mode = "a")
myFile.write('James my boy')

# WRITE MODE=========================
myFile = open(r"C:\python-level-two\text.docx",mode = "w")
myFile.write('James my boy')