import boto3

# variables

alarm_name = "High-CPU-Utilization"  # replace with your CloudWatch alarm name
instance_id = "i-0123456789abcdef0"  # replace with your EC2 instance ID
threshold = 80.0  # CPU utilization threshold percentage

cloudwatch = boto3.client('cloudwatch')

cloudwatch.put_metric_alarm(
    AlarmName=alarm_name,
    MetricName='CPUUtilization',
    Namespace='AWS/EC2',
    Statistic='Average',
    Period=300,
    EvaluationPeriods=1,
    Threshold=threshold,
    ComparisonOperator='GreaterThanThreshold',
    ActionsEnabled=True,
    AlarmActions=[
        'arn:aws:sns:us-east-1:123456789012:MyTopic'  # replace with your SNS topic ARN
    ],
    Dimensions=[
        {
            'Name': 'InstanceId',
            'Value': instance_id
        },
    ],
)

print(f"CloudWatch alarm '{alarm_name}' created for instance '{instance_id}' with threshold {threshold}%")