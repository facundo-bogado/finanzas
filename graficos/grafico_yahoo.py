import requests , json
from datetime import datetime
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.dates import MONDAY, DateFormatter, DayLocator, WeekdayLocator
from mpl_finance import candlestick_ohlc

#------------------------------------------------------------------------------

def get_data(stock):
    #interval = input( 'Ingrese el intervalo:\n(1d=day,60m=minute,5m,30m,1w=week(semanal)) etc..:  ')
    now = str(requests.get( 'https://www.invertironline.com/api/cotizaciones/server_time').text)
    headers = {
        'symbol': stock,
        'period1':'1519551261',
        'period2':now,
        'interval':'1d',
        'includePrePost': 'true',
        'events': 'div|split|earn',
        'lang': 'en-US',
        'region': 'US',
        'crumb': 'egtzDEXtY7T',
        'corsDomain':'finance.yahoo.com'
        }
    url = 'https://query1.finance.yahoo.com/v8/finance/chart/'+stock+'?symbol='+stock+'&period1=1519551261&period2='+now+'&interval=1d&includePrePost=true&events=div%7Csplit%7Cearn&lang=en-US&region=US&crumb=egtzDEXtY7T&corsDomain=finance.yahoo.com'
    request = json.loads(requests.get(url,headers=headers).text)
    data = request
    tabla = data['chart']['result'][0]['indicators']['quote'][0]
    dates = []
    for datestamps in data['chart']['result'][0]['timestamp']:
        date = datetime.fromtimestamp(datestamps).strftime('%Y-%m-%d')
        dates.append(date)
    tabla['date'] = dates #a['chart']['result'][0]['timestamp']
    tabla['Adj Close'] = data['chart']['result'][0]['indicators']['adjclose'][0]['adjclose']
    quotes = pd.DataFrame(tabla , columns=['date','open','high', 'low', 'close','Adj Close','volume'])
    #print(quotes)
    quotes.to_csv(stock+'.csv',index=False)
    mondays = WeekdayLocator(MONDAY)        # major ticks on the mondays
    alldays = DayLocator()              # minor ticks on the days
    weekFormatter = DateFormatter('%b %d')  # e.g., Jan 12
    dayFormatter = DateFormatter('%d')      # e.g., 12
    quotes = pd.read_csv(stock+'.csv', #'data/yahoofinance-INTC-19950101-20040412.csv',
                        index_col=0,
                        parse_dates=True,
                        infer_datetime_format=True)
    fig, ax = plt.subplots()
    fig.subplots_adjust(bottom=0.2)
    ax.xaxis.set_major_locator(mondays)
    ax.xaxis.set_minor_locator(alldays)
    ax.xaxis.set_major_formatter(weekFormatter)
    ax.grid(True)
    candlestick_ohlc(ax, zip(mdates.date2num(quotes.index.to_pydatetime()),
                            quotes['open'], quotes['high'],
                            quotes['low'], quotes['close']),
                            width=0.6,colorup='g')
    ax.xaxis_date()
    ax.autoscale_view()
    plt.suptitle(stock)
    plt.setp(plt.gca().get_xticklabels(), rotation=45, horizontalalignment='right')
    plt.show()


stocks = []
cuantas = int(input('Cuantas acciones desea consultar?  '))
n = 0
while n <= cuantas:
    stck = input('Ingrese el simbolo (fuente: yahoo finance):  ')
    stocks.append(stck)
    n+=1
for stock in stocks:
    get_data(stock)
