#logistic regression 
import pandas as pd
import numpy
import statsmodels.api as sml

df=pd.read_csv('loansData.csv')

df['Interest.Rate'].apply(lambda x: 'True' if x <= 12 else 'False')

df['Interest.Level'] = df['Interest.Rate'].apply(lambda x: 'True' if x <= 12 else 'False')

df['Intercept']=1

#Column list 
#I would like to be able to call the columns in instead of listing them but so far, I can't figure it out- df.head???

ind_vars=('Amount.Requested', 'Loan.Amount', 'Interest.Rate', 'Loan.Length', 'Loan.Purpose',	
	'Debt.To.Income.Ratio',	'State', 'Home.Ownership', 'Monthly.Income', 'FICO.Score',	
	'Open.CREDIT.Lines', 'Revolving.CREDIT.Balance', 'Inquiries.in.the.Last.6.', 'Employment.Length', 
	'Intercept', 'Interest.Level')
list=[ind_vars]
for list_items in list:
	print repr(list_items)


#print df.head(50).to_string()
#print df[df['Interest.Rate'] == 10].head() # should all be True
#print df[df['Interest.Rate'] == 13].head() # should all be False


#script runs till here

#print df.head(50).to_string()
#print df[df['Interest.Rate'] == 10].head() # should all be True
#print df[df['Interest.Rate'] == 13].head() # should all be False



#Note
#Additional instruction/synatax example and clarification needed for modeling exercise. Also, data "IR_TF" not clear.
