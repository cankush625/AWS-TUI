import os
from services.ec2.key_pair import key_pair
from services.ec2.instance_ssh_login import instance_login
from services.ec2.instance_details import instance_details
from services.ec2.instance_services import instance_services
from services.ec2.ebs_services import ebs_services

def ec2_services():
    while True:
        os.system("tput setaf 4")
        print('''
        
            Press
                1. Key-Pair
                2. Instance SSH Login
                3. Instance Details
                4. Instance Services
                5. EBS(Elastic Block Storage)
                6. Exit
                ''')
        os.system("tput setaf 7")

        # Taking user choice to run the service
        choice = int(input("Enter your choice(EC2 service number): "))

        if choice == 1:
            key_pair()
        if choice == 2:
            instance_login()
        if choice == 3:
            instance_details()
        if choice == 4:
            instance_services()
        if choice == 5:
            ebs_services()
        if choice == 6:
            exit()