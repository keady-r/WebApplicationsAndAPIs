# Write a program in python that will read a file from a repository, 

import requests
import json

filename = "repo-public.json"
url = "https://api.github.com/repos/keady-r/data-representation-coursework"

response = requests.get(url)
print(response.status_code)
repoJSON = response.json()


with open (filename, "w") as fp:
    json.dump(repoJSON, fp, indent=4)