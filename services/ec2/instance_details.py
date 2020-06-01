import os
import subprocess

def instance_details():
    while True:
        os.system("tput setaf 4")
        print('''
        
            Press
                1. Details of all instances
                2. Get IP address of instances
                3. Get required instance details
                4. Exit
                ''')
        os.system("tput setaf 7")

        # Taking user choice to run the service
        choice = int(input("Enter your choice(EC2 service number): "))

        if choice == 1:
            get_instance_details()
        if choice == 2:
            get_instance_ip()
        if choice == 3:
            get_required_instance_details()
        if choice == 4:
            exit()

# Method to get details of all of the instances
def get_instance_details():
    os.system("aws ec2 describe-instances")

# Method to retrieve IP addresses of the instances
def get_instance_ip():
    instanceNum = input("Enter the instance number for which you want to get Public IP (Enter * for all instances): ")
    os.system("aws ec2 describe-instances --query Reservations[{0}].Instances[0].PublicIpAddress".format(instanceNum))

# Method to retrieve required details of the instances
def get_required_instance_details():
    instanceNum = input("Enter the instance number for which you want to get Public IP (Enter * for all instances): ")
    listOfDetailsNames = ","
    listOfDets = []
    while True:
        choice = int(input("Enter 1 to continue and 2 to stop entering details names"))
        # Taking the names of the required features whose values we have to retrieve from instance details
        if choice == 1:
            name = input("Enter the details name :")
            listOfDets.append(name)
        if choice == 2:
            break
    # Joining each element in the set of the listOfDets with comma so that no space will remain in between
    listOfDetailsNames = listOfDetailsNames.join(set(listOfDets))
    #os.system("aws ec2 describe-instances --query Reservations[{0}].Instances[0].{1}".format(instanceNum, listOfDetailsNames))
    subprocess.call("aws ec2 describe-instances --query Reservations[{0}].Instances[0].[{1}]".format(instanceNum, listOfDetailsNames), shell=True)