from flask import Flask, request, jsonify
import os
from dotenv import load_dotenv
load_dotenv()
from flask_cors import CORS
from api import querySchools
import re


app = Flask(__name__)
CORS(app)

def prepareQueryString(queryStr):
  queryStr = queryStr.decode("utf-8")
  queryStr = queryStr.split("&")
  queryStr = "&" + "&".join(queryStr)
  return queryStr

@app.route('/schools/<int:id>')
def getSchoolById(id):
  """ GET school by int id """
  queryStr = f"&id={id}"
  data = querySchools(queryStr=queryStr)
  
  return { "data": data[0] }


@app.route('/schools/')
def getSchoolsByQuery():
  """ GET request for schools by query ex. ?school.name="School Name"&school.degrees_awarded.predominant=2,3&_fields=school.name,school.size"""
  queryStr = prepareQueryString(request.query_string)

  queryResult = querySchools(queryStr)

  return queryResult

@app.route('/earnings-chart-data/<int:id>')
def getEarningsChartData(id):
  """ Retuns 3, 6, 7, 8, 9, & 10 year-after-entry mean earnings prepared as chart data for a single school in the shape needed for bar chart"""
  queryStr = f"&keys_nested=true&fields=school.name,id,latest.earnings&id={id}"
  queryResult = querySchools(queryStr)
  earningsResult = queryResult["results"][0]["latest"]["earnings"]
  
  earningSegments = [
  "lowest_tercile",
  "middle_tercile",
  "highest_tercile",
  "female_students",
  "male_students",
  '10th_percentile_earnings',
  "25th_percentile_earnings",
  "75th_percentile_earnings",
  "90th_percentile_earnings"
  ]

  earnings = []
  # looking for keys with 10_yrs_after_entry 9_yrs_after_entry, etc.
  for key, value in earningsResult.items():

    if key.find("yrs_after_entry") != -1:
      # some yrs_after_entry 
      if "mean_earnings" in value:
          earningsObjet = {}
          earningsObjet["years_after_entry"] = key

          # some mean_earnings fields are just numbers
          if type(value["mean_earnings"]) == int:
            earningsObjet["mean_earnings"] = value["mean_earnings"]
            earnings.append(earningsObjet)
          if type(value["mean_earnings"]) == dict:
            for key2, value2 in value["mean_earnings"].items():
              if key2 in earningSegments:
                earningsObjet[key2] = value2
            earnings.append(earningsObjet)

  return { 
    "earnings": earnings,
    "id": id,
    "name": queryResult["results"][0]["school"]["name"]
  }

if __name__ == "__main__":
  app.run(debug=os.environ.get('DEBUG') == "True")