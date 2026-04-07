## Import necessary modules
## CSV for handling CSV files, boto3 for AWS SDK,  datetime for handling date and time.
import csv
import boto3
from datetime import datetime

def lambda_handler(event, context):
    # Initialize the S3 resource using boto3
    s3 = boto3.resource('s3')
    
    # Extract  the bucket and the CSV file name from the event input
    billing_bucket = event['Record'][0]['s3']['bucket']['name']
    csv_file = event['Record'][0]['s3']['object']['key']
    
    # Define the name of the error bucket where you want to copy the error CSV files
    error_bucket = 'test-python-724995943431-us-east-1-an'  # Replace with your error bucket name
    
    # Download the CSV file from the S3 bucket read the containt decode from bytes to string and split it into lines
    obj = s3.Object(billing_bucket, csv_file)
    data = obj.get()['Body'].read().decode('utf-8').splitlines()
    
    # Initlialize a flag (error_found) to false. We'll set this  flag to true when we find the error.
    error_found = False
    
    # Define valid product lines and validate currencies.
    valid_product_lines = ['Bakary', 'Meat', 'Dairy']  # Add more valid product lines as needed
    valid_currencies = ['USD', 'EUR', 'GBP']  # Add more valid
    
    # read the CSV containt line by line using Python csv reader.Ignore the header line (data[1:])
    for row in csv.reader(data[1:], delimiter=','):
        # For each line, extract the relevant fields (e.g., date, product line, currency, bill amount) and perform the necessary validations.
        date = row [6]
        product_line = row[4]
        currency = row[7]
        bill_amount = float(row[8])
    
    # Check if the product line is valid. If not, set the error_found flag to true and print the error message.
    if product_line not in valid_product_lines:
        error_found = True
        print(f"Error in record {row[0]}: Invalid product line. {product_line}. ")

    # check if the currency is valid. If not, set the error_found flag to true and print the error message.
    if currency not in valid_currencies:
        error_found = True
        print(f"Error in record {row[0]}: Invalid currency. {currency}. ")

    # Check if the bill amount is a negative number. If not, set the error_found flag to true and print the error message.
    if bill_amount < 0:
        error_found = True
        print(f"Error in record {row[0]}: Negative bill amount. {bill_amount}. ")
    
    # Check if the date is in the correct format (e.g., YYYY-MM-DD) and is a valid date. If not, set the error_found flag to true.
        try:
            datetime.strptime(date, '%Y-%m-%d')
        except ValueError:
            error_found = True
            print(f"Error in record {row[0]}: Invalid date format. {date}. ")
    
    # Afetr checking all the rows, if the error is found, copy the CSV file to the error bucket and delete it from the original bucket.
    if error_found:
        copy_source = {
            'Bucket': billing_bucket,
            'Key': csv_file
            } 
        try:    
            s3.meta.client.copy(copy_source, error_bucket, csv_file)
            print(f"Moved errors file to error bucket: {error_bucket}")
            s3.Object(billing_bucket, csv_file).delete()
            print("Deleted original file from billing bucket.")
    
    # Handle any exceptions that may occur during the copy and delete operations, and print the error message.
        except Exception as e:
            print(f"Error moving file to error bucket: {str(e)}")
    
    # If no errors were found,return a success message with status code 200. and a body message indicating the no error were found in the CSV file.
    else:
        return {
            'statusCode': 200,    
            'body': 'No errors found in the CSV file!'
        }