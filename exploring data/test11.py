import pandas as pd
import os

df = pd.read_csv("data/shein-products.csv", encoding = 'iso-8859-1')
print(df.columns)
print(df.shape[0])
print(df.shape[1])
print(df.info(memory_usage='deep'))

clean_columns=[]

for column in df.columns:
	column=column.strip()
	column=column.lower()
	column=column.replace(' ','_')
	clean_columns.append(column)

#dropping rows with null product names or prices
df = df.dropna(subset=['product_name', 'final_price'])

df['final_price'] = df['final_price'].astype(float)

os.makedirs(r'D:\dataopsclasspractice\exploring data\storing', exist_ok=True)
df.to_parquet(r'D:\dataopsclasspractice\exploring data\storing\shein-products-cleaned.parquet', index=False)
