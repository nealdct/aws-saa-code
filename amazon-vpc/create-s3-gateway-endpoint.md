# Create a Custom VPC

1. Create a VPC choosing the "VPC and more" option
2. Provide a name for the VPC, e.g. lab1-custom-vpc
3. No NAT Gateway
4. Use defaults for other selections
5. Modify the public subnets to auto assign IPv4 addresses

# Test the S3 Gateway Endpoint

1. Launch an instance in a public subnet of the VPC with S3 read only permissions
2. Connect to the instance using EC2 Instance Connect 
3. Run 'aws s3 ls' - you should receive a list of buckets
4. Edit the policy on the S3 gateway endpoint to change 'Allow' to 'Deny'
5. Run 'aws s3 ls' again - it should not have changed (should work)
6. Edit the S3 gateway endpoint to add the public route table
7. Run 'aws s3 ls' again - this time access should be denied
8. Revert the policy and it should start working again (via the S3 gateway endpoint)