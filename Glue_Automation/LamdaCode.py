import json
import boto3

def lambda_handler(event, context):
   # Retrieve File Information
   bucket_name =   event['Records'][0]['s3']['bucket']['name']
   s3_file_name =  event['Records'][0]['s3']['object']['key']
   client = boto3.client('glue')
   print("bucket: ",bucket_name)
   print("file: ", s3_file_name)
   response = client.start_job_run(JobName = 'lambdaglue', Arguments={"--buck":bucket_name,"--file":s3_file_name})
