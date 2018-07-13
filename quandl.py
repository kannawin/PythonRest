import quandl
import pandas
import numpy

api_key = 'LrpdsDS_QoC_2z_BbHoS'
reference = 'CHRIS/MGEX_IH1'

##sets you API KEY
quandl.ApiConfig.api_key = api_key

##quandl.get retrieves the data, it already comes in the form of a pandas dataframe
df = pandas.DataFrame(quandl.get(reference))

##Do what you need here with the data frame
