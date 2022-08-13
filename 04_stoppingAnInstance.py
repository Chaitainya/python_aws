# Stopping instance || instances

import boto3
ec2 = boto3.resource('ec2')
ids = ['i-06441158abf760eaf', 'i-081343f82001a599a']
ec2.instances.filter(InstanceIds = ids).stop()
print("Instance stopped")