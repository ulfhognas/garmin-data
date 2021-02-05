import pandas as pd
import numpy as np
from activetime import get_time
from activetime import get_sec

def activemean(somedata, c1):
    if c1 not in somedata.columns:
        print('that is not a column')
        pass
    elif c1=='Time':
        mu = get_time(round(somedata['seconds'].mean()))
        return mu
    else:
        mu = somedata[c1].mean()
        return mu
