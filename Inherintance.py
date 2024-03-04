class PARENT:
    def __init__(self):
        self.surname = 'Adedokun'
        self.firstname = 'Solomon'
        self.hobby = 'Colding'

        # self.describe()

    def describe(self):
        print(f'My name is {self.firstname} {self.surname}. I love {self.hobby}.')



parent = PARENT()
parent.describe()


# ============================= INHERITANCE  ===========================================
# MARCH 4TH

class CHILD(PARENT):
    def __init__(self):
        PARENT.__init__(self)
        # or
        super().__init__()
        self.firstname = 'James'
        self.hobby = 'Fishing'

        # self.describe()

    def playing(self):
        print(f'I {self.firstname} loves food')


# child = CHILD()

class GrandChild(CHILD):
    def __init__(self):
        CHILD.__init__(self)
        self.firstname = 'Emmanuel'
        self.hobby = 'Twerking'

        # self.describe()


grandchild = GrandChild()


# =============================

# from time import sleep
# sleep(3)

# import time
# time.sleep(3)




