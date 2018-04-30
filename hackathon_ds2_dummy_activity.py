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


partGroup = ds2.groupby(['ProspectID'])['Activity'].agg('count')
avgAct = partGroup.mean()
dumAct = pd.pivot_table(ds2, index='ProspectID', columns='Activity', aggfunc=lambda x: 1, fill_value=0)