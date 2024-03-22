import json

def lambda_handler(event, context):
    operation = event['queryStringParameters']['operation']
    num1 = float(event['queryStringParameters']['num1'])
    num2 = float(event['queryStringParameters']['num2'])
    
    if operation == 'add':
        result = num1 + num2
    elif operation == 'subtract':
        result = num1 - num2
    elif operation == 'multiply':
        result = num1 * num2
    elif operation == 'divide':
        result = num1 / num2
    else:
        return {
            'statusCode': 400,
            'body': json.dumps('Invalid operation')
        }

    return {
        'statusCode': 200,
        'body': json.dumps(f"The result is {result}")
    }