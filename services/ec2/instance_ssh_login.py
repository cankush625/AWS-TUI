import os

'''Method for login into running instance instance'''
def instance_login():
    # Enter user name
    userName = input("Enter the user name: ")
    # Enter public IP Address of the instance
    ipAddress = input("Enter the IP Address of the instance: ")
    # Enter the name of the key file in the .pem format
    keyFileName = input("Enter the name of the .pem key file: ")

    # Command to login into the running instance
    os.system("sudo ssh -l {0} {1} -i {2}".format(userName, ipAddress, keyFileName))