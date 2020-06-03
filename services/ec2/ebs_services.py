import os

def ebs_services():
    while True:
        os.system("tput setaf 4")
        print('''
        
            Press
                1. Create New Volume
                2. Get Volume Details
                3. Delete Volume
                4. Attach Volume to Instance
                5. Detach Volume
                6. Exit
                ''')
        os.system("tput setaf 7")

        # Taking user choice to run the service
        choice = int(input("Enter your choice: "))

        if choice == 1:
            createNewVolume()
        if choice == 2:
            getVolumeDetails()
        if choice == 3:
            deleteVolume()
        if choice == 4:
            attachVolume()
        if choice == 5:
            detachVolume()
        if choice == 6:
            exit()

# Create a new volume
def createNewVolume():
    availabilityZone = input("Enter the name of the availability zone: ")
    volumeType = input("Enter the volume type: ")
    size = input("Enter the volume size in GB: ")
    key = input("Enter the key: ")
    value = input("Enter the value: ")
    command = "aws ec2 create-volume --availability-zone " + availabilityZone + " --volume-type " + volumeType + " --size " + size + " --tag-specifications ResourceType=volume,Tags=[{Key=" + key + ",Value=" + value + "}]"
    os.system(command)

# Get volume details
def getVolumeDetails():
    os.system("aws ec2 describe-volumes")

# Delete existing volume
def deleteVolume():
    volumeID = input("Enter the ID of the volume which you want to delete: ")
    os.system("aws ec2 delete-volume --volume-id {0}".format(volumeID))

# Attach the existing volume to the instance
def attachVolume():
    volumeID = input("Enter the volume ID which you want to attach: ")
    instanceID = input("Enter the instance ID to which you want to attach volume: ")
    deviceName = input("Enter the device name( for example, /dev/sdh or xvdh ): ")
    os.system("aws ec2 attach-volume --volume-id {0} --instance-id {1} --device {2}".format(volumeID, instanceID, deviceName))

# Detach the volume
def detachVolume():
    volumeID = input("Enter the volume ID which you want to attach: ")
    os.system("aws ec2 detach-volume --volume-id {0}".format(volumeID))