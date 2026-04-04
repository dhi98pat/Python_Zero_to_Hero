# import boto3

# # Option 1: Use default AWS CLI credentials/profile
# s3_client = boto3.client('s3')

# # Option 2: Explicitly provide credentials (not recommended for production)
# # s3_client = boto3.client(
# #     's3',
# #     aws_access_key_id="YOUR_ACCESS_KEY",
# #     aws_secret_access_key="YOUR_SECRET_KEY",
# #     region_name="ap-south-1"  # Example region
# # )

# # Fetch bucket list
# response = s3_client.list_buckets()

# print("Your S3 Buckets:")
# for bucket in response['Buckets']:
#     print(f" - {bucket['Name']}")

###########################################

# import boto3
# from botocore.exceptions import ClientError

# # Initialize S3 client (uses default AWS CLI credentials/profile)
# s3_client = boto3.client('s3')

# bucket_name = "my-unique-bucket-name-12345-jira"  # Bucket names must be globally unique
# region = "us-east-1"  # Example: Mumbai region

# try:
#     # Create bucket with region specification
#     response = s3_client.create_bucket(
#         Bucket=bucket_name,
#     #    CreateBucketConfiguration={'LocationConstraint': region}
#     )
#     print(f"Bucket '{bucket_name}' created successfully!")
# except ClientError as e:
#     print(f"Error: {e}")

import boto3
s3 = boto3.client("s3")
s3.upload_file(r"C:\Users\Dhiraj\Downloads\image.png", 
               "my-unique-bucket-name-12345-jira", 
               "image.png")
