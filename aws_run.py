import os
from auth.aws_login import aws_login
from services.ec2.instance_ssh_login import instance_login

os.system("tput setaf 1")
print("\t\t\t\tWelcome to the AWS-TUI interface!")
os.system("tput setaf 7")
print("\t\t\t--------------------------------------------")

while True:
    os.system("tput setaf 4")
    print('''
    
        Press
            1. Login to the AWS Account
            2. AWS Services
            3. Exit
            ''')
    os.system("tput setaf 7")

    # Taking user choice to run the service
    choice = int(input("Enter your choice(number): "))

    if choice == 1:
        aws_login()
    if choice == 2:
        pass
        # instance_login()
    if choice == 3:
        exit()