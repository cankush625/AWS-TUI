# This file provides methods like create key-pair, names of the key-pairs
import os

def key_pair():
    while True:
        os.system("tput setaf 4")
        print('''
        
            Press
                1. Create new key-pair
                2. Show keyName of available key-pairs
                3. Exit
                ''')
        os.system("tput setaf 7")

        # Taking user choice to run the service
        choice = int(input("Enter your choice(EC2 service number): "))

        if choice == 1:
            create_key_pair()
        if choice == 2:
            show_keynames()
        if choice == 3:
            exit()

def create_key_pair():
    newKeyName = input("Enter the name for the new key-pair: ")
    os.system("sudo aws ec2 create-key-pair --key-name {0}".format(newKeyName))

def show_keynames():
    os.system("aws ec2 describe-key-pairs --query KeyPairs[*].KeyName")