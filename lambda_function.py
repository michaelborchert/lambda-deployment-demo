import json

def lambda_handler(event, context):
    if event:
        return json.dumps(event)

    return {
        'statusCode': 200,
        'body': json.dumps('Hello, from Lambda!')
    }
