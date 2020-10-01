import os

def efs_services():
     while True:
        os.system("tput setaf 4")
        print('''
        
            Press
                1. Create EFS Storage
                2. Describe EFS file systems
                3. Tag EFS file system
                4. List tags for resource
                5. Create mount target
                6. Describe mount targets
                7. Delete mount target
                8. Delete EFS file system
                9. Exit
                ''')
        os.system("tput setaf 7")

        # Taking user choice to run the service
        choice = int(input("Enter your choice: "))

        if choice == 1:
            createEFSStorage()
        if choice == 2:
            describeEFSFileSystems()
        if choice == 3:
            tagResource()
        if choice == 4:
            listTags()
        if choice == 5:
            createMountTarget()
        if choice == 6:
            describeMountTargets()
        if choice == 7:
            deleteMountTarget()
        if choice == 8:
            deleteEFSFileSystem()
        if choice == 9:
            exit()

# Creating new EFS storage
def createEFSStorage():
    creationToken = input("Enter the creation token: ")
    performanceMode = input("Enter the performance mode: ")
    throughputMode = input("Enter the throughtput mode: ")
    tagName = input("Enter the tag name: ")
    isEncrypted = input("Enter True/False: ")
    try:
        if isEncrypted:
            os.system("aws efs create-file-system --creation-token {0} --performance-mode {1} --throughput-mode {2} --encrypted --tags Key=Name,Value='{3}'".format(creationToken, performanceMode, throughputMode, tagName))
        else:
            os.system("aws efs create-file-system --creation-token {0} --performance-mode {1} --throughput-mode {2} --tags Key=Name,Value='{3}'".format(creationToken, performanceMode, throughputMode, tagName))
    except FileSystemAlreadyExists:
        print("File System already exist")

def describeEFSFileSystems():
    os.system("tput setaf 4")
    print('''
    
        Press
            1. Describe EFS file systems
            2. Describe EFS by creationToken
            3. Describe EFS by filesystem id
            4. Exit
            ''')
    os.system("tput setaf 7")
    choice1 = int(input("Enter your choice: "))
    if choice1 == 1:
        os.system("aws efs describe-file-systems")
    if choice1 == 2:
        token = input("Enter the creation token: ")
        os.system("aws efs describe-file-systems --creation-token {0}".format(token))
    if choice1 == 3:
        id = input("Enter the file system ID: ")
        os.system("aws efs describe-file-systems --file-system-id {0}".format(id))
    if choice1 == 4:
        exit()

def tagResource():
    efsId = input("Enter the EFS file system ID: ")
    tagKey = input("Enter the tag key: ")
    tagValue = input("Enter the tag value: ")
    os.system("aws efs tag-resource --resource-id {0} --tag Key={1},Value={2}".format(efsId, tagKey, tagValue))

def listTags():
    resourceId = input("Enter the EFS file system ID: ")
    os.system("aws efs list-tags-for-resource --resource-id {0}".format(resourceId))

def createMountTarget():
    resourceId = input("Enter the EFS file system ID: ")
    subnetId = input("Enter the subnet ID: ")
    os.system("aws efs create-mount-target --file-system-id {0} --subnet-id {1}".format(resourceId, subnetId))

def describeMountTargets():
    resourceId = input("Enter the EFS file system ID: ")
    os.system("aws efs describe-mount-targets --file-system-id {0}".format(resourceId))

def deleteMountTarget():
    mountTargetId = input("Enter the mount target ID: ")
    os.system("aws efs delete-mount-target --mount-target-id {0}".format(mountTargetId))

def deleteEFSFileSystem():
    resourceId = input("Enter the EFS file system ID: ")
    os.system("aws efs delete-file-system --file-system-id {0}".format(resourceId))