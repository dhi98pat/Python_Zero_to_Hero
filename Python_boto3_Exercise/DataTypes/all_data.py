isinstance = [
    {
        "instance_id": "i-1234567890abcdef0",
        "instance_type": "t2.micro",
        "state": "running",
        "cpu_utilization": 75.5,
        "Tags":{"Env": "Prod"}
    },
    {
        "instance_id": "i-0987654321fedcba0",
        "instance_type": "t2.large",
        "state": "stopped",
        "cpu_utilization": 0.0,
        "Tags":{"Env": "Dev"}
    }
]

for instance in isinstance:
    if instance ["cpu_utilization"] > 70.0:
        print(f"Instance {instance['instance_id']} has high CPU utilization: {instance['cpu_utilization']}%")   