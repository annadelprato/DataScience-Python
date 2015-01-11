#multivariate.py

##File clean up
#imports
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import statsmodels.api as sm

#file import
df=pd.read_csv('LoanStats.csv', dtype=str, header=1)

#cleaning up the columns

df.dropna(inplace=True)

df['int_rate']=df['int_rate'].str.replace('%'," ")

df['home_ownership'] = df['home_ownership'].apply(lambda x: '1' if x == 'RENT' else '0')

#printing again to see if cleaning took 
print df['int_rate'][0:50]
print df['annual_inc'][0:50]
print df['home_ownership'][0:50]

df.to_csv('LoanStatsclean.csv')


# Modeling 

#import pandas as pd
#import matplotlib.pyplot as plt
#import numpy as np
#import statsmodels.api as sm

df=pd.read_csv('LoanStatsclean.csv')
		

#plot histogram
plt.figure()
p=df['int_rate'].hist()
plt.show()

#plot histogram
plt.figure()
p=df['home_ownership'].hist()
plt.show()

#plot histogram
plt.figure()
p=df['annual_inc'].hist()
plt.show()

#scatter plot matrix works if 'int_rate' is changed from float
#a=pd.scatter_matrix(df, alpha=0.05, figure=(10,10), diagonal='hist')
#plt.show()

int_rate = df['int_rate']
annual_inc = df['annual_inc']
home_ownership = df['home_ownership']

# The dependent variable
y = np.matrix(int_rate).transpose()
# The independent variables shaped as columns
x1 = np.matrix(annual_inc).transpose()
x2 = np.matrix(home_ownership).transpose()

x = np.column_stack([x1,x2])

X = sm.add_constant(x)
model = sm.OLS(y,X)
f = model.fit()

print 'Coefficients: ', f.params[0:2]
print 'Intercept: ', f.params[2]
print 'P-Values: ', f.pvalues
print 'R-Squared: ', f.rsquared

#models i
#y=B0+B1x1+E int_rate~annual_inc+E
#y=B0 +B1+B2x1+E
#y=B0 + B1 + B2d2 + Epsilon

#y=B0+B1x1+B2(x1*d2)+Epsilon (x1*d2) = interaction term adjusts slope
#y=int_rate
#x=annual_inc
#epsilon = noise
#d=dummy variable home_ownership
#interaction term = annual_inc*home_ownership ***note need to multiply these in model

#note
#syntax examples needed to continue with modeling