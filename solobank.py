def home():
    print(" welcome to SOLOBANK. Bank of the New age. ".center(100, "$").title())
    first()


def first():
    print('''
          
          First time user must register.
              Proceed to registration. Press '1'
          '''.strip())
    user = input('Select > ')
    if user != '1':
        print('Error. Try Again')
        first()
    else:
        register()

def register():
    print('Come and register.')
        

    
home()