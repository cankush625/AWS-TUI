import os

def cloudfront_services():
     while True:
        os.system("tput setaf 4")
        print('''
        
            Press
                1. Create Distribution
                2. List Distributions
                3. Get Distribution
                4. Get Invalidation
                5. List Invalidations
                6. Update Distribution
                7. Delete Distribution
                8. Exit
                ''')
        os.system("tput setaf 7")

        # Taking user choice to run the service
        choice = int(input("Enter your choice: "))

        if choice == 1:
            createDistribution()
        if choice == 2:
            listDistributions()
        if choice == 3:
            getDistribution()
        if choice == 4:
            getInvalidation()
        if choice == 5:
            listInvalidations()
        if choice == 6:
            updateDistribution()
        if choice == 7:
            deleteDistribution()
        if choice == 8:
            exit()

# Creating new CloudFront distribution
def createDistribution():
    pass

# Displaying distributions
def listDistributions():
    os.system("aws cloudfront list-distributions")

# Getting distribution
def getDistribution():
    distributionID = input("Enter the distribution id(You will get it from List Distributions option): ")
    os.system("aws cloudfront get-distribution --id {0}".format(distributionID))

# Getting invalidation
def getInvalidation():
    id = input("Enter the  identifier  for  the  invalidation  request: ")
    distributionID = input("Enter the distributions ID: ")
    os.system("aws cloudfront get-invalidation --id {0} --distribution-id {1}".format(id, distributionID))

# Displaying invalidations
def listInvalidations():
    distributionID = input("Enter the distribution id(You will get it from List Distributions option): ")
    os.system("aws cloudfront list-invalidations --distribution-id {0}".format(distributionID))

# Updating distribution
def updateDistribution():
    pass

# Deleting distribution
def deleteDistribution():
    distributionID = input("Enter the distribution id(You will get it from List Distributions option): ")
    eTagHeaderValue = input("Enter the value of the ETag header(You will get it from Get Distribution option): ")
    os.system("aws cloudfront delete-distribution --id {0} --if-match {1}".format(distributionID, eTagHeaderValue))