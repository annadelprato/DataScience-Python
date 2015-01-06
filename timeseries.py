import pandas as pd
import numpy as np 
from scipy import stats
import matplotlib.pyplot as plt
import statsmodels.api as sm


df = pd.read_csv('LoanStats3b.csv', header=1, low_memory=False)

#clean up 
df.dropna(inplace=True)
# ex: df.fillna(df.mean())

#df['int_rate']=df['int_rate'].str.replace('%'," ")

# converts string to datetime object in pandas:
df['list_d_format'] = pd.to_datetime(df['list_d']) 
dfts = df.set_index('list_d_format') 
#year_month_summary = dfts.groupby(lambda x : x.year+x.month).count()
year_month_summary = dfts.groupby(lambda x : x.year*100+x.month).count()
loan_count_summary = year_month_summary['list_d']
#montly data for 1 year

#print df['list_d_format'][0:50]
#print df['int_rate'][0:50]

#not sure how 'total_acc' column is specified with above syntax

#print [loan_count_summary]

#plotting
loan_count_summary.plot(label='loan counts')
plt.legend()
plt.show()
fig = plt.figure(figsize=(12,8))
ax1 = fig.add_subplot(211)
fig = sm.graphics.tsa.plot_acf(loan_count_summary.values.squeeze())
ax2 = fig.add_subplot(212)
fig = sm.graphics.tsa.plot_pacf(loan_count_summary)
plt.show()

#notes
#notes: data is not stationary - large fluctuations and increasing trend observed
# data needs to be "differenced" before proceeding i.e., subtraction of the current observations from previous ones. Differencing removes the trend.

#syntax needed to continue with modeling
#Also, not sure if correct data columns are bing used. The exercise instruction do not state column names explicitly.