import boto3

def lambda_handler(event, context):
    ec2_client = boto3.client('ec2')
    # Get all Elastic IPs in the account
    response = ec2_client.describe_addresses()
    
    for elastic_ip in response['Addresses']:
        if elastic_ip.get('InstanceId') is None:
            print(f"Allocation ID: {elastic_ip.get('AllocationId')}, Public IP: {elastic_ip.get('PublicIp')}")
            ec2_client.release_address(AllocationId=elastic_ip.get('AllocationId'))
    return {
        'statusCode': 200,
        'body': f"Processed {len(response['Addresses'])} Elastic IPs"
    }    