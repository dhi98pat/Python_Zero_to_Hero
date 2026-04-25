## Required Libraries.
import boto3
import io
import csv
import logging

# Constrants - database and credentials details and currecy converstion rates.

currency_conversion_to_usd = {'USD':1, 'CAD': 0.79, 'MXN': 0.05}
database_name = 'my_database'
secret_arn = 'arn:aws:secretsmanager:us-east-1:123456789012:secret:my_secret'
db_cluster_arn = 'arn:aws:rds:us-east-1:123456789012:cluster:my_db_cluster'

# Boto3 client for AWS Services
s3_client = boto3.client('s3')
rds_client = boto3.client('rds-data')


# Configure logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Function to process each record from the CSV file
def process_record(record):
    id, company_name, country, city, product_line, item, bill_date, currency, bill_amount = record
    bill_amount = float(bill_amount) 

    # Convert the bill amount to USD using the currency conversion rates
    rate = currency_conversion_to_usd.get(currency)  # Default to 1 if currency not found
    if rate:
        usd_amount = bill_amount * rate
    else:
        # If no conversion rate is found for the currency, log a warning and skip the conversion
        logger.info(f"No rate found for currency {currency}. Skipping conversion.")      
      # Prepare sql statement with placeholders for inserting data into the RDS database
        sql_statement = ("INSERT IGNORE INTO billing_data "
                          "VALUES (:id, :company_name, :country, :city, :product_line, :item, :bill_date, :currency, :bill_amount, :usd_amount)"
                        )
      # Prepare parameters for the SQL statement
    sql_parameters = [
        {'name': 'id', 'value': {'stringValue': id}},
        {'name': 'company_name', 'value': {'stringValue': company_name}},
        {'name': 'country', 'value': {'stringValue': country}},
        {'name': 'city', 'value': {'stringValue': city}},
        {'name': 'product_line', 'value': {'stringValue': product_line}},
        {'name': 'item', 'value': {'stringValue': item}},
        {'name': 'bill_date', 'value': {'stringValue': bill_date}},
        {'name': 'currency', 'value': {'stringValue': currency}},
        {'name': 'bill_amount', 'value': {'doubleValue': bill_amount}},
        {'name': 'usd_amount', 'value': {'doubleValue': usd_amount}}
    ]

    # Execute the SQL statement and log the response
    response = execute_statement(sql_statement, sql_parameters)
    logger.info(f"Executed SQL statement with response: {response}")

# Function to execute SQL statement.
def execute_statement(sql, sql_parameters):
    try:
        response = rds_client.execute_statement(
            secretArn=secret_arn,
            database=database_name,
            resourceArn=db_cluster_arn,
            sql=sql,
            parameters=sql_parameters
        )
        return response
    except Exception as e:
        logger.error(f"Error executing SQL statement: {e}")
        return None
    
    return response

def lambda_handler(event, context):
    try:    
        # get the bucket and file name from the event
        bucket_name = event['Records'][0]['s3']['bucket']['name']
        s3_file = event['Records'][0]['s3']['object']['key']

        # Read the file from s3
        response = s3_client.get_object(Bucket=bucket_name, Key=s3_file)
        data = response['Body'].read().decode('utf-8')

        # Use csv reader to process the CSV data
        csv_reader = csv.reader(io.StringIO(data))
        next(csv_reader)  # Skip the header row

        # Process each row in the CSV file
        for record in csv_reader:
            process_record(record)  # Implement your record processing logic here

        logging.info("lambda has finished the execution successfully.")    
    except Exception as e:
        logging.error(f"An error occurred: {e}")    