import boto.ec2
import sys
#sets region, grabs ec2 creds from the ~/.boto config file. 
conn = boto.ec2.connect_to_region("us-west-2")