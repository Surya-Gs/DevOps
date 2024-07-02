# Get PR information on a repo using python
import requests

response=requests.get("https://api.github.com/applications")

print(response[0])
