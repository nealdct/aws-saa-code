# Created Nested Stack using the AWS CLI

1. Create a file named vpc.yaml with the following content

```yaml
AWSTemplateFormatVersion: '2010-09-09'
Resources:
  VPC:
    Type: AWS::EC2::VPC
    Properties:
      CidrBlock: 10.0.0.0/16
      EnableDnsSupport: true
      EnableDnsHostnames: true
      Tags:
        - Key: Name
          Value: NestedStackVPC
Outputs:
  VpcId:
    Description: VPC ID
    Value: !Ref VPC
```

2. Create a file named subnet1.yaml with the following content

```yaml
AWSTemplateFormatVersion: '2010-09-09'
Parameters:
  VpcId:
    Type: String
Resources:
  Subnet1:
    Type: AWS::EC2::Subnet
    Properties:
      AvailabilityZone: !Select [ 0, !GetAZs '' ]
      CidrBlock: 10.0.1.0/24
      VpcId: !Ref VpcId
      Tags:
        - Key: Name
          Value: NestedStackSubnet1
Outputs:
  Subnet1Id:
    Description: Subnet 1 ID
    Value: !Ref Subnet1
```

3. Create a file named subnet2.yaml with the following content

```yaml
AWSTemplateFormatVersion: '2010-09-09'
Parameters:
  VpcId:
    Type: String
Resources:
  Subnet2:
    Type: AWS::EC2::Subnet
    Properties:
      AvailabilityZone: !Select [ 1, !GetAZs '' ]
      CidrBlock: 10.0.2.0/24
      VpcId: !Ref VpcId
      Tags:
        - Key: Name
          Value: NestedStackSubnet2
Outputs:
  Subnet2Id:
    Description: Subnet 2 ID
    Value: !Ref Subnet2
```

4. Upload the vpc.yaml, subnet1.yaml, and subnet2.yaml files to an S3 bucket and retrieve the URLs

aws s3 cp <file-name> s3://<bucketname>

aws s3api list-objects --bucket my-cloudformation-s3-bucket-3121s2 --query "Contents[].{Key: Key}" --output text | awk '{ print "https://my-cloudformation-s3-bucket-3121s2.s3.amazonaws.com/" $1 }'

5. Create a file named main.yaml with the following content (replace your-bucket-name with the name of the S3 bucket where you uploaded the templates)

```yaml
AWSTemplateFormatVersion: '2010-09-09'
Resources:
  VPCStack:
    Type: AWS::CloudFormation::Stack
    Properties:
      TemplateURL: https://my-cloudformation-s3-bucket-3121s2.s3.amazonaws.com/vpc.yaml

  Subnet1Stack:
    Type: AWS::CloudFormation::Stack
    Properties:
      TemplateURL: https://my-cloudformation-s3-bucket-3121s2.s3.amazonaws.com/subnet1.yaml
      Parameters:
        VpcId: !GetAtt VPCStack.Outputs.VpcId

  Subnet2Stack:
    Type: AWS::CloudFormation::Stack
    Properties:
      TemplateURL: https://my-cloudformation-s3-bucket-3121s2.s3.amazonaws.com/subnet2.yaml
      Parameters:
        VpcId: !GetAtt VPCStack.Outputs.VpcId
```

7. Deploy the main stack using the AWS CloudFormation CLI

aws cloudformation create-stack --stack-name NestedStackExample --template-body file://main.yaml --capabilities CAPABILITY_NAMED_IAM

8. The stack can be deleted with the following command

aws cloudformation delete-stack --stack-name NestedStackExample