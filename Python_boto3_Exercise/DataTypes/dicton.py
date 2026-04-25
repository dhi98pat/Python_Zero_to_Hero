## Most important data type for DevOps as 80 % of boto3 responses are in the form of dictonary.

ec2_instance = {
    "InstanceId": "i-1234567890abcdef0",
    "InstanceType": "t2.micro",
    "State": "running",
    "Tags": {
        "Environment": "Production",
        "Owner": "Dhiraj"
    }
}
print(ec2_instance["InstanceId"])
print(ec2_instance["Tags"]["Environment"])
print(ec2_instance["Tags"]["Owner"]) 