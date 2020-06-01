import os

def iam_services():
    while True:
        os.system("tput setaf 4")
        print('''
        
            Press
                1. Create User
                2. Create Access Key
                3. Attach User Policy
                4. Exit
                ''')
        os.system("tput setaf 7")

        # Taking user choice to run the service
        choice = int(input("Enter your choice: "))

        if choice == 1:
            create_iam_user()
        if choice == 2:
            create_access_key()
        if choice == 3:
            attach_user_policy()
        if choice == 4:
            exit()

def create_iam_user():
    userName = input("Enter the User Name: ")
    os.system("aws iam create-user --user-name {0}".format(userName))

def create_access_key():
    userName = input("Enter the User Name: ")
    os.system("aws iam create-access-key --user-name {0}".format(userName))

def attach_user_policy():
    awsManagedPolicyName = input("Enter the user policy name: ")
    userName = input("Enter the User Name: ")
    os.system("aws iam attach-user-policy --policy-arn arn:aws:iam:ACCOUNT-ID:aws:policy/{0} --user-name {1}".format(awsManagedPolicyName, userName))