import os
import requests
from flask_restful import abort
BASE_URL = os.environ.get('BASE_URL')
API_KEY = os.environ.get('API_KEY')
BASE_QUERY = f"{BASE_URL}?api_key={API_KEY}"

def querySchools(queryStr):
  """ queryStr should start with '&' and is contatinated with base url and api key ==> BASE_URL + ? api_key=API_KEY&school.city=Chicago  """
  print(f"{BASE_QUERY}{queryStr}")
  response = requests.get(f"{BASE_QUERY}{queryStr}")

  if response.status_code == 200:
    data = response.json()
    return data
  else:
    return abort(response.status_code)

