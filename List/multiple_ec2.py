import boto3

# List of instance IDs to stop
instance_ids = ["i-0123456789abcdef0", "i-0abcdef1234567890"]

ec2 = boto3.client("ec2", region_name="us-east-1")
ec2.stop_instances(InstanceIds=instance_ids)

print(f"Stopped instances: {instance_ids}")
