import os
import json
import boto3
from uuid import uuid4

# Configure AWS SDK for Python (Boto3)
region_name = os.environ.get('AWS_REGION', 'us-east-1')  # Default to us-east-1 if not set
boto3.setup_default_session(region_name=region_name)
dynamodb = boto3.resource('dynamodb', region_name=region_name, api_version='2012-08-10')
doc_client = dynamodb.Table('ProductVisits')

def lambda_handler(event, context):  # Changed handler name to lambda_handler
    print('Received event:', json.dumps(event, indent=2))
    
    # Process each record in the event
    for record in event['Records']:
        body = record['body']
        print(body)
        
        body = json.loads(body)
        
        try:
            required_fields = ['ProductId', 'ProductName', 'Category', 'PricePerUnit', 'CustomerId', 'CustomerName', 'TimeOfVisit']
            if not all(field in body for field in required_fields):
                print('Please provide values for product, category, customer, and time of visit.')
                continue
            
            body['ProductVisitKey'] = str(uuid4())
            
            print(f"{body['ProductVisitKey']} {body['ProductId']} {body['ProductName']} {body['Category']} {body['PricePerUnit']} {body['CustomerId']} {body['CustomerName']} {body['TimeOfVisit']}")
            
            params = {
                'Item': body
            }
            
            doc_client.put_item(**params)
            
            print('Product Visit record is successfully created.')
        
        except Exception as e:
            print(e)
            
    return {}
