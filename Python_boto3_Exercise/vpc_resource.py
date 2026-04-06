## Creating the VPC with boto3 resource..
import boto3
import time
# Create a VPC resource and name your VPC.
ec2 = boto3.client('ec2')
vpc_name = 'Test-python-VPC'
responce = ec2.describe_vpcs(
    Filters=[
        {
            'Name': 'tag:Name',
            'Values': [vpc_name]
        }])
vpcs = responce.get('Vpcs', [])
if vpcs:
    vpc_id = vpcs[0]['VpcId']
    print(f"VPC '{vpc_name}' already exists with ID: {vpc_id}")
else:
    vpc_response = ec2.create_vpc(CidrBlock='10.0.0.0/16')
    vpc_id = vpc_response['Vpc']['VpcId']
    time.sleep(5)  # Wait for the VPC to be fully created before tagging it
    ec2.create_tags(Resources=[vpc_id], Tags=[{'Key': 'Name', 'Value': vpc_name}])
    print(f"VPC '{vpc_name}' with id {vpc_id} is being created...")

## Create Internet gateway
ig_name = 'Test-python-IG'
response = ec2.describe_internet_gateways(
    Filters=[
        {
            'Name': 'tag:Name',
            'Values': [ig_name]
        }])
igws = response.get('InternetGateways', [])
if igws:
    igw_id = igws[0]['InternetGatewayId']
    print(f"Internet Gateway '{ig_name}' already exists with ID: {igw_id}")
else:
    igw_response = ec2.create_internet_gateway()
    igw_id = igw_response['InternetGateway']['InternetGatewayId']
    ec2.create_tags(Resources=[igw_id], Tags=[{'Key': 'Name', 'Value': ig_name}])
    ec2.attach_internet_gateway(VpcId=vpc_id, InternetGatewayId=igw_id)
    print(f"Internet Gateway '{ig_name}' with id {igw_id} is been created...")

## Create a route table and public route
rt_response = ec2.create_route_table(VpcId=vpc_id)
rt_id = rt_response['RouteTable']['RouteTableId']
route = ec2.create_route(
    RouteTableId=rt_id,
    DestinationCidrBlock='0.0.0.0/0',
    GatewayId=igw_id
    )    
print(f"Route Table with ID '{rt_id}' is been created...")

## Create 3 subnets.
subnet_cidrs = [
    {'CIDR': '10.0.1.0/24', 'AZ': 'us-east-1a'},
    {'CIDR': '10.0.2.0/24', 'AZ': 'us-east-1b'},
    {'CIDR': '10.0.3.0/24', 'AZ': 'us-east-1c'}
]
subnet_ids = []
for subnet_config in subnet_cidrs:
    existing_subnets = ec2.describe_subnets(
        Filters=[
            {'Name': 'vpc-id', 'Values': [vpc_id]},
            {'Name': 'cidr-block', 'Values': [subnet_config['CIDR']]}
        ])
    if existing_subnets['Subnets']:
        subnet_id = existing_subnets['Subnets'][0]['SubnetId']
        print(f"Subnet with CIDR '{subnet_config['CIDR']}' already exists with ID: {subnet_id}")
        subnet_ids.append(subnet_id)
    else:
        subnet_response = ec2.create_subnet(VpcId=vpc_id, CidrBlock=subnet_config['CIDR'], AvailabilityZone=subnet_config['AZ'])
        subnet_id = subnet_response['Subnet']['SubnetId']
        subnet_ids.append(subnet_id)
        print(f"Subnet with CIDR '{subnet_config['CIDR']}' created with ID: {subnet_id}")
print(f"Subnets created/verified with IDs: {', '.join(subnet_ids)}")

## Delete all the created resources in the file.
# for subnet_id in subnet_ids:
#     ec2.delete_subnet(SubnetId=subnet_id)
# print("Subnets deleted successfully.")
# ec2.delete_route(RouteTableId=rt_id, DestinationCidrBlock='0.0.0.0/0')
# print("Route deleted successfully.")
# ec2.delete_route_table(RouteTableId=rt_id)
# print("Route table deleted successfully.")
# ec2.detach_internet_gateway(VpcId=vpc_id, InternetGatewayId=igw_id)
# ec2.delete_internet_gateway(InternetGatewayId=igw_id)
# print("Internet gateway deleted successfully.")
# ec2.delete_vpc(VpcId=vpc_id)
# print("VPC deleted successfully.")
