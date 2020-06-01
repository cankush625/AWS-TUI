import os

def instance_services():
    while True:
        os.system("tput setaf 4")
        print('''
        
            Press
                1. Launch Instances
                2. Exit
                ''')
        os.system("tput setaf 7")

        # Taking user choice to run the service
        choice = int(input("Enter your choice: "))

        if choice == 1:
            launch_instance()
        if choice == 2:
            exit()

def launch_instance():
    image_id = input("Enter the image(AMI) ID: ")
    instance_type = input("Enter the instance type: ")
    count = input("How many instances you want to launch?: ")
    subnet_id = input("Enter the subnet ID: ")
    security_group_id = input("Enter the security group ID: ")
    key_name = input("Enter the key name: ")

    os.system("aws ec2 run-instances --image-id {0} --instance-type {1} --count {2} --subnet-id {3} --security-group-ids {4} --key-name {5}".format(image_id, instance_type, count, subnet_id, security_group_id, key_name))