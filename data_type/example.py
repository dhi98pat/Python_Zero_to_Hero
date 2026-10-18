## Example combining multiple data types.

# employee = {
#     "name": "Dhiraj Patel",
#     "age": 30,
#     "salary": 500.0,
#     "is_active": True,
#     "skills":["AWS", "Terraform", "Python"],
# }
# print(employee)

## In real-world DevOps automation, Dictionary (dict), List (list), String (str), Boolean (bool), and Integer (int) account for more than 90% of the data you'll work with, especially when handling JSON/YAML responses from AWS, Kubernetes, Terraform, Jenkins, and Docker. Complex, bytes, and bytearray are used less frequently but are still important to understand.

## Production-Level DevOps Example : Suppose Jenkins deploys a new version:
# deployment = {
#     "application": "payment-service",
#     "version": "v3.2.1",
#     "replicas": 6,
#     "cpu_usage": 65.7,
#     "healthy": True,
#     "pods": [
#         "payment-pod-1",
#         "payment-pod-2",
#         "payment-pod-3"
#     ],
#     "regions": ("ap-south-1", "us-east-1"),
#     "active_nodes": {
#         "node1",
#         "node2",
#         "node3"
#     }
# }

# print(deployment)


## Python Code Using All Major Data Types

# ===============================
# DEVOPS PRODUCTION CONFIGURATION
# ===============================

# 1. String (str)
project_name = "ecommerce-platform"

# 2. Integer (int)
replica_count = 5

# 3. Float (float)
cpu_utilization = 78.45

# 4. Boolean (bool)
deployment_success = True

# 5. Complex (complex)
signal_processing = 3 + 4j

# 6. List (list)
microservices = [
    "user-service",
    "payment-service",
    "order-service",
    "inventory-service"
]

# 7. Tuple (tuple)
aws_region = ("ap-south-1", "Mumbai")

# 8. Set (set)
active_nodes = {
    "worker-node-1",
    "worker-node-2",
    "worker-node-3",
    "worker-node-3"
}

# 9. Dictionary (dict)
cluster_details = {
    "cluster_name": "prod-eks",
    "environment": "production",
    "version": "1.30",
    "node_count": 10
}

# 10. Bytes (bytes)
docker_image_hash = b"sha256:abc123xyz"

# 11. Bytearray (bytearray)
deployment_log = bytearray(b"Deployment Started")

# ===============================
# PRODUCTION REPORT
# ===============================
print(f"Project: {project_name}")
print(f"Replicas: {replica_count}")
print(f"CPU Usage: {cpu_utilization}%")
print(f"Deployment Status: {deployment_success}")

print("\nMicroservices:")
for service in microservices:
    print(service)

print("\nAWS Region:")
print(aws_region)

print("\nActive Nodes:")
print(active_nodes)

print("\nCluster Details:")
print(cluster_details)

print("\nImage Hash:")
print(docker_image_hash)

print("\nDeployment Logs:")
print(deployment_log)