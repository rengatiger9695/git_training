import boto3
s3_object= boto3.resource('s3')
for i in s3_object.buckets.all():
    print (i.name)