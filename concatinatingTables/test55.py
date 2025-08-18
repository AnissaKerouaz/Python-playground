#concatinating tables used when appending logs, creating feature unions, or combining distributed data
import pandas as pd
import os
df_shein = pd.read_csv("data/shein-products.csv")
df_walmart = pd.read_csv('data/walmart-products.csv')

df_shein['source'] = 'shein'
df_walmart['source'] = 'walmart'

all_columns = list(df_shein.columns)  
for col in df_walmart.columns:
    if col not in all_columns:
        all_columns.append(col)


for col in all_columns:
    if col not in df_shein.columns:
        df_shein[col] = pd.NA#if column is not in shein df we create it and fill it with NA

for col in all_columns:
    if col not in df_walmart.columns:
        df_walmart[col] = pd.NA

#Reorder columns in both datasets to be exactly the same
#If df_shein already has all the columns listed in all_columns, it works perfectly and just reorders them.
#If df_shein is missing any column in all_columns, pandas will raise a KeyError because it can?t find that column.
df_shein = df_shein[all_columns]
df_walmart = df_walmart[all_columns]

df_all = pd.concat([df_shein, df_walmart], ignore_index=True)

if 'brand' in df_all.columns:
    df_all['brand'] = df_all['brand'].str.lower().str.strip()
if 'seller' in df_all.columns:
    df_all['seller'] = df_all['seller'].str.lower().str.strip()

df_all = df_all.drop_duplicates(subset=['product_id', 'source'])

#analysis
#We chose the source column here because it tells us which dataset each row came from.
print("Number of products per platform:")
print(df_all['source'].value_counts())

#picking the most frequent in the dataset
if 'brand' in df_all.columns:
    print("\nTop 5 brands with most products:")
    print(df_all['brand'].value_counts().head(5))

#number of listings with missing price or rating
for col in ['final_price', 'rating']:
    if col in df_all.columns:
        print(f"\nMissing values in {col}: {df_all[col].isna().sum()}")
                                          #this is where the count for how many missing values is done

os.makedirs(r'D:\dataopsclasspractice\concatinatingTables\merge', exist_ok=True)
df_all.to_parquet(r'D:\dataopsclasspractice\concatinatingTables\merge\shein-products-cleaned.parquet', index=False)
