import boto3

def lambda_handler(event, context):
    # Get the source and destination file paths
    source_bucket = event['Records'][0]['s3']['bucket']['name']
    source_file = event['Records'][0]['s3']['bucket']['name']
    destination_bucket = 'your-destination-bucket'
    destination_file = 'folder2/destination-file.txt'

    # Create an S3 client
    s3 = boto3.client('s3')

    try:
        # Copy the file within the same bucket
        s3.copy_object(
            Bucket=destination_bucket,
            CopySource={'Bucket': source_bucket, 'Key': source_file},
            Key=destination_file
        )
        return {
            'statusCode': 200,
            'body': 'File copied successfully.'
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': f'Error: {str(e)}'
        }
