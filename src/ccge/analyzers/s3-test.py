#!/usr/bin/env python3

import json

import boto3
from botocore.exceptions import ClientError

client = boto3.client("s3")

try:
    response = client.list_buckets()
    # loop thru buckets and extract bucket names
    bucket_names = []
    for bucket in response["Buckets"]:
        bucket_names.append(bucket["Name"])
except Exception as e:
    print(f"No credentials detected or error is {e}")


def check_public_access(bucket):
    try:
        response = client.get_public_access_block(Bucket=bucket)
        config = response["PublicAccessBlockConfiguration"]
        if all(config.values()):
            print(
                "All bucket configurations are NOT set to public (Everything is safely set to true)"
            )
        else:
            print("Bucket is potentially public")
        print(json.dumps(config, indent=2, default=str))

    except ClientError as e:
        print(f"Error: {e}")


for bucket in bucket_names:
    print(f"S3 Bucket Public Configurations for Bucket Name: {bucket}")
    check_public_access(bucket)
