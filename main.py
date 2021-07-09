from flask import Flask, request
import os
from dotenv import load_dotenv
load_dotenv()
from api import querySchools

app = Flask(__name__)


@app.route('/school/<int:id>')
def getSchoolById(id):
  """ GET school by int id """
  queryStr = f"&id={id}"
  data = querySchools(queryStr=queryStr)

  return { "data": data[0] }



@app.route('/school')
def getSchoolsByQuery():
  """ GET request for schools by query with ability to select only certain data """
  queryStr = request.query_string.decode("utf-8")
  
  if "select" in queryStr:

    selectedData = []
    
    queryStr = queryStr.split("&")
    
    select = list(filter(lambda x: "select" in x, queryStr))[0]
    select = select.split("=")[1:][0].split(",")

    queryStr = list(filter(lambda x: "select" not in x, queryStr))
    
    queryStr = "&" + "&".join(queryStr)

    queryResult = querySchools(queryStr)
    
    if queryResult:
      for school in queryResult["results"]:
        modifiedResult = {}
        modifiedResult["id"] = school["id"]
        for field in select:
          if field in school:
            modifiedResult[field] = school[field]
        selectedData.append(modifiedResult)
    
    return { "data": {"metadata": queryResult["metadata"], "results": selectedData} }
  else:

    queryResult = querySchools(queryStr)
    return { "data": queryResult }
    


    



if __name__ == "__main__":
  app.run(debug=True)