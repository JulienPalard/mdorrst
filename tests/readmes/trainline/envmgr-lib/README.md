# envmgr-lib

```bash
# Get all AMIs
amis = AMI.get_all()

# Create an ASG instance
asg = ASG('my-asg-name', 'PROD')

# Check the remote ASG exists
asg_exists = asg.exists()

# Get the ASG schedule
asg_schedule = asg.get_schedule()

# Set the ASG schedule
asg.set_schedule('ON')

# Get ASG status
status = asg.get_status()

# Get ASG health
health = asg.get_health()

# Get instances with AMI older than certain age
instances = Instance.get_instances_by_ami_age(30)

# Create a Service instance
service = Service('MyService', 'PROD')

# Get Service health
health = service.get_health()

# Get inactive slices:
slices = service.get_slices(False)

# Publish an open file handle as version 2.0.0 of the service
service.publish(file, '2.0.0')

# Deploy the service
deploy_id = service.deploy()

#Get the deployment info
service.get_deployment()

# Toggle the service and get toggle status
upstream = service.toggle()
status = upstream.get_status()

```

