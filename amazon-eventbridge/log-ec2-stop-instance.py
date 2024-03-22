import json

def lambda_handler(event, context):
    print('LogEC2StopInstance')
    print('Received event:', json.dumps(event, indent=2))
    return {
        'statusCode': 200,
        'body': 'Finished'
    }
