# dev_team = {"Alice", "Bob", "Charlie"}
# ops_team = {"Charlie", "David", "Eve"}

# # Union (all members)
# print(dev_team | ops_team)  
# # Output: {'Alice', 'Bob', 'Charlie', 'David', 'Eve'}

# # Intersection (common members)
# print(dev_team & ops_team)  
# # Output: {'Charlie'}

# # Difference (only in dev_team)
# print(dev_team - ops_team)  
# # Output: {'Alice', 'Bob'}


## Imagine you’re automating infrastructure and need to ensure you don’t process duplicate resource IDs.

import boto3

# Example: Collect EC2 instance IDs from multiple sources
source_a_ids = ["i-123", "i-456", "i-789"]
source_b_ids = ["i-456", "i-999"]

# Use sets to ensure uniqueness
unique_ids = set(source_a_ids) | set(source_b_ids)

ec2 = boto3.client("ec2", region_name="us-east-1")
response = ec2.describe_instances(InstanceIds=list(unique_ids))

print(f"Processing unique EC2 instances: {unique_ids}")
