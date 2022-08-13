# Terminating instance

import boto3
ec2 = boto3.resource("ec2")
instance_id = "i-0cbfef4dbde19186f"
instance = ec2.Instance(instance_id)
response = instance.terminate()
print(response)