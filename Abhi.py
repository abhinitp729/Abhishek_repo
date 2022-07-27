import boto3
company = boto3.client('sqs',region_name='us-east-1',aws_access_key_id="xyz",aws_secret_access_key="xyz1"
queue=company.create_queue(QueueName='sqswfdataartest.fifo', Attributes={'DelaySeconds':'0','VisibilityTimeout':'15','MessageRetentionPeriod':'28880','MaximumMessageSize':'10000','FifoQueue':'true'})
