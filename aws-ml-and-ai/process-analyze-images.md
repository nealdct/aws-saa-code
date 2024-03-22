# Instructions

1. Create an S3 bucket

2. Create a DynamoDB table
- Name: ImageAnalysisResults
- Primary key: ImageName

3. Create a Lambda function
- Name: RekognitionLab
- Runtime: Python 3.9
- Code: Add the following code

```python
import boto3
import json

def lambda_handler(event, context):
    # Initialize clients
    s3_client = boto3.client('s3')
    rekognition_client = boto3.client('rekognition')
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('YourDynamoDBTableName')  # Replace with your table name

    # Get the S3 bucket name and object key from the event
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    object_key = event['Records'][0]['s3']['object']['key']

    # Call Amazon Rekognition to detect labels in the image
    response = rekognition_client.detect_labels(
        Image={'S3Object': {'Bucket': bucket_name, 'Name': object_key}},
        MaxLabels=10
    )

    # Store the labels detected in DynamoDB
    labels = [{'Confidence': label['Confidence'], 'Name': label['Name']} for label in response['Labels']]
    table.put_item(
        Item={
            'ImageName': object_key,
            'Labels': json.dumps(labels)
        }
    )

    return {
        'statusCode': 200,
        'body': json.dumps('Image processed successfully!')
    }
```

4. Edit the table name in the code and deploy

5. Add permissions to Lambda
- AmazonRekognitionFullAccess
- AmazonDynamoDBFullAccess
- AmazonS3ReadOnlyAccess

6. In Lambda create a trigger for object creation events in the S3 bucket
7. Upload images to the bucket and review the results in DynamoDB