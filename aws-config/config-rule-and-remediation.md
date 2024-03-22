# Create an AWS Config rule and remediation - removes any SG rules that have 0.0.0.0/0 as a source unless they use TCP port 80

1. Create an IAM role with a custom trust policy for Systems Manager and add the 'AmazonSSMAutomationRole' policy
2. Add an inline policy to the role with the JSON from the 'automation-iam-role.json' document
3. Create a config rule using the 'pc-sg-open-only-to-authorized-ports' managed rule
4. Add port 80 next to 'authorizedTcpPorts'
5. Add a remediation rule using the automatic action 'AWS-DisablePublicAccessForSecurityGroup'
6. For Resource ID parameter specify 'GroupId'
7. For IpAddressToBlock specify '0.0.0.0/0'
8. For AutomationAssumeRole specify the ARN of the role created earlier