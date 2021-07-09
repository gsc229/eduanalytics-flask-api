from flask import Flask, request
import os
from dotenv import load_dotenv
load_dotenv()
from flask_cors import CORS
from api import querySchools

app = Flask(__name__)
CORS(app)

@app.route('/school/<int:id>')
def getSchoolById(id):
  """ GET school by int id """
  queryStr = f"&id={id}"
  data = querySchools(queryStr=queryStr)

  return { "data": data[0] }


@app.route('/school')
def getSchoolsByQuery():
  """ GET request for schools by query with ability to select only certain data nested up to four levels deep"""
  queryStr = request.query_string.decode("utf-8")

  queryStr_has_select = "select" in queryStr

  queryStr = queryStr.split("&")
  
  select = list(filter(lambda x: "select" in x, queryStr))[0] if queryStr_has_select else None
  select = select.split("=")[1:][0].split(",") if queryStr_has_select else None

  queryStr = list(filter(lambda x: "select" not in x, queryStr))
  
  queryStr = "&" + "&".join(queryStr)

  queryResult = querySchools(queryStr)

  return { "data": queryResult }


if __name__ == "__main__":
  app.run(debug=True)