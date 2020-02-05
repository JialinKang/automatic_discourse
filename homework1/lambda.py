import json

def lambda_handler(event, context):
    # TODO implement
    print('this is jialin first test file')
    for i in range(10):
        print(i)
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
