import pandas as pd
import numpy as np

df = pd.read_csv('SalesPortalOrderLog.csv')


def add_columns(df, column_name_1, column_name_2,decider_column):
	df[column_name_1] = np.where(df[decider_column] == 'Order', 1, 0)
	df[column_name_2] = np.where(df[decider_column] == 'Estimate', 1, 0)
	return df

df = add_columns(df,'Total Orders', 'Total Estimates', 'Type')
# print(df.head())


for i in df['Int/Ext'].unique():
	print(i)
	print(df['Name'].unique())
	print(df[df['Int/Ext'] ==i]['Total Orders'].count())


