import pandas as pd
import math
import matplotlib.pyplot as plt
import random

names = ['Bob','Jessica','Mary','John','Mel']

random.seed(500)
random_names = [names[random.randint(0, 4)] for i in range(1000)]
print(random_names[:20])
births = [random.randint(0, 1000) for i in range(1000)]
print(births[:10])
BabyDataSet = list(zip(random_names, births))
print(BabyDataSet[:10])
#df = pd.DataFrame(data=BabyDataSet, columns=['Names', 'Births'])
#print(df[:10])
#df.to_csv('Births1880.csv', index=False, header=False)

Location = r'/home/kashaeva/PycharmProjects/Births1880.csv'
df = pd.read_csv(Location, names=['Names','Births'])
#print(df.info())
#print(df.head())
#print(df.tail())

"""find all the unique records of the "Names" column."""
unique_names = df['Names'].unique()
print(unique_names)
print(df['Names'].describe())

"""we can create a groupby object"""
name = df.groupby('Names')
df = name.sum()
Sorted = df.sort_values('Births', ascending=False)
print(Sorted.head(1))
print(df['Births'].max())
df['Births'].plot.bar()
plt.show()