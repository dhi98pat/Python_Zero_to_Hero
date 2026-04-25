from config import CPU_THRESHOLD, MAX_RETRIES, IS_PRODUCTION
from logger import log
import time

## Simulated EC2 data (dict + list)
instances = [
    {
        "instance_id": "i-1234567890abcdef0",
        "instance_type": "t2.micro",
        "state": "running",
        "cpu_utilization": 75.5,
        "Tags": {"Env": "Prod"},
        "AutoRemediation": True
    },
    {
        "instance_id": "i-0987654321fedcba0",
        "instance_type": "t2.large",
        "state": "stopped",
        "cpu_utilization": 0.0,
        "Tags": {"Env": "Dev"},
        "AutoRemediation": False
    },
    {
        "instance_id": "i-1122334455667788",
        "instance_type": "t2.medium",  # Assuming a type
        "state": "stopped",
        "cpu_utilization": None,
        "Tags": {},
        "AutoRemediation": False
    }
]

alerted_instances = set() # set for uniqueness

def handle_instance (instance: dict):
    instance_id = instance["instance_id"]
    cpu = instance.get("cpu_utilization")
    env = instance.get("Tags", {}).get("Env", "Unknown")
    auto_remediation = instance.get("AutoRemediation", False)

    # NoneType handling
    if cpu is None:
        log(f"Instance {instance_id} has no CPU data. Skipping.")
        return
    # Threshold checks
    warning, critical, severe = CPU_THRESHOLD
    if cpu >= critical:
        log(f"CRITICAL: {instance_id} CPU at {cpu}% in {env} environment.")
        alerted_instances.add(instance_id)
        if IS_PRODUCTION and auto_remediation:
            restart_instance(instance_id)
        elif cpu >= warning:
            log(f"WARNING: {instance_id} CPU at {cpu}% in {env} environment.")
        else:
            log(f"OKAY: {instance_id} CPU at {cpu}% in {env} environment.") 

def restart_instance(instance_id: str):
    retries = 0
    while retries < MAX_RETRIES:
        log(f"Attempting to restart {instance_id} (Attempt {retries + 1})")
        time.sleep(1)  # Simulate restart delay
        retries += 1
        # Simulate success on second attempt
        log(f"Restart attempt {retries} for {instance_id} completed.")
        return

def main():
    log("EC2 Health Monitoring Started")
    for instance in instances:   # list iteration
        if instance["state"] == "running":
           handle_instance(instance)
    log(f"Alerted Instances: {alerted_instances}")
    log("EC2 Health Monitoring Completed")

if __name__ == "__main__":
    main()        
