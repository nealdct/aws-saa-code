AWSTemplateFormatVersion: '2010-09-09'
Description: Create an EC2 instance with a security group for SSH access
Resources:
  InstanceSecurityGroup:
    Type: AWS::EC2::SecurityGroup
    Properties:
      GroupDescription: Enable SSH access
      SecurityGroupIngress:
        - IpProtocol: tcp
          FromPort: 22
          ToPort: 22
          CidrIp: 0.0.0.0/0
  MyInstance:
    Type: AWS::EC2::Instance
    Properties:
      ImageId: ami-0440d3b780d96b29d
      InstanceType: t2.micro
      SecurityGroups:
        - !Ref InstanceSecurityGroup