import os

def efs_services():
     while True:
        os.system("tput setaf 4")
        print('''
        
            Press
                1. Create EFS Storage
                2. List Storages
                3. Get Storage
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
        if choice == 8:
            exit()

# Creating new EFS storage
def createEFSStorage():
    creationToken = input("Enter the creation token: ")
    performanceMode = input("Enter the performance mode: ")
    throughputMode = input("Enter the throughtput mode: ")
    tagName = input("Enter the tag name: ")
    isEncrypted = input("Enter True/Flase: ")
    try:
        if isEncrypted:
            os.system("aws efs create-file-system --creation-token {0} --performance-mode {1} --throughput-mode {2} --encrypted --tags Key=Name,Value='{3}'".format(creationToken, performanceMode, throughputMode, tagName))
        else:
            os.system("aws efs create-file-system --creation-token {0} --performance-mode {1} --throughput-mode {2} --tags Key=Name,Value='{3}'".format(creationToken, performanceMode, throughputMode, tagName))
    except FileSystemAlreadyExists:
        print("File System already exist")
