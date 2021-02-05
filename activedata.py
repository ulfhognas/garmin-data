import pandas as pd
from activetime import get_time
from activetime import get_sec, get_speed

def activedata(pathname = '/home/ulf/Documents/Activities.csv',
 Activity_Type = 'all',
 Title = 'all',
 minutecutoff = 'none'):

 mydata = pd.read_csv(pathname)
 mydata['seconds'] = mydata['Time'].apply(get_sec)
 #df['col_3'] = df.apply(lambda x: f(x.col_1, x.col_2), axis=1)
 mydata['speed'] = mydata.apply(lambda x: get_speed(x['seconds'],
                                                    x['Distance']),
                                axis = 1)
 mydata = pd.DataFrame(mydata)
 mydata['datenumber'] = pd.to_datetime(mydata['Date']).dt.strftime("%Y%m%d").astype(int)

 if minutecutoff != 'none':
     mydata = mydata[mydata['seconds'] >= minutecutoff * 60]
 if Activity_Type != 'all':
     mydata = mydata[mydata['Activity Type']==Activity_Type]
 if Title != 'all':
     mydata = mydata[mydata['Title']==Title]
 return(mydata)
