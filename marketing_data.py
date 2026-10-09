import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns
from scipy import stats

df = pd.read_csv(r"C:\Users\DELL\Downloads\marketing_data.csv")
print(df.head)
print(df.columns)
'''Index(['ID', 'Year_Birth', 'Education', 'Marital_Status', ' Income ',
       'Kidhome', 'Teenhome', 'Dt_Customer', 'Recency', 'MntWines',
       'MntFruits', 'MntMeatProducts', 'MntFishProducts', 'MntSweetProducts',
       'MntGoldProds', 'NumDealsPurchases', 'NumWebPurchases',
       'NumCatalogPurchases', 'NumStorePurchases', 'NumWebVisitsMonth',
       'AcceptedCmp3', 'AcceptedCmp4', 'AcceptedCmp5', 'AcceptedCmp1',
       'AcceptedCmp2', 'Response', 'Complain', 'Country'],
      dtype='str')'''
''' Coustomer Info columns =['Year_Birth', 'Education', 'Marital_Status', ' Income ',
       'Kidhome', 'Teenhome',]
       products columns = [MntWines',
       'MntFruits', 'MntMeatProducts', 'MntFishProducts', 'MntSweetProducts',
       'MntGoldProds]
       number of purchases from store and platforms = [NumDealsPurchases', 'NumWebPurchases',
       'NumCatalogPurchases', 'NumStorePurchases', 'NumWebVisitsMonth',]'''

print( "After importing the data, examine variables such as Dt_Customer and Income to verify their accurate importation.")
dff = df['Dt_Customer']
''' so Dt_Customer is string data type data is date format we can convert it to to_datetime'''
df['Dt_Customer'] = pd.to_datetime(df['Dt_Customer'])
print(df['Dt_Customer'].dtype)
dff = df[' Income ']
print(dff.dtype)
'''Income is having string type at the same time having spacing issue in column name'''
'''By using stip function we can remove spacesing from and back'''
df.columns = df.columns.str.strip()
#print(dff.dtype)
#print(dff)
'''in output i can see '$' and ',' with number to convert it to float need to remove them by using replace'''
df['Income'] = df['Income'].str.replace(r'[\$\,]','',regex=True)
print(f' after replacing dollar and comma : {df['Income']}\n')
print('2. There are missing income values for some customers. Conduct missing value imputation,' \
'\nconsidering that customers with similar education and marital status tend to have comparable yearly ' \
'\n incomes, on average. It may be necessary to cleanse the data before proceeding. Specifically, ' \
'\nscrutinize the categories of education and marital status for data cleaning.')
dff = df['Income'].isnull().sum()
print(dff)
'''we have 24 null values in Income column after made it float function'''
''' we have to add null values based on there marital and education so we need to now how data is with marital and education '''
dff = df['Education'].value_counts()
print(f' education count of each value : {dff}')
'''Education
Graduation    1127
PhD            486
Master         370
2n Cycle       203
Basic           54 dtype of int64'''
dff = df['Marital_Status'].value_counts()
print(f' Mariage status count of each value : {dff} \n')
'''i can find that Married,Together,Single,Divorced,Widow,Alone,YOLO,Absurd so many values lied in mritical_status so 
i can combine single with [Alone + YOLO + Absurd ] because all meaning same as single i googled it '''
df['Marital_Status'] = df['Marital_Status'].replace({'Alone':'Single','YOLO':'Single','Absurd' : 'Single'})
print( f' after combining some similar columns : {df['Marital_Status'].value_counts()} \n')
'''now maritical_column is perfect for null values'''
df['Income'] = df['Income'].astype(float)
dff = pd.DataFrame(df.groupby(['Education','Marital_Status'])['Income'].transform('mean'))
#print(f' made group of column which have value of mean after combining of education with marital status : {dff}\n')
'''got an error that one dtype 'str' does not support operation 'mean' lets check dtype of it '''
#dff = df.info()
#print(dff)
#df.info()
df['Income'] = df['Income'].fillna(df.groupby(['Education','Marital_Status'])['Income'].transform('mean'))
dff = df['Income'].isnull().sum()
#print(df.iloc[134])
#print(dff)
print(df[df['Income'] == 'dff'])
print('i can find the 0 null values in income column \n \n')


print ('Create variables to represent the total number of children, age, and total spending.')
'''i need to create a age and total spending
in my data i have 'Kidhome', 'Teenhome' combine it i can get age'''
df['age'] = df['Kidhome'] + df['Teenhome']
#print(df['age'])
#print(df.head())
''' i have done a mistake that kept children name as age so using rename changed it'''
df = df.rename(columns={'age':'children'})
dff = df.columns
#print(dff)

'''i need to find the age for for coustomer so i have birth year so and Date of customer so  minusing both can i get my data'''
dff = df.dtypes
#print(dff)
''' so Year_Birth is int64 and Dt_Customer is datetime format so from datetime i can convert it to year  '''
df['age'] = df['Dt_Customer'].dt.year.max() - df['Year_Birth']
df['age'] = df['age'].astype(int)
print(f' created Age column : {df['age'].head()}\n')
#print(df.columns)

''' to find the total spending '''
dff = ['MntWines','MntFruits', 'MntMeatProducts', 'MntFishProducts', 'MntSweetProducts','MntGoldProds']
df['total_spending'] = df[dff].sum(axis=1)
print(f' created total spending column : {df['total_spending'].head()}')

'''as per number of transactions across the three channels
 NumDealsPurchases', 'NumWebPurchases',
       'NumCatalogPurchases' '''
dff = ['NumStorePurchases', 'NumWebPurchases',
       'NumCatalogPurchases']
df['Total_purchases'] = df[dff].sum(axis=1)
#print(df['Tol_numofpurchese_3channel'])
#print(df.iloc[134])
#print(df.dtypes)
#df['Income'] = df['Income'].str.replace('dff', '',regex=False)
#df['Income'] = df['Income'].fillna('dff')
#dff = df['Income'].isnull.sum()
#print(dff)
#print(df.dtypes)
#rint(df.iloc[134])
print(f' created total purchases column : {df['Total_purchases']}\n')


print("Generate box plots and histograms to gain insights into the'\ ' \n distributions and identify outliers. Implement outlier treatment as needed ")
'''fig represents total fig size and axes gives a where the each plot should be there fig and axes names can be changed '''
fig, axes = plt.subplots(2,2, figsize=(10,10))
sns.histplot(df['age'], kde=True, ax=axes[0,0])
axes[0,0].set_title('Age distribution')
sns.boxplot(df['age'], ax=axes[0,1])   
axes[0,1].set_title('Age outlayers')
sns.histplot(df['Income'], kde=True, ax=axes[1,0], color='black')
axes[1,0].set_title('Income distribution')
sns.boxplot(df['Income'], ax=axes[1,1] )     
axes[1,1].set_title('Income outlayers')
#plt.show()
'''i can find age outlayers are at 120 of age and income at 6L'''
df_clean1 = df[(df['age']< 100)].copy()
df_clean2 = df[(df['Income'] < 200000)].copy()
print(df_clean1.head(10))
fig , axes = plt.subplots(2,2, figsize=(10,15))
sns.histplot(df_clean1['age'], kde=True, ax= axes[0,0], color='violet')
axes[0,0].set_title('age distribution')
sns.boxplot(df_clean1['age'], ax=axes[0,1], color='Red')
axes[0,1].set_title('age outlayers')
sns.histplot(df_clean2['Income'], kde=True, ax=axes[1,0])
axes[1,0].set_title('Income distribution')
sns.boxplot(df_clean2['Income'], ax=axes[1,1])
axes[1,1].set_title('Income outlayers')
#plt.show()
''' after df_clean2 i can also find outlayers at 160000 so need calculate the IQR value IQR = q1 - q3 and 
q1 = 25% of data and q3 = 75% of data '''
q1 = df['Income'].quantile(0.25)
q3 = df['Income'].quantile(0.75)
iqr = q1 - q3
print(f" 25% data or Q1 :{q1}\n 75% of data or Q3 : {q3}\n IQR value  = {iqr}") # IQR =  -32751.0
lower_limit = q1 - 1.5 * iqr
print(f"lower limit : {lower_limit} \n") # lower limit 84665.25
upper_limit = q1 + 1.5 * iqr 
print(f" upper limit : {upper_limit} \n") # upper limit -13587.75
outlayers = df[(df['Income'] < lower_limit) | (df['Income'] > upper_limit )]
#print(outlayers) # data after 94871.0 this value is treated as outlayers by graph i can see that outlayer lies on 160000 so as import of data not modifying it and making copy of it and creating graph 
upper_limit_value = outlayers['Income'].iloc[-1]
#print(upper_limit_value)
df_clean = df.copy()
df_clean['Income'] = df_clean['Income'].clip( upper= upper_limit_value)

print(f' clipped upper limit value : { df_clean['Income'].iloc[-1]} \n last value is 94871.0 as checked')

fig , axes = plt.subplots(1,2, figsize=(10,10))
sns.histplot(df_clean['Income'],kde=True, color='Green', ax=axes[0])
axes[0].set_title('Income distribution')
sns.boxplot(df_clean['Income'], color='green', ax=axes[1])
axes[1].set_title('Income outlayers')

#plt.show()


print("Apply ordinal and one-hot encoding based on the various types of categorical variables.")
#dff = df_clean.select_dtypes(include= 'category',).columns
#print(f' i have category column : {dff.dtype}')
print(df_clean.select_dtypes(include=['category','string','object'])) 
print("Education , Marital_Status & Country are comes under categorical column as per data ")
''' IN ordinal education can be consider more degree will have high value using label encoding for this'''
print(df_clean['Education'].value_counts())
'''Graduation    1127
PhD            486
Master         370
2n Cycle       203
Basic           54'''
label = {'Basic':0,'2n Cycle':1,'Graduation':2, 'Master':3, 'PhD':4 }
df_clean['Education_label'] = df_clean['Education'].map(label)
print(f" After doing label encoding of education column because weightage given by degree {df_clean['Education_label']}\n")
print(df_clean['Marital_Status'].value_counts())
'''Marital_Status
Married     864
Together    580
Single      487
Divorced    232
Widow        77'''
#marriage_data = {'Married','Together','Single','Divorced','Widow'}
df_clean = pd.get_dummies(df_clean,columns=['Marital_Status','Country'], drop_first=True)
print(df_clean.head(20))
print(df_clean.columns)
print(df_clean.shape)
#print(df['Response'].head(20))

'''Identify the top-performing products and those with the lowest revenue'''
data = ['MntWines','MntFruits', 'MntMeatProducts', 'MntFishProducts', 'MntSweetProducts','MntGoldProds']
product_revenue = df_clean[data].sum()
plt.figure(figsize=(10,15))
sns.barplot( x=product_revenue.index, y=product_revenue.values, width=0.9,  palette=['orange', 'blue', 'red', 'green', 'brown', 'navy'])
'''Examine if there is a correlation between customers' age and the acceptance rate of the last campaign.'''
''' pd.qcut will helps to divide total values in equalvalent groups by q=4 give 4 equal values and taken response column to see the correlation'''
df_clean['age_group'] = pd.qcut(df['age'],q=4, duplicates='drop',labels=['young','elder','midde-age','older'])
age_response = df_clean.groupby('age_group')['Response'].mean()*100
age_response.plot(kind='line', marker='o', color='black',xlabel='Age',ylabel='Response_rate',title='correlation of acceptance rate of the last campaign')
#plt.show()
'''Determine the country with the highest number of customers who accepted the last campaign.'''
#print(df.columns)
country = df[df['Response'] == 1]['Country'].value_counts()
plt.figure(figsize=(10,15))
country.plot(kind='bar',title='country with the highest number of customers who accepted the last campaign')
#plt.show()
'''Investigate if there is a discernible pattern in the number of children at home and the total expenditure.'''
plt.figure(figsize=(10,10))
sns.boxplot(x='children',y='Total_purchases',data=df_clean).set_title("total children and there total expenditure")

'''Analyze the educational background of customers who lodged complaints in the last two years.'''
Cus_complain = df_clean.groupby('Education')['Complain'].value_counts()
plt.figure(figsize=(12,12))
Cus_complain.plot(kind='pie', title='complaints based on there Qualification',y='')
#plt.show()

#print(df['Country'].value_counts())
#plt.title("Products Performence based on Revenue")
#plt.xlabel("Products")
#plt.ylabel("Revenue")
#plt.show()

print("Older individuals may not possess the same level of technological proficiency \n and may, therefore, lean toward traditional in-store shopping preferences.")
older_age = df_clean[df_clean['age_group'] == 'older']['age']
corr , pvalue = stats.pearsonr(df_clean['age'], df_clean['NumStorePurchases'])
#print(corr)#0.1282720555938009

 #1.1099607633898813e-09
print (f'as p value {print(pvalue)} lesser than o.5 we have can accept the hypothysis that more age people lean towarrds to in-store shopping ')

print ("Customers with children likely experience time constraints, making online shopping a more convenient option \n ")
df_clean['new_children'] = (df_clean['children'] > 0).astype(int)
df_clean['wed_shop'] = df_clean['NumWebPurchases'] / df_clean['Total_purchases'].replace(0,1)
corr1 , pvalue1 = stats.pearsonr(df_clean['new_children'],df_clean['wed_shop'])
print(f'correlation : {corr1}\n') #0.2984864819714961
print(f'P value :{pvalue1}\n') #2.5170820610762264e-47
print(f"we have evidence that p value is less then 0.05 so we conclude that Customers with children \nlikely experience time constraints, making online shopping a more convenient option\n")


print("Sales at physical stores may face the risk of cannibalization by alternative distribution channels.\n")
df_clean['online_purchases'] = df_clean['NumWebPurchases'] + df_clean['NumCatalogPurchases']
corr2 , pvalue2 = stats.pearsonr(df_clean['NumStorePurchases'],df_clean['online_purchases'])
print(f'correlation value : {corr2}') #0.6153592978630218
print(f' P value : {pvalue2}') #1.4705856043016368e-233
print("we have evidence that p value is less then 0.05 so we conclude that Sales at physical stores may '\
' \n face the risk of cannibalization by alternative distribution channels but correlation is 0.615 so there'\
' \n tentative or positive towards that online purchases coustomers will have going to store as well \n ")

print("Does the United States significantly outperform the rest of the world in total purchase volumes? \n")
#print(df_clean.columns)
#print(df.columns)
us_purchases = df[df['Country'] == 'US']['Total_purchases']
not_us = df[df['Country']!= 'US']['Total_purchases']
corr3, pvalue3 = stats.ttest_ind(us_purchases,not_us)
print(f"correlation value : {corr3} \n")#0.030662287601973773

print(f" T test Value :{pvalue3}") #0.14685355981832582

print("There is insufficient statistical evidence to conclude that the United States significantly outperforms the rest of the world in total purchase volumes.")
plt.show()
#1.4512386847675383
#0.14685355981832415
