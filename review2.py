# import review
#  review.mybank.home()

# ==================== INHERITANCE =============
from revieww import Bank
class NewBank(Bank):
    def __init__(self):
        super().__init__()
        # or
        Bank.__init__(self)
        
        self.name = 'NANO Bank'
        
    
    def withdraw(self):
        pass
    

NewBank = NewBank()
    
print(NewBank.name)
            