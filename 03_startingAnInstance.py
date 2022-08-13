# Starting instance or instances

import boto3
client = boto3.client('ec2', region_name='ap-south-1b')
client.start_instances( InstanceIds = ['i-06441158abf760eaf', 'i-081343f82001a599a'], DryRun = True )

# still under construction