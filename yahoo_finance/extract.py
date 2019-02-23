import requests , json , time , datetime

# https://query1.finance.yahoo.com/v8/finance/chart/GE?symbol=GE&period1=1507950000&period2=1529377200&interval=1d&includePrePost=true&events=div|split|earn&lang=en-US&region=US&crumb=nZkcdAUvq.D&corsDomain=finance.yahoo.com

simbolo = input('ingrese el simbolo: ')
desde = input('ingrese desde que fecha quiere descargar los datos (dd/mm/aaaa): ')
hasta = input('ingrese hasta que fecha quiere descargar los datos (dd/mm/aaaa); ')
desde = str(int(time.mktime(datetime.datetime.strptime(desde, "%d/%m/%Y").timetuple())))
hasta = str(int(time.mktime(datetime.datetime.strptime(hasta, "%d/%m/%Y").timetuple())))
headers = {
    'symbol':simbolo,
    'period1':desde,
    'period2':hasta,
    'interval':'1d',
    'includePrePost':'true',
    'events':'div|split|earn',
    'lang':'en-US',
    'region':'US',
    'crumb':'nZkcdAUvq.D',
    'corsDomain':'finance.yahoo.com'
    }

url =  'https://query1.finance.yahoo.com/v8/finance/chart/'+simbolo+'?symbol='+simbolo+'&period1='+desde+'&period2='+hasta+'&interval=1d&includePrePost=true&events=div|split|earn&lang=en-US&region=US&crumb=nZkcdAUvq.D&corsDomain=finance.yahoo.com'
r = requests.get(url=url, headers=headers)
with open(simbolo+'.json', 'w') as file:
    file.write(r.text)
#print(r.text)
