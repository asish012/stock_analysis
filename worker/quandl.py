import quandl
quandl.ApiConfig.api_key = 'GTCmp7ssw2WwwyFmkFnq'
# quandl.ApiConfig.api_version = '2015-04-09'

data = quandl.get('NSE/ABMD')

print(data)