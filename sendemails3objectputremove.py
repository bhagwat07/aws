import boto3
def lambda_handler(event, context):
    for i in event['Records']:
        action = i['eventName']
        ip = i['requestParameters']['sourceIPAddress']
        bucket_name = i['s3']['bucket']['name']
        file_name = i['s3']['object']['key']
    # Access the Simple Email Service via boto3
    client = boto3.client('ses')
    subject = str(action) + "Event From" + bucket_name
    body = '''
        <br>
        This email is notify you ragarding {} event.
        Source IP: {}
    '''.format(action,ip)
    
    message = {"Subject":{'Data':subject},"Body":{"Html":{'Data':body}}}
    response = client.send_email(Source= "prediator31@gmail.com", Destination={'ToAddresses' : ['bhagwat.dataengg@gmail.com']},Message = message)
        
