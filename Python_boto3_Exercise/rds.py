## RDS Creation using boto3.
import boto3
import time

## Initiating a boto3 client for RDS.
rds_client = boto3.client('rds')

# Use Aurora Serverless v2 (provisioned mode with serverless scaling)
engine_version = '8.0.mysql_aurora.3.04.0'  # Version that supports Serverless v2

## user defined variables for RDS instance creation.
username = 'admin'
password = 'Admin12345'
db_subnet_group_name = 'rds-testing'
db_cluster_id = 'my-db-cluster'

## Creating a RDS cluster.
try:
    response = rds_client.describe_db_clusters(DBClusterIdentifier=db_cluster_id)
    print(f"RDS cluster '{db_cluster_id}' already exists. skipping creation.")
except rds_client.exceptions.DBClusterNotFoundFault:
    response = rds_client.create_db_cluster(
        Engine='aurora-mysql',
        EngineVersion=engine_version,
        DBClusterIdentifier=db_cluster_id,
        MasterUsername=username,
        MasterUserPassword=password,
        DatabaseName='mydatabase',
        ServerlessV2ScalingConfiguration={
            'MinCapacity': 0.5,
            'MaxCapacity': 4
        },
    )
    print(f"RDS cluster '{db_cluster_id}' creation initiated. waiting for it to be available...")
    ## Wait for the DB cluster to be available before proceeding.
    while True:
        response = rds_client.describe_db_clusters(DBClusterIdentifier=db_cluster_id)
        status = response['DBClusters'][0]['Status']
        print(f"Current status of RDS cluster '{db_cluster_id}': {status}")
        if status == 'available':
            break
        print("Waiting for RDS cluster to be available...")
        time.sleep(40)  # Wait for 40 seconds before checking again.

## Modify the DB cluster. Update the scaling configuration for the cluster.

response = rds_client.modify_db_cluster(
    DBClusterIdentifier=db_cluster_id,
    ServerlessV2ScalingConfiguration={
        'MinCapacity': 1,
        'MaxCapacity': 8
    },
)
print(f"RDS cluster '{db_cluster_id}' modification initiated. waiting for it to be available...")
## Delete the DB cluster.  
response = rds_client.delete_db_cluster(
    DBClusterIdentifier=db_cluster_id,
    SkipFinalSnapshot=True
)   
print(f"RDS cluster '{db_cluster_id}' deletion initiated. waiting for it to be deleted...")       