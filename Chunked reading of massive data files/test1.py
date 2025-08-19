import pandas as pd
sales=0
new=[]
for chunk in pd.read_csv("data/orders_large.csv", chunksize= 500):
    chunk['total'] = chunk['quantity'] *chunk['price']
    sales += chunk['total'].sum()

    desired_country = chunk[chunk['country'] == 'France']
    new.append(desired_country)

pd.concat()
for chunk in pd.read_csv('df_huge', chunksize=500):
    



