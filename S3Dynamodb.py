import boto3
import json 

s3_client = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')

def lambda_handler(event, context):
    bucket = event['Records'][0]['s3']['bucket']['name']
    filename = event['Records'][0]['s3']['object']['key']
    #print('We found right bucket name and object: {0} {1}'.format(bucket, filename))
    json_object = s3_client.get_object(
            Bucket=bucket,
            Key=filename
    )
    jsonFileReader = json_object['Body'].read()
    jsonDict = json.loads(jsonFileReader)
    table = dynamodb.Table('Employees')
    table.put_item(Item=jsonDict)
    
    return 'Hello from Lambda'
    