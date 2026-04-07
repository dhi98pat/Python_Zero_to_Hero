import json
import boto3
import logging
from datetime import datetime
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')
    current_date = datetime.now().strftime("%Y-%m-%d")
    
    try: 
        response = ec2.create_snapshot(
            VolumeId='vol-087fee4c84365a404',  # Replace with your volume ID
            Description= 'My EC2 Snapshot',
            TagSpecifications=[
                {
                'ResourceType': 'snapshot',
                'Tags': [
                    {
                        'Key': 'Name',
                        'Value': f"My EC2 Snapshot {current_date}"
                    },
                ]
            }
            ]
        )
        logger.info(f"Snapshot created successfully: {json.dumps(response, default=str)}")
    except Exception as e:
        logger.error(f"Error creating snapshot: {str(e)}")    
