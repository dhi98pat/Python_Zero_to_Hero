# Import the boto3 library
import boto3

# Instantiate a boto3 resource for S3 and name your bucket.
s3 = boto3.resource('s3')
bucket_name = 'test-curd-bucket-2024'

# Create the bucket if it does not exist
all_my_buckets = [bucket.name for bucket in s3.buckets.all()]
if bucket_name not in all_my_buckets:
    print(f"Bucket '{bucket_name}' does not exist. Creating bucket...")
    s3.create_bucket(Bucket=bucket_name)
    print(f"Bucket '{bucket_name}' created successfully.")
else:
    print(f"Bucket '{bucket_name}' already exists.No need to create it.")

# Create 'file_1' and 'file_2' in the bucket
file_1 = 'file_1.txt'
file_2 = 'file_2.txt'

# Upload 'file_1' to the new bucket
s3.Bucket(bucket_name).upload_file(Filename=file_1, Key=file_1)
print(f"'{file_1}' uploaded to bucket '{bucket_name}'.")

# READ and print the file from the bucket
obj = s3.Object(bucket_name, file_1)
body = obj.get()['Body'].read()
print(body)

# UPDATE 'file_1' in the bucket with new content from 'file_2'
s3.Object(bucket_name, file_1).put(Body=open(file_2, 'rb'))
obj = s3.Object(bucket_name, file_1)
body = obj.get()['Body'].read()
print(body)

# DELETE the file from the bucket
s3.Object(bucket_name, file_1).delete()

# DELETE the bucket (the bucket should be empty.)
bucket = s3.Bucket(bucket_name)
bucket.delete()
print(f"Bucket '{bucket_name}' and its contents have been deleted.")
