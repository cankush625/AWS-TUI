import os

def cloudtrail_services():
    while True:
        os.system("tput setaf 4")
        print('''
        
            Press
                1. Get All Event Logs
                2. Get Last Event Logs
                3. Create Trail
                4. Get Trail Details
                5. Get Required Trail Details
                6. Delete Trail
                7. Exit
                ''')
        os.system("tput setaf 7")

        # Taking user choice to run the service
        choice = int(input("Enter your choice: "))

        if choice == 1:
            getEventLogs()
        if choice == 2:
            getLastEventLogs()
        if choice == 3:
            createTrail()
        if choice == 4:
            getTrailDetails()
        if choice == 5:
            getRequiredTrailDetails()
        if choice == 6:
            deleteTrail()
        if choice == 7:
            exit()

# Get all event logs
def getEventLogs():
    os.system("aws cloudtrail lookup-events")

# Get last event logs
def getLastEventLogs():
    os.system("aws cloudtrail lookup-events --query Events[0]")

# Creating new trail
def createTrail():
    trailName = input("Enter the trail name: ")
    bucketName = input("Enter the bucket name: ")
    isMultyRegionTrail = input("Enter the is multi region trail option(for eg. --is-multi-region-trail): ")
    os.system("aws cloudtrail create-trail --name {0} --s3-bucket-name {1} {2}".format(trailName, bucketName, isMultyRegionTrail))

# Get details of trails
def getTrailDetails():
    os.system("aws cloudtrail describe-trails")

# Get bucket name and trail name from the CloudTrail
def getRequiredTrailDetails():
    trailNumber = int(input("Enter the trail number(* for all trails): "))
    listOfDetailsNames = ","
    listOfDets = []
    while True:
        choice = int(input("Enter 1 to continue and 2 to stop entering details names"))
        # Taking the names of the required features whose values we have to retrieve from trail details
        if choice == 1:
            name = input("Enter the details name :")
            listOfDets.append(name)
        if choice == 2:
            break
    # Joining each element in the set of the listOfDets with comma so that no space will remain in between
    listOfDetailsNames = listOfDetailsNames.join(list(listOfDets))
    os.system("aws cloudtrail describe-trails --query trailList[{0}].[{1}]".format(trailNumber, listOfDetailsNames))

# Delete the trail
def deleteTrail():
    trailName = input("Enter the trail name: ")
    os.system("aws cloudtrail delete-trail --name {0}".format(trailName))