import boto3

# variables for S3 configuration.
bucket_name = 'my-s3-bucket'  # replace with your S3 bucket name
file_name = 'my-file.txt'  # replace with your file name
object_name = 'uploaded-file.txt'  # name of the file in S3 after upload

s3 = boto3.client('s3')
s3.upload_file(file_name, bucket_name, object_name)
print(f'Uploaded {file_name} to S3 bucket {bucket_name} as {object_name}')
