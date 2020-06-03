import os

def cloudtrail_services():
    while True:
        os.system("tput setaf 4")
        print('''
        
            Press
                1. Get All Event Logs
                2. Get Last Event Logs
                3. Exit
                ''')
        os.system("tput setaf 7")

        # Taking user choice to run the service
        choice = int(input("Enter your choice: "))

        if choice == 1:
            getEventLogs()
        if choice == 2:
            getLastEventLogs()
        if choice == 3:
            exit()

# Get all event logs
def getEventLogs():
    os.system("aws cloudtrail lookup-events")

# Get last event logs
def getLastEventLogs():
    os.system("aws cloudtrail lookup-events --query Events[0]")