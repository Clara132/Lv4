import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
import seaborn as sns

# ucitavanje ociscenih podataka
df = pd.read_csv('cars_processed.csv')
print(df.info())

print('Broj mjerenja:', len(df))

print('\nTip pojedinog stupca:\n', df.dtypes)

print('Automobil s najvećom cijenom:', df.sort_values(by=['selling_price']).head(1))

print('Automobil s najmanjom cijenom:\n', df.sort_values(by=['selling_price']).tail(1))

print('2012. godine je proizvedeno', df[df['year']==2012]['year'].count(),'automobila.\n')

print('Najviše kilometara je prešao:', df.sort_values(by=['km_driven']).head(1))
print('Najmanje kilometara je prešao:\n', df.sort_values(by=['km_driven']).tail(1))

print('Automobili najčešće imaju', round(df.seats.mean()), 'sjedala.\n')

print('Prosječna prijeđena kilometraža za automobile s dizel motorom je:', df[df['fuel']=='Diesel']['km_driven'].mean())
print('Prosječna prijeđena kilometraža za automobile s benzinskim motorom je:', )

# razliciti prikazi
sns.pairplot(df, hue='fuel')

sns.relplot(data=df, x='km_driven', y='selling_price', hue='fuel')
df = df.drop(['name','mileage'], axis=1)

obj_cols = df.select_dtypes(object).columns.values.tolist()
num_cols = df.select_dtypes(np.number).columns.values.tolist()

fig = plt.figure(figsize=[15,8])
for col in range(len(obj_cols)):
    plt.subplot(2,2,col+1)
    sns.countplot(x=obj_cols[col], data=df)

df.boxplot(by ='fuel', column =['selling_price'], grid = False)

df.hist(['selling_price'], grid = False)

#tabcorr = df.corr()
#sns.heatmap(df.corr(), annot=True, linewidths=2, cmap= 'coolwarm') 

#plt.show()
