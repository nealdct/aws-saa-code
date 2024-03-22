## Create Image and Push to ECR Repository

Launch EC2 instance - Amazon Linux 2 AMI, t2.micro
Connect to instance using EC2 Instance Connect

Run the following commands on EC2:

sudo su
yum update
yum install docker
systemctl enable docker.service
systemctl start docker.service
docker pull nginx
docker images

Create an IAM role and use policy "ecr-allow-all.json"
Attach role to EC2 instance and then run the following commands (replace account number):

aws ecr create-repository --repository-name nginx --region us-east-1
docker tag nginx:latest 111111111111.dkr.ecr.us-east-1.amazonaws.com/nginx:latest
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 111111111111.dkr.ecr.us-east-1.amazonaws.com/nginx
docker push 111111111111.dkr.ecr.us-east-1.amazonaws.com/nginx:latest