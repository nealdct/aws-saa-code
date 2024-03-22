## PIP
curl -O https://bootstrap.pypa.io/get-pip.py
python3 get-pip.py --user
## boto3
pip install boto3

## Create a Python script with the following code

```python
import boto3

# Initialize the KMS client
kms = boto3.client('kms', region_name='us-east-1')

# The ID or ARN of your KMS key (you can get it from the AWS console)
key_id = 'arn:aws:kms:us-east-1:676238238199:key/e1de5166-f54a-4fc9-835d-1234da4dd743'

# Data to be encrypted
plaintext = 'This is a secret message'

# Encrypt the data
response = kms.encrypt(
    KeyId=key_id,
    Plaintext=plaintext,
    EncryptionAlgorithm='SYMMETRIC_DEFAULT'
)

# Get the ciphertext blob
ciphertext_blob = response['CiphertextBlob']

# Save the encrypted data to a file
with open('encrypted_data', 'wb') as encrypted_file:
    encrypted_file.write(ciphertext_blob)

print('Encrypted data saved to "encrypted_data" file.')

# Decrypt the data
decrypt_response = kms.decrypt(
    CiphertextBlob=ciphertext_blob,
    KeyId=key_id
)

# Get the plaintext back
decrypted_plaintext = decrypt_response['Plaintext'].decode('utf-8')

# Save the decrypted data to a file
with open('decrypted_data.txt', 'w') as decrypted_file:
    decrypted_file.write(decrypted_plaintext)

print('Decrypted data saved to "decrypted_data.txt" file.')
```
