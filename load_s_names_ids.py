import requests
import os
import time
import json
from dotenv import load_dotenv
load_dotenv()

BASE_URL = os.environ.get('BASE_URL')
API_KEY = os.environ.get('API_KEY')

page = 0
per_page = 100

s_names_ids = []

while True:
  request_string = BASE_URL + f"?api_key={API_KEY}&page={page}&per_page={per_page}"
  print("\nrequest_string: \n", request_string, "\npage:\n", page)

  response = requests.get(request_string)
  print("\nresponse: \n", response)
  
  if response.status_code == 200:
    print("==============200================200====================200", response.status_code)
    data = response.json()
    results = data['results']
    pagination = data['metadata']
    total = pagination['total']
    print("\npagination: \n", pagination, "\nresults length: \n", len(results))

    if(len(s_names_ids) >= total):
      break

    for school in results:
      print(school['school']['name'])
      s_names_ids.append({
        "name": school['school']['name'],
        "id": school['id']
      })
    print("\nlength: \n", len(s_names_ids))
    page+=1

  time.sleep(3)

print("length:\n", len(s_names_ids), "final: \n", s_names_ids)

with open('s_names_ids.json', 'w') as f:
  json.dump(s_names_ids, f, ensure_ascii=False, indent=4)
