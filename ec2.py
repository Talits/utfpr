import boto3
ec2 = boto3.resource('ec2')

instances = ec2.create_instances(
        ImageId="ami-053b0d53c279acc90",
        MinCount=1,
        MaxCount=1,
        InstanceType="t2.micro",
        KeyName="talitaaula"
    )

