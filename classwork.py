def land():
    ussdCode = input('Enter the ussd code here: ')
    if ussdCode != '*312#':
        print('Invalid USSD code entered')
        land()
    else:
        offers()


def offers():
    print('''
        Welcome
        
        1. My Offer
        2. My Area
        3. Data Plans
        4. N5000/18GB/30dys
        5. N3000/10GB/30dys
        6. N1500/5GB/7Days
        7. N500/2GB/2Days
        8. SMART DATA PLANS
        9. Family Plans
        99. press for next page
        *
        
        
        ''')

    user = int(input('Select: '))
    if user == 1:
        my_offer()
    elif user == 2:
        area_offer()
    elif user == 3:
        data_plan()
    elif user == 99:
        next_page()
    elif user == '*':
        exit()
    else:
        print('Invalid request enter a valid key')
        offers()
        
                

def my_offer():
    print("""
        My Airtel Offer
        
        1. N500 gives N2500 for calls
        2. N700 gives N3500 for calls
        3. MORE VOICE OFFER
        4. DATA OFFER
        5. RECHARGE OFFER
        22. Back
        0. Menu
                            
        """)
    userOne = int(input('Put a number here: '))
    if userOne == 22:
        offers()
        
def area_offer():
     print('''
        AREA OFFERS
        
        1. N3000/20GB/30days
        2. N5000/40GB/30days
        3. 500/30MINS/1.5GB/7DAYS
        4. 1000/70mins/3GB/15days
        22. Back
        0. menu    
                    
                    ''')
     
     
                
     userTwo = int(input('Put a number here: '))
     if userTwo == 22:
        offers()
    
def data_plan():
     print("""
                    
    1. Daily/Weekly Bundles
    2. Weekly Bundles
    3. Monthly Bundles
    4. More Data (Data++)
    5. Mega Bundles
    6. Big Data Bundles
    *. Next
    22. Back
    0. Menu            
    
                    """)
     
     userThree = int(input('Put a number here: '))
     if userThree == 22:
        offers()
                
def next_page():
    print("""
                                    
    10. Everyday ON
    11. super Binge
    12. Social Bundle
    13. Hourly Plan
    14. Gifting & Sharing                  
    15. Trybe Data Bundles
    16. Data Balance
    0. Main Menu            
                    
                    """)
    userNineNine = int(input('Put a number here: '))
    if userNineNine == 0:
        offers()
    
land()

