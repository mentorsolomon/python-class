# ================ RAGEX FEBRUARY 13TH ==========================
# Regular expressionss called code of codes. powerful tools for pattern macthing and manipulation of strings
# ^ = .startswith 
# \w = varchar
# \d = digit {} curly braces act as a qualifier
# + = one or more occurrence
# \. = matches the literal . symbol
# $ = .endsswith
# r = rawstrings
# # def checkForMail(email):
    # pattern = r'^\w+@\w\.\w\$'

 
import re
import timer

#  1 MATCH
# pattern = r'abc'
# string = 'abc def'
# matche = re.match(pattern, string)
# # if matche:
# #     print('There is a Match')
# # else:
# #     print('No Match')
    
# #  2 SEARCH
# pattern = r'abc'
# string = 'qabc abc def'
# matche = re.search(pattern, string)
# # if matche:
# #     print(matche.group())
# # else:
# #     print('No Match')
    
# #  3 FINDALL()
# pattern = r'\d{3}'
# string = 'I have 233 friends, 101 contacts and 212 girls. 700 wives and 300 concubines'
# matche = re.findall(pattern, string)
# # print(matche)


# ============== CLASSWORK ============
# csv_open = open(r"C:\python-level-two\words\students-grade.csv", mode = "rt")
# data = csv_open.read()
# # print(data)
# match = re.findall(r'(\w+) (\w+),(\d+),(\w)', data)
# # print(match)

# studentDetails = [{
#           'Name': matches[0],
#           'Surname': matches[1],
#           'Score': matches[2],
#           'Grade': matches[3]} 
#           for matches in match]
# print(studentDetails)


# ========================== PRACTICE ============================

def mail():
    mail = input('Email: ').strip()
    match = re.findall(r'\w+@\w+\.\w+', mail)
    if match:
        print('Email created')
        username = mail.strip(r'@\w+\.\w+')
        print(username)
    else:
        print('Incorrect email pattern.')
        mail()
        
    
mail()