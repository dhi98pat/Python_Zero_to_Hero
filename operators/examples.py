## Scenario: Kubernetes Auto-Scaling and Alerting System

# # Monitoring Metrics
# cpu_usage = 85
# memory_usage = 75
# disk_usage = 92

# # Existing replicas
# replicas = 3

# # Running services
# services = ["frontend", "backend", "database"]

# # Arithmetic Operators
# available_cpu = 100 - cpu_usage
# print("Available CPU:", available_cpu)

# # Comparison Operators
# if cpu_usage > 80:
#     print("High CPU detected")

# # Logical Operators
# if cpu_usage > 80 and memory_usage > 70:
#     print("Trigger Horizontal Pod Autoscaler")

# # Assignment Operators
# replicas += 2
# print("New Replica Count:", replicas)

# # Membership Operators
# if "database" in services:
#     print("Database Service Healthy")

# # Identity Operators
# current_services = services

# if current_services is services:
#     print("Same Service Object")

# # Bitwise Operator Example
# node_status1 = 1
# node_status2 = 1

# health_check = node_status1 & node_status2
# print("Cluster Health:", health_check)


## Imagine you're managing an AWS EKS cluster:

cpu = 90
memory = 82
replicas = 4

if cpu > 85 and memory > 80:
    replicas += 2
    print(f"Scaling application to {replicas} replicas")

if cpu >= 90:
    print("Send Slack Alert")

services = ["jenkins", "docker", "terraform", "kubernetes"]

if "terraform" in services:
    print("Terraform Service Available")
else:
    print("Terraform Service Not Found")