# author :  avicoder

import requests
import json
from datetime import datetime

now = datetime.utcnow()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

res = requests.get("https://gist.githubusercontent.com/ammarshah/f5c2624d767f91a7cbdc4e54db8dd0bf/raw/660fd949eba09c0b86574d9d3aa0f2137161fc7c/all_email_provider_domains.txt",stream=True)

output ={}
result = []

for r  in res.iter_lines():
	result.append(r.decode("utf-8"))


output.update({"result":result, "last_updated":dt_string, "readme":"list of Free email providers", "author":"avicoder"})

out_file = open("providers.json", "w")
json.dump(output,out_file, indent = 4, sort_keys = False)
out_file.close()

