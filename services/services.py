import os
from services.ec2.services_ec2 import ec2_services
from services.IAM.iam_services import iam_services
from services.CloudTrail.cloudtrail_services import cloudtrail_services
from services.S3.s3_services import s3_services
from services.CloudFront.cloudfront_services import cloudfront_services
from services.EFS.efs_services import efs_services

def aws_services():
    while True:
        os.system("tput setaf 4")
        print('''
        
            Press
                1. EC2
                2. IAM
                3. S3
                4. EFS
                5. CloudTrail
                6. CloudFront
                7. Exit
                ''')
        os.system("tput setaf 7")

        # Taking user choice to run the service
        choice = int(input("Enter your choice(service number): "))

        if choice == 1:
            ec2_services()
        if choice == 2:
            iam_services()
        if choice == 3:
            s3_services()
        if choice == 4:
            efs_services()
        if choice == 5:
            cloudtrail_services()
        if choice == 6:
            cloudfront_services()
        if choice == 7:
            exit()