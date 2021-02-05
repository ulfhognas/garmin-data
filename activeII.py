import pandas as pd
import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt
from activetime import get_time
from activetime import get_sec
from activedata import activedata
from activemean import activemean

mydata = activedata(Activity_Type = 'Strength Training', minutecutoff = 10)

print(mydata['Activity Type'].unique())

print(mydata['Title'].unique())

print(get_time(mydata['seconds'].mean()))

print(get_time(mydata['seconds'].sum()))
