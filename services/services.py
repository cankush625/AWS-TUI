import os
from services.ec2.services_ec2 import ec2_services

def aws_services():
    while True:
        os.system("tput setaf 4")
        print('''
        
            Press
                1. EC2
                2. IAM
                3. Exit
                ''')
        os.system("tput setaf 7")

        # Taking user choice to run the service
        choice = int(input("Enter your choice(service number): "))

        if choice == 1:
            ec2_services()
        if choice == 3:
            exit()