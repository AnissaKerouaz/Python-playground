import pandas as pd
df = pd.read_csv('data/shein-products.csv')

#the count of missing rows in each column
missing_values = df.isnull().sum()
print(missing_values)
#filling missing stock with 0
df['in_stock'] = df['in_stock'].fillna(0)
#dropping rows where price is missing
df =df.dropna(subset=['final_price'])

#sorting by desc rating and extracting top 5 high-rated items
df = df.sort_values(by='rating', ascending=False).head(5)


