import request

#api - endpoint
from django.contrib.sites import requests

# Making a GET request
r = requests.get('https://api.github.com / users / cooks-johns')

# check status code for response received
# success code - 200
print(r)

# print content of request
print(r.content)