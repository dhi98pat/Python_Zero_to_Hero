## Tuples are useful when you want to store fixed configuration values that shouldn’t change

## Fixed AWS Configuration values
aws_config = ("us-east-1", "t2.micro")
region, instance_type = aws_config

print(f"Region: {region}, Instance Type: {instance_type}")
