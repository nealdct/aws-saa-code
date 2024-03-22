# Import data
aws dynamodb batch-write-item --request-items file://estore-items.json

#### SCANS ####

# Perform scan of ProductOrders table:
aws dynamodb scan --table-name estore

#### QUERIES ####

# Use Key-Conditions Parameter:
aws dynamodb query  --table-name estore --key-conditions '{ "clientid":{ "ComparisonOperator":"EQ", "AttributeValueList": [ {"S": "harold@example.org"} ] } }'