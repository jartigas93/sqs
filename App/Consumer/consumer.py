import boto3
import json
from App.functions import functions as fn
import argparse

sqs = boto3.client("sqs")


def receive_message(queue_url):
    response = sqs.receive_message(
        QueueUrl=queue_url,
        MaxNumberOfMessages=10,
        WaitTimeSeconds=10,
    )

    for message in response.get("Messages", []):
        message_body = message["Body"]
        print(f"Message body: {json.loads(message_body)}")


        response = sqs.delete_message(
            QueueUrl=queue_url,
            ReceiptHandle=message["ReceiptHandle"],
        )
        print(f"Deleted message: {message['MessageId']}")


def main(args):
    myQueue = args.queue

    listqueues = fn.listqueues(sqs, myQueue)
    if listqueues:
        print("Queue already exists.")
        queueUrl = fn.getqueue(myQueue, sqs)
        receive_message(queueUrl["QueueUrls"][0])

    print("-" * 40)
    print("Finish process")
    print("-" * 40)


if __name__ == '__main__':
    argparser = argparse.ArgumentParser()
    argparser.add_argument('--queue', help='Queue name', default="sqs-demo")
    args = argparser.parse_args()

    main(args)
