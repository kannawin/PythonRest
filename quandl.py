import quandl

api_key = 'LrpdsDS_QoC_2z_BbHoS'
reference = 'CHRIS/MGEX_IH1'

quandl.ApiConfig.api_key = api_key

quandl.get(reference)
