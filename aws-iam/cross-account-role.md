# Create a role in the target account

1. Select 'another account' as the trusted entity
2. Enter the account ID and check the 'Require external ID' checkbox
3. Enter the external ID
4. Attach the following policy to the role:

{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "AllowBucketAccess",
            "Effect": "Allow",
            "Action": [
                "s3:GetObject",
                "s3:PutObject",
                "s3:ListBucket"
            ],
            "Resource": [
                "arn:aws:s3:::<bucket-name>",
                "arn:aws:s3:::<bucket-name>/*"
            ]
        }
    ]
}

# Assume the role in the target account

1. Run the following command to assume the role using the CLI

aws sts assume-role --role-arn arn:aws:iam::<target-account-id>:role/<role-name> --role-session-name mysession --external-id <external-id>

2. Configure the credentials

aws configure set aws_access_key_id <access-key-id> --profile target-account
aws configure set aws_secret_access_key <secret-access-key> --profile target-account
aws configure set aws_session_token <session-token> --profile target-account

3. Run CLI commands against the bucket

aws s3 ls s3://<bucket-name> --profile target-account
