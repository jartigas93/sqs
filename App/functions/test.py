import boto3
from botocore.exceptions import ClientError

sqs = boto3.client("sqs")


def listqueues(sqs, name):
    try:
        response = sqs.list_queues(QueueNamePrefix=name)
        if response.get('QueueUrls', []):
            print("Found queues with prefix '%s': %s", name, response)
            return response
        # else:
        #     print("No queues found with that name prefix.")
        #     return None

    except ClientError as error:
        print("Couldn't list queues.", name)
        raise error


listqueues(sqs, "amiguitennnnnnn")
# getqueue("sqs-demo",sqs)