import os

def s3_services():
    while True:
        os.system("tput setaf 4")
        print('''
        
            Press
                1. Create New Bucket
                2. Upload file to the Bucket
                3. Delete file from Bucket
                4. Get list of files from Bucket
                5. Delete Bucket
                6. Empty Bucket (Remove all objects)
                7. Bucket Access Control List
                8. Put Bucket ACL
                9. Object Access Control List
                10. Put Object ACL
                11. Exit
                ''')
        os.system("tput setaf 7")

        # Taking user choice to run the service
        choice = int(input("Enter your choice: "))

        if choice == 1:
            createNewBucket()
        if choice == 2:
            uploadFileToBucket()
        if choice == 3:
            deleteFileFromBucket()
        if choice == 4:
            getListOfFiles()
        if choice == 5:
            deleteBucket()
        if choice == 6:
            emptyTheBucket()
        if choice == 7:
            getBucketACL()
        if choice == 8:
            putBucketACL()
        if choice == 9:
            getObjectACL()
        if choice == 10:
            putObjectACL()
        if choice == 11:
            exit()

# Create new S3 bucket
def createNewBucket():
    bucketName = input("Enter the new bucket name: ")
    regionName = input("Enter the region name: ")
    locationConstraint = input("Enter location constraint(region name): ")
    os.system("aws s3api create-bucket --bucket {0} --region {1} --create-bucket-configuration LocationConstraint={2}".format(bucketName, regionName, locationConstraint))

# Upload file to the S3 bucket
def uploadFileToBucket():
    localFileLocation = input("Enter the local file location: ")
    s3BucketLocation = input("Enter the S3 bucket location: ")
    acl = input("Enter the ACL for this file(for eg. public-read): ")
    os.system("aws s3 cp {0} {1} --acl {2}".format(localFileLocation, s3BucketLocation, acl))

# Delete file from S3 bucket
def deleteFileFromBucket():
    fileName = input("Enter the file location from the S3 bucket: ")
    os.system("aws s3 rm {0}".format(fileName))

# Get the list of stored files in the bucket
def getListOfFiles():
    bucketName = input('Enter the bucket name: ')
    os.system("aws s3 ls {0}".format(bucketName))

def deleteBucket():
    os.system("tput setaf 4")
    print('''
    
        Press
            1. Delete Empty Bucket
            2. Delete Non-Empty Bucket
            3. Exit
            ''')
    os.system("tput setaf 7")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        deleteEmptyBucket()
    if choice == 2:
        deleteNonEmptyBucket()
    if choice == 3:
        exit()

# Delete the existing empty bucket
def deleteEmptyBucket():
    bucketName = input("Enter the bucket name: ")
    regionName = input("Enter the region name: ")
    os.system("aws s3api delete-bucket --bucket {0} --region {1}".format(bucketName, regionName))

# Delete the existing non-empty bucket
def deleteNonEmptyBucket():
    bucketName = input("Enter the bucket name: ")
    os.system("aws s3 rb s3://{0} --force".format(bucketName))

# Removing all of the objects from bucket
def emptyTheBucket():
    bucketName = input("Enter the bucket name: ")
    os.system("aws s3 rm s3://{0} --recursive".format(bucketName))

# Get bucket access control list
def getBucketACL():
    bucketName = input("Enter the bucket name: ")
    os.system("aws s3api get-bucket-acl --bucket {0}".format(bucketName))

# Put bucket access control list
def putBucketACL():
    os.system("tput setaf 4")
    print('''
    
        Press
            1. Put Bucket ACL by User ID
            2. Put Bucket ACL by Email (Supported in limited regions)
            3. Exit
            ''')
    os.system("tput setaf 7")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        putBucketACLbyID()
    if choice == 2:
        putBucketACLbyEmail()
    if choice == 3:
        exit()

# Put bucket ACL by ID
def putBucketACLbyID():
    bucketName = input("Enter the bucket name: ")
    aclName = input("Enter the ACL name(for eg. --grant-read): ")
    userID = input("Enter the User ID: ")
    os.system("aws s3api put-bucket-acl --bucket {0} {1} id={2}".format(bucketName, aclName, userID))

# Put bucket ACL by email
# Using email addresses to specify a grantee is  only  supported in the limited AWS Regions
def putBucketACLbyEmail():
    bucketName = input("Enter the bucket name: ")
    aclName = input("Enter the ACL name(for eg. --grant-read): ")
    emailID = input("Enter the Email ID: ")
    os.system("aws s3api put-bucket-acl --bucket {0} {1} emailaddress={2}".format(bucketName, aclName, emailID))

# Get object access control list
def getObjectACL():
    bucketName = input("Enter the bucket name: ")
    keyName = input("Enter the key name(for eg. file.txt): ")
    os.system("aws s3api get-object-acl --bucket {0} --key {1}".format(bucketName, keyName))

# Put object access control list
def putObjectACL():
    os.system("tput setaf 4")
    print('''
    
        Press
            1. Put Object ACL by User ID
            2. Put Object ACL by Email (Supported in limited regions)
            3. Exit
            ''')
    os.system("tput setaf 7")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        putObjectACLbyID()
    if choice == 2:
        putObjectACLbyEmail()
    if choice == 3:
        exit()

# Put object ACL by ID
def putObjectACLbyID():
    bucketName = input("Enter the bucket name: ")
    keyName = input("Enter the name of the file(for eg. file.txt): ")
    aclName = input("Enter the ACL name(for eg. --grant-read): ")
    userID = input("Enter the User ID: ")
    os.system("aws s3api put-bucket-acl --bucket {0} --key {1} {2} id={3}".format(bucketName, keyName, aclName, userID))

# Put object ACL by email
# Using email addresses to specify a grantee is  only  supported in the limited AWS Regions
def putObjectACLbyEmail():
    bucketName = input("Enter the bucket name: ")
    keyName = input("Enter the name of the file(for eg. file.txt): ")
    aclName = input("Enter the ACL name(for eg. --grant-read): ")
    emailID = input("Enter the Email ID: ")
    os.system("aws s3api put-bucket-acl --bucket {0} --key {1} {2} emailaddress={3}".format(bucketName, keyName, aclName, emailID))