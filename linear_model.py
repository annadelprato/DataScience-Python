#test2.py
#inear modelInterestRate = b + a1(FICOScore) + a2(LoanAmount)

import numpy as np
import pandas as pd
import statsmodels.api as sm

#loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')
loansData = pd.read_csv('loansData.csv')
#loansData = pd.read_csv('loansData.csv')

intrate = loansData['Interest.Rate']
loanamt = loansData['Loan.Amount']
fico = loansData['FICO.Score']

# The dependent variable
y = np.matrix(intrate).transpose()
# The independent variables shaped as columns
x1 = np.matrix(fico).transpose()
x2 = np.matrix(loanamt).transpose()

x = np.column_stack([x1,x2])

X = sm.add_constant(x)
model = sm.OLS(y,X)
f = model.fit()

print 'Coefficients: ', f.params[0:2]
print 'Intercept: ', f.params[2]
print 'P-Values: ', f.pvalues
print 'R-Squared: ', f.rsquared