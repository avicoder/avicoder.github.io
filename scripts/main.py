# author :  avicoder

import requests
import json
from datetime import datetime
from os import path

now = datetime.utcnow()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

API_JSON = path.join(path.dirname(__file__),'../api/mailproviders.json',)

res = requests.get("https://gist.githubusercontent.com/ammarshah/f5c2624d767f91a7cbdc4e54db8dd0bf/raw/660fd949eba09c0b86574d9d3aa0f2137161fc7c/all_email_provider_domains.txt",stream=True)

output ={}
result = []

for r  in res.iter_lines():
	result.append(r.decode("utf-8"))


output.update({"result":result, "last_updated":dt_string, "readme":"list of Free email providers", "author":"avicoder"})


with open(API_JSON, 'w') as outfile:
    json.dump(output, outfile, indent=4)


file1 = open('myfile.txt', 'w')
L = ["This is Delhi \n", "This is Paris \n", "This is London \n"]
s = "Hello\n"
  
# Writing a string to file
file1.write(s)
  
# Writing multiple strings
# at a time
file1.writelines(L)
  
# Closing file
file1.close()
  

