import boto3

# load variables from JSON file
import json
with open('config.json') as f:
    config = json.load(f)

region = config["region"]
instance_type = config["instance_type"]
ami_id = config["ami_id"]

print(f'Loaded configuration: region={region}, instance_type={instance_type}, ami_id={ami_id}')
