import quandl
import pandas
import requests
import json

api_key = 'LrpdsDS_QoC_2z_BbHoS'
reference = 'CHRIS/MGEX_IH1'

##url for a date range
url = 'https://www.quandl.com/api/v3/datasets/?start_date={}&end_date={}&api_key={}'.format(reference,'2018-04-30','2018-04-30',api_key)

##url for a blind grab (get all data)
url1 = 'https://www.quandl.com/api/v3/datasets/{}?api_key={}'.format(reference, api_key)

##gets the data from the API and loads in into JSON form
request = requests.get(url1)
r = json.loads(request.content)

##Creates an array of the column names
dataSet = {}
columns = r['dataset']['column_names']
for s in columns:
  dataSet[s] = []

## Goes through each line in the data sent back and puts it into a dictionary in the form of {'col1':[data], 'col2':[data], ... }
for i in r['dataset']['data']:
  for j in range(0,len(i)):
    dataSet[columns[j]].append(i[j])

#creates dataframe
df = pandas.DataFrame(dataSet)

#do work with dataframe here
