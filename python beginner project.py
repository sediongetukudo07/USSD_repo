"""
# PYTHON PROJECT

1) USSD application
2) Tetris game
3) Calculator
"""

# USSD application
while True:
    code = input("")
    if code == "*141#":
        print("""
        1) My Offer
        2) My Area
        3) Data Bundle
        4) N5000/22GB/30 days
        5) N3000/11GB/30 days
        6) N1500/6GB/7 days
        7) N500/2.5GB/2 days
        8) Family Plan
        * Next
        """)
        while True:
            option = input("")
            if option == "1":
                print('''
                My Airtel Offer
                1) N500/2.5GB/2 days
                2) N1000/5GB/14 days
                3) MORE DATA OFFER
                4) VOICE OFFER
                5) RECHARGE OFFER
                22 Back
                0 Menu
                ''')
                while True:
                    option_1 = input("")
                    if option_1 == "1":
                        print('''
                        2.5GB/2 days for N500
                        1) Activate
                        2) Cancel
                        22 Back
                        0 Menu
                        ''')
                        while True:
                            e = input("")
                            if e == "1":
                                print('''
                                You have successfully purchased 2.5GB plan
                                ''')
                            elif e == "2":
                                exit()
                    elif option_1 == "2":
                        print('''
                        5GB/14 days for N1000
                        1) Activate
                        2) Cancel
                        22 Back
                        0 Menu
                        ''')
                        while True:
                            e = input("")
                            if e == "1":
                                print('''
                                You have successfully purchased 5GB plan
                                ''')
                            elif e == "2":
                                 exit()
                    elif option_1 == "3":
                        print('''
                        1) N500/2.5GB/2 days
                        2) N1000/5GB/14 days
                        3) N2000/9GB/30 days
                        22 Back
                        0 Menu
                        ''')
                        while True:
                            u = input("")
                            if u == "1":
                                print('''
                                2.5GB/2days for N500
                                1) Activate
                                2) Cancel
                                22 Back
                                0 Menu
                                ''')
                                while True:
                                    e = input("")
                                    if e == "1":
                                        print('''
                                        You have successfully purchased 2.5GB plan
                                        ''')
                                    elif e == "2":
                                        exit()
                                    else:
                                        print('''
                                        Invalid Request
                                        2.5GB/2days for N500
                                        1) Activate
                                        2) Cancel
                                        22 Back
                                        0 Menu
                                        ''')
                            elif u == "2":
                                print('''
                                5GB/14days for N1000
                                1) Activate
                                2) Cancel
                                22 Back
                                0 Menu
                                ''')
                                while True:
                                    e = input("")
                                    if e == "1":
                                        print('''
                                        You have successfully purchased 5GB plan
                                        ''')
                                    elif e == "2":
                                        exit()
                                    else:
                                        print('''
                                        Invalid Request
                                        5GB/14days for N1000
                                        1) Activate
                                        2) Cancel
                                        22 Back
                                        0 Menu
                                        ''')
                            elif u == "3":
                                print('''
                                9GB/30days for N2000
                                1) Activate
                                2) Cancel
                                22 Back
                                0 Menu
                                ''')
                                while True:
                                    e = input("")
                                    if e == "1":
                                        print('''
                                        You have successfully purchased 9GB plan
                                        ''')
                                    elif e == "2":
                                        exit()
                                    else:
                                        print('''
                                        Invalid Request
                                        9GB/30days for N2000
                                        1) Activate
                                        2) Cancel
                                        22 Back
                                        0 Menu
                                        ''')
                    elif option_1 == "4":
                        print('''
                        1) N200 gives N1000 for calls
                        2) N300 gives N1500 for calls
                        3) N500 gives N2500 for calls
                        22 Back
                        0 Menu
                        ''')
                        while True:
                            y = input("")
                            if y == "1":
                                print('''
                                N200 gives N1000 for calls & SMS / 30 days
                                1) Activate
                                2) Cancel
                                22 Back
                                0 Menu
                                ''')
                                while True:
                                    a = input("")
                                    if a == "1"
                                        print('''
                                        You have b
                                        ''')
                            elif y == "2":
                                print('''
                                N300 gives N1500 for calls & SMS / 30 days
                                1) Activate
                                2) Cancel
                                22 Back
                                0 Menu
                                ''')
                            elif y == "3":
                                print('''
                                N500 gives N2500 for calls & SMS / 30 days
                                1) Activate
                                2) Cancel
                                22 Back
                                0 Menu
                                ''')
                    elif option_1 == "5":
                        print('''
                        Recharge via Smartcash and get 100 BONUS 
                        airtime. Dial *939# to open a Smartcash wallet and recharge your Airtel line
                        ''')
                    else:
                        print('''
                        Invalid Request
                        My Airtel Offer
                        1) N500/2.5GB/2 days
                        2) N1000/5GB/14 days
                        3) MORE DATA OFFER
                        4) VOICE *141#
                        5) RECHARGE OFFER
                        22 Back
                        0 Menu
                        * Next''')

            elif option == "2":
                print('''
                1) N200/400MB/3days
                2) N3000/20GB/30days
                3) N5000/40GB/30days
                4) 500/30MINS/1.5GB
                5) Umunna: 1000/70mins/3GB/15days
                22 Back
                0 Menu
                ''')
                while True:
                    option_2 = input("")
                    if option_2 == "1":
                        print('''
                        400MB for 3days at N200. After your plan finishes?
                        1) Continue browsing from airtime/ 160MB
                        2) Stop my Data
                        22 Back
                        0 Menu
                        ''')
                        while True:
                            b = input("")
                            if b == "1":
                                print('''
                                Payment Option
                                1) Airtime
                                2) Smartcash + 20% more
                                22 Menu
                                0 Menu
                                ''')
                                cz = input("")
                                if cz == "1":
                                    print('''
                                    You have successfully purchased 100MB data plan
                                    ''')
                                elif cz == "2":
                                    print('''
                                    Please enter Smartcash PIN
                                    ''')
                            elif b == "2":
                                print('''
                                Payment Option
                                1) Airtime
                                2) Smartcash + 20% more
                                22 Back
                                0 Menu
                                ''')
                                cz = input("")
                                if cz == "1":
                                    print('''
                                    You have successfully purchased 100MB data plan
                                    ''')
                                elif cz == "2":
                                    print('''
                                    Please enter Smartcash PIN
                                    ''')
            elif option == "3":
                print('''
                1) Daily/Weekly Bundles
                2) Weekly Bundles
                3) Monthly Bundles
                4) More Data (Data++)
                5) Mega Bundles
                6) Big Data Plans
                * Next
                22 Back
                0 Menu
                ''')
                while True:
                    option_3 = input("")
                    if option_3 == "1":
                        print('''
                        1) N50/40MB/Daily
                        2) N100/100MB/Daily
                        3) N200/200MB/3dys
                        4) N300/350MB/7dys
                        5) N500/750MB/14Days
                        6) N300/1GB/Daily
                        7) N500/2GB/Daily
                        * Next
                        22 Back
                        0 Menu
                        ''')
                        while True:
                            option_4 = input("")
                            if option_4 == "1":
                                print('''
                                40MB for 1day at N50. What should happen 
                                when your bundle finishes?
                                1) Continue browsing from airtime/ 160MB
                                2) Stop my Data
                                22 Back
                                0 Menu
                                ''')
                                while True:
                                    a = input("")
                                    if a == "1":
                                        print('''
                                        Payment Option
                                        1) Airtime
                                        2) Smartcash + 20% more
                                        22 Back
                                        0 Menu
                                        ''')
                                        cz = input("")
                                        if cz == "1":
                                            print('''
                                            You have successfully purchased 40MB data plan
                                            ''')
                                        elif cz == "2":
                                            print('''
                                            Please enter Smartcash PIN
                                            ''')
                                    elif a == "2":
                                        print('''
                                        Payment Option
                                        1) Airtime
                                        2) Smartcash + 20% more
                                        22 Back
                                        0 Menu
                                        ''')
                                        cz = input("")
                                        if cz == "1":
                                            print('''
                                            You have successfully purchased 40MB data plan
                                            ''')
                                        elif cz == "2":
                                            print('''
                                            Please enter Smartcash PIN
                                            ''')
                            elif option_4 == "2":
                                print('''
                                100MB for 1day at N100. What should happen 
                                when your bundle finishes?
                                1) Continue browsing from airtime/ 160MB Extra
                                2) Stop my Data
                                22 Back
                                0 Menu
                                ''')
                                while True:
                                    b = input("")
                                    if b == "1":
                                        print('''
                                        Payment Option
                                        1) Airtime
                                        2) Smartcash + 20% more
                                        22 Menu
                                        0 Menu
                                        ''')
                                        cz = input("")
                                        if cz == "1":
                                            print('''
                                            You have successfully purchased 100MB data plan
                                            ''')
                                        elif cz == "2":
                                            print('''
                                            Please enter Smartcash PIN
                                            ''')
                                    elif b == "2":
                                        print('''
                                        Payment Option
                                        1) Airtime
                                        2) Smartcash + 20% more
                                        22 Back
                                        0 Menu
                                        ''')
                                        cz = input("")
                                        if cz == "1":
                                            print('''
                                            You have successfully purchased 100MB data plan
                                            ''')
                                        elif cz == "2":
                                            print('''
                                            Please enter Smartcash PIN
                                            ''')
                            elif option_4 == "3":
                                print('''
                                200MB for 3days at N200. What should happen 
                                when your bundle finishes?
                                1) Continue browsing from airtime/ 160MB Extra
                                2) Stop my Data
                                22 Back
                                0 Menu
                                ''')
                                while True:
                                    c = input("")
                                    if c == "1":
                                        print('''
                                        Payment Option
                                        1) Airtime
                                        2) Smartcash + 20% more
                                        22 Back
                                        0 Menu
                                        ''')
                                        cz = input("")
                                        if cz == "1":
                                            print('''
                                            You have successfully purchased 200MB data plan
                                            ''')
                                        elif cz == "2":
                                            print('''
                                            Please enter Smartcash PIN
                                            ''')
                                    elif c == "2":
                                        print('''
                                        Payment Option
                                        1) Airtime
                                        2) Smartcash + 20% more
                                        22 Back
                                        0 Menu
                                        ''')
                                        cz = input("")
                                        if cz == "1":
                                            print('''
                                            You have successfully purchased 200MB data plan
                                            ''')
                                        elif cz == "2":
                                            print('''
                                            Please enter Smartcash PIN
                                            ''')
                            elif option_4 == "4":
                                print('''
                                350MB for 7days at N300. What should happen 
                                when your bundle finishes?
                                1) Continue browsing from airtime/ 160MB Extra
                                2) Stop my Data
                                22 Back
                                0 Menu
                                ''')
                                while True:
                                    d = input("")
                                    if d == "1":
                                        print('''
                                        Payment Option
                                        1) Airtime
                                        2) Smartcash + 20% more
                                        22 Back
                                        0 Menu
                                        ''')
                                        az = input("")
                                        if az == "1":
                                            print('''
                                            You have successfully purchased 350MB data plan
                                            ''')
                                        elif az == "2":
                                            print('''
                                            Please enter Smartcash PIN
                                            ''')
                                    elif d == "2":
                                        print('''
                                        Payment Option
                                        1) Airtime
                                        2) Smartcash + 20% more
                                        22 Back
                                        0 Menu
                                        ''')
                                        bz = input("")
                                        if bz == "1":
                                            print('''
                                            You have successfully purchased 350MB data plan
                                            ''')
                                        elif bz == "2":
                                            print('''
                                            Please enter Smartcash PIN
                                            ''')
                            elif option_4 == "5":
                                print('''
                                750MB for 14days at N500. What should happen 
                                when your bundle finishes?
                                1) Continue browsing from airtime/ 160MB Extra
                                2) Stop my Data
                                22 Back
                                0 Menu
                                ''')
                                while True:
                                    e = input("")
                                    if e == "1":
                                        print('''
                                        Payment Option
                                        1) Airtime
                                        2) Smartcash + 20% more
                                        22 Back
                                        0 Menu
                                        ''')
                                        cz = input("")
                                        if cz == "1":
                                            print('''
                                            You have successfully purchased 750MB data plan
                                            ''')
                                        elif cz == "2":
                                            print('''
                                            Please enter Smartcash PIN
                                            ''')
                                    elif e == "2":
                                        print('''
                                        Payment Option
                                        1) Airtime
                                        2) Smartcash + 20% more
                                        22 Back
                                        0 Menu
                                        ''')
                                        cz = input("")
                                        if cz == "1":
                                            print('''
                                            You have successfully purchased 750MB data plan
                                            ''')
                                        elif cz == "2":
                                            print('''
                                            Please enter Smartcash PIN
                                            ''')
                            elif option_4 == "6":
                                print('''
                                1GB for 1day at N300. What should happen 
                                when your bundle finishes?
                                1) Continue browsing from airtime/ 160MB Extra
                                2) Stop my Data
                                22 Back
                                0 Menu
                                ''')
                                while True:
                                    e = input("")
                                    if e == "1":
                                        print('''
                                        Payment Option
                                        1) Airtime
                                        2) Smartcash + 20% more
                                        22 Back
                                        0 Menu
                                        ''')
                                        cz = input("")
                                        if cz == "1":
                                            print('''
                                            You have successfully purchased 1GB data plan
                                            ''')
                                        elif cz == "2":
                                            print('''
                                            Please enter Smartcash PIN
                                            ''')
                                    elif e == "2":
                                        print('''
                                        Payment Option
                                        1) Airtime
                                        2) Smartcash + 20% more
                                        22 Back
                                        0 Menu
                                        ''')
                                        cz = input("")
                                        if cz == "1":
                                            print('''
                                            You have successfully purchased 1GB data plan
                                            ''')
                                        elif cz == "2":
                                            print('''
                                            Please enter Smartcash PIN
                                            ''')
                            elif option_4 == "7":
                                print('''
                                2GB for 1day at N500. What should happen 
                                when your bundle finishes?
                                1) Continue browsing from airtime/ 160MB Extra
                                2) Stop my Data
                                22 Back
                                0 Menu
                                ''')
                                while True:
                                    e = input("")
                                    if e == "1":
                                        print('''
                                        Payment Option
                                        1) Airtime
                                        2) Smartcash + 20% more
                                        22 Back
                                        0 Menu
                                        ''')
                                        cz = input("")
                                        if cz == "1":
                                            print('''
                                            You have successfully purchased 2GB data plan
                                            ''')
                                        elif cz == "2":
                                            print('''
                                            Please enter Smartcash PIN
                                            ''')
                                    elif e == "2":
                                        print('''
                                        Payment Option
                                        1) Airtime
                                        2) Smartcash + 20% more
                                        22 Back
                                        0 Menu
                                        ''')
                                        cz = input("")
                                        if cz == "1":
                                            print('''
                                            You have successfully purchased 2GB data plan
                                            ''')
                                        elif cz == "2":
                                            print('''
                                            Please enter Smartcash PIN
                                            ''')
                            else:
                                print('''
                                Invalid Request
                                1) N50/40MB/Daily
                                2) N100/100MB/Daily
                                3) N200/200MB/3dys
                                4) N300/350MB/7dys
                                5) N500/750MB/14Days
                                6) N300/1GB/Daily
                                7) N500/2GB/Daily
                                * Next
                                22 Back
                                0 Menu
                                ''')
                    elif option_3 == "2":
                        print('''
                        Weekly Bundles
                        1) N500/750MB/14Days
                        2) N500/1GB/7days
                        3) N1500/6GB/7days
                        4) N300/350MB/7dys
                        5) N100/All Social/5 days
                        22 Back
                        ''')
                        while True:
                            option_5 = input("")
                            if option_5 == "1":
                                print('''
                                750MB for 14days at N500. After your plan 
                                finishes?
                                1) Continue browsing from airtime/ 160MB Extra
                                2) Stop my Data
                                22 Back
                                0 Menu
                                ''')
                                while True:
                                    e = input("")
                                    if e == "1":
                                        print('''
                                        Payment Option
                                        1) Airtime
                                        2) Smartcash + 20% more
                                        22 Back
                                        0 Menu
                                        ''')
                                        cz = input("")
                                        if cz == "1":
                                            print('''
                                            You have successfully purchased 750MB weekly plan data plan
                                            ''')
                                        elif cz == "2":
                                            print('''
                                            Please enter Smartcash PIN
                                            ''')
                                    elif e == "2":
                                        print('''
                                        Payment Option
                                        1) Airtime
                                        2) Smartcash + 20% more
                                        22 Back
                                        0 Menu
                                        ''')
                                        cz = input("")
                                        if cz == "1":
                                            print('''
                                            You have successfully purchased 750MB weekly data plan
                                            ''')
                                        elif cz == "2":
                                            print('''
                                            Please enter Smartcash PIN
                                            ''')
                            elif option_5 == "2":
                                print('''
                                1GB for 7days at N500. After your plan 
                                finishes?
                                1) Continue browsing from airtime/ 160MB Extra
                                2) Stop my Data
                                22 Back
                                0 Menu
                                ''')
                                while True:
                                    e = input("")
                                    if e == "1":
                                        print('''
                                        Payment Option
                                        1) Airtime
                                        2) Smartcash + 20% more
                                        22 Back
                                        0 Menu
                                        ''')
                                        cz = input("")
                                        if cz == "1":
                                            print('''
                                            You have successfully purchased 1GB weekly data plan
                                            ''')
                                        elif cz == "2":
                                            print('''
                                            Please enter Smartcash PIN
                                            ''')
                                    elif e == "2":
                                        print('''
                                        Payment Option
                                        1) Airtime
                                        2) Smartcash + 20% more
                                        22 Back
                                        0 Menu
                                        ''')
                                        cz = input("")
                                        if cz == "1":
                                            print('''
                                            You have successfully purchased 1GB weekly data plan
                                            ''')
                                        elif cz == "2":
                                            print('''
                                            Please enter Smartcash PIN
                                            ''')
                            elif option_5 == "3":
                                print('''
                                6GB for 7days at N1500. After your plan 
                                finishes?
                                1) Continue browsing from airtime/ 160MB Extra
                                2) Stop my Data
                                22 Back
                                0 Menu
                                ''')
                                while True:
                                    e = input("")
                                    if e == "1":
                                        print('''
                                        Payment Option
                                        1) Airtime
                                        2) Smartcash + 20% more
                                        22 Back
                                        0 Menu
                                        ''')
                                        cz = input("")
                                        if cz == "1":
                                            print('''
                                            You have successfully purchased 6GB weekly data plan
                                            ''')
                                        elif cz == "2":
                                            print('''
                                            Please enter Smartcash PIN
                                            ''')
                                    elif e == "2":
                                        print('''
                                        Payment Option
                                        1) Airtime
                                        2) Smartcash + 20% more
                                        22 Back
                                        0 Menu
                                        ''')
                                        cz = input("")
                                        if cz == "1":
                                            print('''
                                            You have successfully purchased 6GB weekly data plan
                                            ''')
                                        elif cz == "2":
                                            print('''
                                            Please enter Smartcash PIN
                                            ''')
                            elif option_5 == "4":
                                print('''
                                350MB for 7days at N300. After your plan 
                                finishes?
                                1) Continue browsing from airtime/ 160MB Extra
                                2) Stop my Data
                                22 Back
                                0 Menu
                                ''')
                                while True:
                                    d = input("")
                                    if d == "1":
                                        print('''
                                        Payment Option
                                        1) Airtime
                                        2) Smartcash + 20% more
                                        22 Back
                                        0 Menu
                                        ''')
                                        az = input("")
                                        if az == "1":
                                            print('''
                                            You have successfully purchased 350MB data plan
                                            ''')
                                        elif az == "2":
                                            print('''
                                            Please enter Smartcash PIN
                                            ''')
                                    elif d == "2":
                                        print('''
                                        Payment Option
                                        1) Airtime
                                        2) Smartcash + 20% more
                                        22 Back
                                        0 Menu
                                        ''')
                                        bz = input("")
                                        if bz == "1":
                                            print('''
                                            You have successfully purchased 350MB data plan
                                            ''')
                                        elif bz == "2":
                                            print('''
                                            Please enter Smartcash PIN
                                            ''')
                            elif option_5 == "5":
                                print('''
                                All Social for 5days at N100. What should happen 
                                when your bundle finishes?
                                1) Continue browsing from airtime/ 160MB Extra
                                2) Stop my Data
                                22 Back
                                0 Menu
                                ''')
                                while True:
                                    d = input("")
                                    if d == "1":
                                        print('''
                                        Payment Option
                                        1) Airtime
                                        2) Smartcash + 20% more
                                        22 Back
                                        0 Menu
                                        ''')
                                        az = input("")
                                        if az == "1":
                                            print('''
                                            You have successfully purchased All Social data plan
                                            ''')
                                        elif az == "2":
                                            print('''
                                            Please enter Smartcash PIN
                                            ''')
                                    elif d == "2":
                                        print('''
                                        Payment Option
                                        1) Airtime
                                        2) Smartcash + 20% more
                                        22 Back
                                        0 Menu
                                        ''')
                                        bz = input("")
                                        if bz == "1":
                                            print('''
                                            You have successfully purchased All Social data plan
                                            ''')
                                        elif bz == "2":
                                            print('''
                                            Please enter Smartcash PIN
                                            ''')
                            else:
                                print('''
                                Invalid Request
                                Weekly Bundles
                                1) N500/750MB/14Days
                                2) N500/1GB/7days
                                3) N1500/6GB/7days
                                4) N300/350MB/7dys
                                5) N100/All Social/5 days
                                22 Back
                                ''')
                    elif option_3 == "3":
                        print('''
                        1) N1000/1.5GB
                        2) N1200/2GB
                        3) N1500/3GB
                        4) N2000/4.5GB
                        5) N2500/6GB
                        6) N3000/10GB
                        7) N4000/11GB
                        8) N5000/20GB
                        22 Back
                        0 Menu
                        ''')
                        while True:
                            i = input("")
                            if i == "1":
                                print('''
                                1.5GB / 30days at N1,000. After your plan 
                                finishes?
                                1) Continue browsing from airtime/ 160MB Extra
                                2) Stop my Data
                                22 Back
                                0 Menu
                                ''')
                            elif i == "2":
                                print('''
                                2GB / 30days at N1,200. After your plan 
                                finishes?
                                1) Continue browsing from airtime/ 160MB Extra
                                2) Stop my Data
                                22 Back
                                0 Menu
                                ''')
                            elif i == "3":
                                print('''
                                3GB / 30days at N1,500. After your plan 
                                finishes?
                                1) Continue browsing from airtime/ 160MB Extra
                                2) Stop my Data
                                22 Back
                                0 Menu
                                ''')
                            elif i == "4":
                                print('''
                                4.5GB / 30days at N2,000. After your plan 
                                finishes?
                                1) Continue browsing from airtime/ 160MB Extra
                                2) Stop my Data
                                22 Back
                                0 Menu
                                ''')
                            elif i == "5":
                                print('''
                                6GB / 30days at N2,500. After your plan 
                                finishes?
                                1) Continue browsing from airtime/ 160MB Extra
                                2) Stop my Data
                                22 Back
                                0 Menu
                                ''')
                            elif i == "6":
                                print('''
                                10GB / 30days at N3,000. After your plan 
                                finishes?
                                1) Continue browsing from airtime/ 160MB Extra
                                2) Stop my Data
                                22 Back
                                0 Menu
                                ''')
                            elif i == "7":
                                print('''
                                11GB / 30days at N4,000. After your plan 
                                finishes?
                                1) Continue browsing from airtime/ 160MB Extra
                                2) Stop my Data
                                22 Back
                                0 Menu
                                ''')
                            elif i == "8":
                                print('''
                                20GB / 30days at N5,000. After your plan 
                                finishes?
                                1) Continue browsing from airtime/ 160MB Extra
                                2) Stop my Data
                                22 Back
                                0 Menu
                                ''')
                            else:
                                print('''
                                Invalid Request
                                1) N1000/1.5GB
                                2) N1200/2GB
                                3) N1500/3GB
                                4) N2000/4.5GB
                                5) N2500/6GB
                                6) N3000/10GB
                                7) N4000/11GB
                                8) N5000/20GB
                                22 Back
                                0 Menu
                                ''')
                    elif option_3 == "4":
                        print('''
                        1) N500/2.5GB/2 days
                        2) N1000/1.5
                        3) N3000/11GB/30 days
                        4) N4000/15GB/30 days
                        5) N5000/22GB/30 days
                        22 Back
                        0 Menu
                        ''')
                    elif option_3 == "5":
                        print('''
                        1) N5,000 for 20GB
                        2) N8,000 for 30GB
                        3) N10,000 for 40GB
                        4) N15,000 for 75GB
                        5) N20,000 for 120GB
                        22 Back
                        0 Menu
                        ''')
                    elif option_3 == "6":
                        print('''
                        1) N30,000/240GB/30days
                        2) N36,000/280GB/30days
                        3) N50,000/400GB/90days
                        4) N60,000/500GB/120days
                        5) N100,000/1TB/365days
                        22 Back
                        0 Menu
                        ''')
                    else:
                        print('''
                        Invalid Request
                        1) Daily/Weekly Bundles
                        2) Weekly Bundles
                        3) Monthly Bundles
                        4) More Data (Data++)
                        5) Mega Bundles
                        6) Big Data Plans
                        * Next
                        22 Back
                        0 Menu
                        ''')
            elif option == "4":
                print('''
                22GB for 30days at N5000. After your plan finishes?
                1) Continue browsing from Airtime/160MB Extra
                2) Stop my Dat*141a
                22 Back
                0 Menu
                ''')
            elif option == "5":
                print('''
                11GB for 30days at N3000. After your plan finishes?
                1) Continue browsing from Airtime/160MB Extra
                2) Stop my Data
                22 Back
                0 Menu
                ''')
            elif option == "6":
                print('''
                1) Continue browsing from Airtime/160MB Extra
                2) Stop my Data
                22 Back
                0 Menu
                ''')
            elif option == "7":
                print('''
                2.5GB for 2days at N500. After your plan finishes?
                1) Continue browsing from Airtime/160MB Extra
                2) Stop my Data
                22 Back
                0 Menu
                ''')
            elif option == "8":
                print('''
                1) Family Plan+
                2) Family Data Plan
                3) Booster Plan
                4) Manage Group
                22 Back
                0 Menu
                ''')

            elif option == "*":
                print('''
                9) Everyday ON
                10) Super Binge
                11) Social Bundle
                12) Hourly Plan
                13) Gifting & Sharing
                14) Trybe Data Plan
                15) Data Balance
                0 Menu
                ''')
            else:
                print('''
                Invalid Request
                1) My Offer
                2) My Area
                3) Data Bundle
                4) N5000/22GB/30 days
                5) N3000/11GB/30 days
                6) N1500/6GB/7 days
                7) N500/2.5GB/2 days
                8) Family Plan
                * Next
                ''')
    elif code == "":
        print("USSD code must be between 1 to 150 characters!!!")
    else:
        print("Seems you dial a wrong code, try *141#")

# Calculator

# ------------------------------------------------------------------------------------------------------------------
