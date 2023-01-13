import boto3


def lambda_handler(event, context):
    glue_jobs =	{
        "zips.json": "zipsjsonjob",
        "us-500.csv": "us-500job",
        "bank-full.csv": "bank-fullcsvjob",
        "vehicle.csv": "vehiclecsvjob",
        "transactions.csv":"transactionscsvjob",
        "aadhar.csv":"aadharcsvjob"
        }
        
    file_name = event['Records'][0]['s3']['object']['key']
    bucketName=event['Records'][0]['s3']['bucket']['name']
    print("File Name : ",file_name)
    print("Bucket Name : ",bucketName)
    glue=boto3.client('glue');
    
    if file_name == "zips.json":
        response = glue.start_job_run(JobName = glue_jobs[file_name])
        print("Run {}".format(glue_jobs[file_name]))
    
    elif file_name == "us-500.csv":
        glue=boto3.client('glue');
        response = glue.start_job_run(JobName = glue_jobs[file_name])
        print("Run {}".format(glue_jobs[file_name]))
    
    elif file_name == "bank-full.csv":
        glue=boto3.client('glue');
        response = glue.start_job_run(JobName = glue_jobs[file_name])
        print("Run {}".format(glue_jobs[file_name]))
        
    elif file_name == "vehicle.csv":
        glue=boto3.client('glue');
        response = glue.start_job_run(JobName = glue_jobs[file_name])
        print("Run {}".format(glue_jobs[file_name]))
    
    elif file_name == "transactions.csv":
        glue=boto3.client('glue');
        response = glue.start_job_run(JobName = glue_jobs[file_name])
        print("Run {}".format(glue_jobs[file_name]))
    
    elif file_name == "aadhar.csv":
        glue=boto3.client('glue');
        response = glue.start_job_run(JobName = glue_jobs[file_name])
        print("Run {}".format(glue_jobs[file_name]))
