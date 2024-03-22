# On an EC2 instance, install the following utilities

## PIP
curl -O https://bootstrap.pypa.io/get-pip.py
python3 get-pip.py --user
## Redis
pip install redis


# Create a Python script with the following code

```python
import redis

# Replace `your-endpoint` with the endpoint of your ElastiCache cluster, which you can find in the AWS console
cache = redis.StrictRedis(host='your-endpoint', port=6379, db=0)

# Storing a value in the cache
cache.set('my-cached-key', 'my-cached-value')

# Retrieving a value from the cache
value = cache.get('my-cached-key')

# Decoding the bytes literal to a string
decoded_value = value.decode('utf-8')
print(decoded_value)
```
