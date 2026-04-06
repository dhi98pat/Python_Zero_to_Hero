#"""
#This script manages AWS EC2 instances using the Boto3 library. It allows you to create, start, stop, and terminate EC2 instances. The script also includes functionality to list all EC2 instances and their statuses.
#"""

# Import the boto3 library
import boto3   
# Create an EC2 resource and instance name
ec2 = boto3.resource('ec2')
instance_name = 'Test-python-Instance'
# Store instance ids
instance_ids = None

# Check if instance which you are typing to create already exists or not
# and only work with an instance that hasn't been terminated.

instances = ec2.instances.all()
instance_exists = False
for instance in instances:
    for tag in instance.tags:
        if tag['Key'] == 'Name' and tag['Value'] == instance_name:
            instance_exists = True
            instance_ids = [instance.id]
            print(f"Instance name'{instance_name}' already exists with ID: {instance.id}")
            break
    if instance_exists:
        break
if not instance_exists:
# lunch a new instance if it hasn't been terminated.
    new_instance = ec2.create_instances(
        ImageId='ami-01b14b7ad41e17ba4',  # Amazon Linux 2 AMI
        MinCount=1,
        MaxCount=1,
        InstanceType='t2.micro',
        KeyName = 'shell',          # Replace with your key pair name
        TagSpecifications=[
            {
                'ResourceType': 'instance',
                'Tags': [
                    {
                        'Key': 'Name',
                        'Value': instance_name
                    }
                ]
            }
        ]
    )
    instance_id = new_instance[0].id
    print(f"Instance '{instance_name}' with id {instance_id} is being created...")

# Start the instance
# ec2.Instance(instance_ids[0]).stop()
# print(f"Instance '{instance_name}' with id {instance_ids[0]} is stopping...")
# Start the instance
# ec2.Instance(instance_ids[0]).start()   
# print(f"Instance '{instance_name}' with id {instance_ids[0]} is starting...")
# Terminate the instance
ec2.Instance(instance_ids[0]).terminate()   
print(f"Instance '{instance_name}' with id {instance_ids[0]} is terminating...")