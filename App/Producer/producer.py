import boto3
from botocore.exceptions import ClientError
import json
from App.functions import functions as fn
import argparse

sqs = boto3.client("sqs")

def public_message(queue):
    try:

        for i in range(10):
            message_body = json.dumps({"task": "task" + str(i)})
            response = sqs.send_message(QueueUrl=queue.get('QueueUrl'),MessageBody=message_body)
            print(f"Sent message {message_body} to queue")

    except ClientError as error:
        print("Couldn't send message to queue %s.", queue.url)
        raise error
    else:
        print(
            "Sent message to %s. Message ID: %s",
            queue.get('QueueUrl'), response.get("MessageId"),
        )
    return response    

def main(args):

    queue = fn.getqueue(args.queue,sqs)
    public_message(queue)

    print("-" * 40)
    print("Finish process")
    print("-" * 40)

if __name__ == '__main__':
    argparser = argparse.ArgumentParser()
    argparser.add_argument('--queue', help='Queue name', default="sqs-demo")

    args = argparser.parse_args()

    main(args)
