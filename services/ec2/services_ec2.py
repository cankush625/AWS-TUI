import os
from services.ec2.key_pair import key_pair

def ec2_services():
    while True:
        os.system("tput setaf 4")
        print('''
        
            Press
                1. Key-Pair
                2. Instance Details
                3. Instance Services
                4. Exit
                ''')
        os.system("tput setaf 7")

        # Taking user choice to run the service
        choice = int(input("Enter your choice(EC2 service number): "))

        if choice == 1:
            key_pair()
        if choice == 4:
            exit()