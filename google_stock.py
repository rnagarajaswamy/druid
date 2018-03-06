import pandas_datareader.data as web
import datetime


date = datetime.strptime('26 Sep 2012', '%d %b %Y')
newdate = date.replace(hour=11, minute=59)




start = datetime.datetime(2017, 1, 1)

end = datetime.datetime(2017, 1, 15)

f = web.DataReader("XPO", 'google', start, end)

f.iloc['2017-01-04']