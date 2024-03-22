import boto3
from botocore.exceptions import WaiterError

def wait_until_instance_stopped(ec2_client, instance_id):
    waiter = ec2_client.get_waiter('instance_stopped')
    try:
        waiter.wait(InstanceIds=[instance_id])
    except WaiterError as e:
        # Handle the exception if the instance fails to stop within the specified timeout
        print(f"Error waiting for instance to stop: {e}")

def lambda_handler(event, context):
    # Retrieve the instance ID from the event parameter
    instance_id = event['instanceId']
    
    # Create an EC2 client
    ec2_client = boto3.client('ec2')
    
    try:
        # Stop the instance
        ec2_client.stop_instances(InstanceIds=[instance_id])
        
        # Wait until the instance is stopped
        wait_until_instance_stopped(ec2_client, instance_id)
        
        # Modify the instance type
        ec2_client.modify_instance_attribute(InstanceId=instance_id, InstanceType={'Value': 't2.medium'})
        
        # Start the instance
        ec2_client.start_instances(InstanceIds=[instance_id])
        
        return 'Instance resizing complete.'
    
    except Exception as e:
        # Handle any exceptions that occur during the resizing process
        return f'Error resizing instance: {e}'
    

# Test event JSON: {"instanceId": "<instance-ID>"}