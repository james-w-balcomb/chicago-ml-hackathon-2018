import pandas as pd
import numpy as np
import datetime

path = r"C:\Users\PButler\Desktop\hackathon"
file1 = path + "\\" + 'DataSet1__24Apr2018' + ".txt"
file2 = path + "\\" + 'DataSet2_24Apr2018' + ".txt"
file3 = path + "\\" + 'DataSet3__24Apr2018' + ".txt"
file4 = path + "\\" + 'DataSet4__24Apr2018' + ".txt"

ds1 = pd.read_table(file1, header=0, sep=' ')
ds2 = pd.read_table(file2, header=0, sep=' ')
ds3 = pd.read_table(file3, header=0, sep=' ')
ds4 = pd.read_table(file4, header=0, sep=' ')


ds3.lifedur = ds3.loc[ds3['dtmoveout'].notnull()]

ds3.lifedur['movein'] = pd.to_datetime(ds3['dtmovein'], format = '%m/%d/%Y')
ds3.lifedur['moveout'] = pd.to_datetime(ds3['dtmoveout'], format = '%m/%d/%Y')

ds3.lifedur['lttime'] = ds3.lifedur.moveout - ds3.lifedur.movein
avgduration = ds3.lifedur.lttime.mean()

#ds4counts = ds4.RateType.value_counts()
#ds4group = ds4.groupby(['RateType','ServiceType']).agg(['count'])

ds4['dailyAmt'] = ""

#ds4['dailyAmt'] = ds4.loc['RateType' == 'DLY','Amount']

ds4['dailyAmt'] = ds4.loc[ds4['RateType'] == 'DLY','Amount']

ds4['dailyAmt'] = ds4.loc[ds4['RateType'] == 'MLY','Amount']/30.42

avgRev = ds4['dailyAmt'].mean()

#ltv = avgduration * avgRev
print avgduration
print avgRev
#print ltv
