import os

def efs_services():
     while True:
        os.system("tput setaf 4")
        print('''
        
            Press
                1. Create EFS Storage
                2. Describe EFS file systems
                3. Tag EFS file system
                4. List Invalidations
                5. Get Invalidation
                6. Update Root Object
                7. Delete Storage
                8. Exit
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
        if choice == 8:
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
        id = input("Enter the file system id: ")
        os.system("aws efs describe-file-systems --file-system-id {0}".format(id))
    if choice1 == 4:
        exit()

def tagResource():
    efsId = input("Enter the EFS file system ID: ")
    tagKey = input("Enter the tag key: ")
    tagValue = input("Enter the tag value: ")
    os.system("aws efs tag-resource --resource-id {0} --tag Key={1},Value={2}".format(efsId, tagKey, tagValue))
