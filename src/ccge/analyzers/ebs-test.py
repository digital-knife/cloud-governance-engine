#!/usr/bin/env python3

import json

import boto3

client = boto3.client("ec2")
response = client.describe_volumes()

# print(json.dumps(response, indent=2, default=str))
print("\n--- Volume Analysis ---")

unattached_volumes = []
attached_volumes = []

for volume in response["Volumes"]:
    volume_id = volume["VolumeId"]
    volume_info = {
        "VolumeId": volume_id,
        "Size": volume["Size"],
        "VolumeType": volume["VolumeType"],
        "State": volume["State"],
        "AvailabilityZone": volume["AvailabilityZone"],
    }

    if not volume["Attachments"]:
        unattached_volumes.append(volume_info)
        print(f"Unattached Volume found: {volume_id}")
    else:
        attachment = volume["Attachments"][0]
        volume_info["InstanceId"] = attachment.get("InstanceId", "Unknown")
        volume_info["AttachmentState"] = attachment.get("State", "Unknown")
        volume_info["Device"] = attachment.get("Device", "Unknown")
        attached_volumes.append(volume_info)
        print(
            f"Volume {volume_id} is {attachment.get('State')} to instance {attachment.get('InstanceId')} as {attachment.get('Device')}"
        )

print("\n--- Summary ---")
print(f"Total Volumes: {len(attached_volumes) + len(unattached_volumes)}")
print(f"Attached: {len(attached_volumes)}")
print(f"Unattached: {len(unattached_volumes)}")

if unattached_volumes:
    print("\nUnattached volumes for review:")
    print(json.dumps(unattached_volumes, indent=2))
