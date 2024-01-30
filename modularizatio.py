class USSD:
    def __init__(self):      
        self.network = ''
        self.home()
        
    def home(self):
        self.ussd = input('USSD: ')
        