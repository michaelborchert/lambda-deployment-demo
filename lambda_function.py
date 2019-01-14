import json

def lambda_handler(event, context):
    if not event:
        return {'statusCode': 200, 'body': json.dumps(event)}
    #else:
    #    return {'statusCode': 400, 'body': 'No event received.'}

    return {
        'statusCode': 200,
        'body': json.dumps('Hello everyone!')
    }
