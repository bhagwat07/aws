import boto3
import json


s3 = boto3.client('s3')

def lambda_handler(event, context):
    # TODO implement
    source_bucket = event['Records'][0]['s3']['bucket']['name']
    object_key = event['Records'][0]['s3']['object']['key']
    target_bucket = 'output-110123'
    copy_source = {'Bucket': source_bucket, 'Key': object_key}
    try:
       s3.copy_object(Bucket=target_bucket, Key=object_key, CopySource=copy_source)
        
        
    except Exception as err:
        print ("Error -"+str(err))
