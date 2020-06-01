import os

def aws_login():
    while True:
        os.system("tput setaf 4")
        print('''
        
            Press
                1. Login
                2. Exit
                ''')
        os.system("tput setaf 7")

        # Taking user choice to run the service
        choice = int(input("Enter your choice: "))

        if choice == 1:
            login()
        if choice == 2:
            exit()

def login():
    os.system("aws configure")