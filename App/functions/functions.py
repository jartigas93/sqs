import boto3
from botocore.exceptions import ClientError

def getqueue(name,sqs):

    try:
        response = listqueues(sqs, name)
        if not response:
            print("Queue '%s' does not exist. Creating queue '%s'...", name)
            new_queue = createqueue(name, sqs)
        
            print("Got queue '%s' with URL=%s", name, new_queue['QueueUrl'])
            return new_queue

        else:
            print("Found queues with prefix '%s': %s", name, response)
            return response

    except ClientError as error:
        print("Couldn't get queue named %s.", name)
        raise error

def listqueues(sqs, name):
    try:
        response = sqs.list_queues(QueueNamePrefix=name)
        if response.get('QueueUrls', []):
            return response
        else:
            print("No queues found with that name prefix.")
            return None

    except ClientError as error:
        print("Couldn't list queues.", name)
        raise error


def createqueue(name,sqs):
    try:
        response = sqs.create_queue(
                    QueueName=name,
                    Attributes={
                        'VisibilityTimeout': '60',
                        'MessageRetentionPeriod': '7200',
                        'DelaySeconds': '0',
                        'ReceiveMessageWaitTimeSeconds': '20',
                    })
        print("Created queue '%s' with URL=%s", name, response['QueueUrl'])
        return response

    except ClientError as error:
        print("Couldn't create queue named %s.", name)
        raise error
