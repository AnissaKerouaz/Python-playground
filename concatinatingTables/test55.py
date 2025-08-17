#used when appending logs, creating feature unions, or combining distributed dat
import pandas as pd
import os
df_shein = pd.read_csv("data/shein-products.csv")
df_walmart = pd.read_csv('data/walmart-products.csv')

df_shein['source'] = 'shein'
df_walmart['source'] = 'walmart'

all_columns = list(df_shein.columns)  # start with Shein columns
for col in df_walmart.columns:
    if col not in all_columns:
        all_columns.append(col)

for col in all_columns:
    if col not in df_shein.columns:
        df_shein[col] = pd.NA

for col in all_columns:
    if col not in df_walmart.columns:
        df_walmart[col] = pd.NA
#Reorder columns in both datasets to be exactly the same
df_shein = df_shein[all_columns]
df_walmart = df_walmart[all_columns]

df_all = pd.concat([df_shein, df_walmart], ignore_index=True)

if 'brand' in df_all.columns:
    df_all['brand'] = df_all['brand'].str.lower().str.strip()
if 'seller' in df_all.columns:
    df_all['seller'] = df_all['seller'].str.lower().str.strip()

df_all = df_all.drop_duplicates(subset=['product_id', 'source'])

print("Number of products per platform:")
print(df_all['source'].value_counts())

#make sure its actually taking the top 5 not just the first 5
if 'brand' in df_all.columns:
    print("\nTop 5 brands with most products:")
    print(df_all['brand'].value_counts().head(5))

for col in ['final_price', 'rating', 'rating_stars']:
    if col in df_all.columns:
        print(f"\nMissing values in {col}: {df_all[col].isna().sum()}")

os.makedirs(r'D:\dataopsclasspractice\concatinatingTables\merge', exist_ok=True)
df_all.to_parquet(r'D:\dataopsclasspractice\concatinatingTables\merge\shein-products-cleaned.parquet', index=False)
