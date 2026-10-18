## Operators are special symbols used to perform operations on variables and values.

The operators you'll use most in AWS, Terraform, Kubernetes, and Python automation scripts are:

Comparison Operators (==, !=, >, )
Logical Operators (and, or, not)
Assignment Operators (=, +=)
Membership Operators (in, not in)

These are heavily used when:

Validating AWS resources
Checking EC2/RDS status
Kubernetes health checks
Terraform automation
CI/CD pipeline conditions
Monitoring and alerting scripts (CloudWatch, Prometheus, Grafana)

# 1. Arithmetic Operators

a = 10
b = 3

print(a + b)   # 13
print(a - b)   # 7
print(a * b)   # 30
print(a / b)   # 3.333
print(a % b)   # 1
print(a // b)  # 3
print(a ** b)  # 1000

# 2. Comparison (Relational) Operators

cpu_usage = 80

print(cpu_usage > 75)
print(cpu_usage == 80)
print(cpu_usage != 90)

## 3. Assignment Operators

memory = 8

memory += 4
print(memory)

memory *= 2
print(memory)

# 4. Logical Operators

cpu = 85
memory = 70

p***t(cpu > 80 and memory > 60)
prin***pu > 90 or memory > 60)
print(no***pu > 90))

## 5. Identity Operators

a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is ***print(a is c)

## 6. Membership Operators

services = ["jenkins"***docker", "kubernetes"]

print("d***er" in services)
print("terrafor***in services)



## Q: Which Python operators are most frequently used in DevOps automation?

Answer:

Comparison Operators (==, !=, >, )
Logical Operators (and, or, not)
Assignment Operators (=, +=)
Membership Operators (in, not in)
Arithmetic Operators (+, -, *, /)