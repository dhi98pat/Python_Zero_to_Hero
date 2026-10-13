import boto3
# varibles for ec2 configuration.
region = 'us-east-1'
ami_id = 'ami-0c55b159cbfafe1f0'
instance_type = 't2.micro'
key_name = 'my-key-pair'
security_group = 'my-security-group' # replace with correct SG.

ec2 = boto3.resource('ec2', region_name=region)

response = ec2.run_instances(
    ImageId=ami_id,
    InstanceType=instance_type,
    KeyName=key_name,
    SecurityGroups=[security_group],
    MinCount=1,
    MaxCount=1
)
instance_id = response['Instances'][0]['InstanceId']
print(f'Launched EC2 instance with ID: {instance_id}')