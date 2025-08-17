import pandas as pd
df = pd.read_csv("data/shein-products.csv", encoding = 'iso-8859-1')

print(df.dtypes)
df = df.drop_duplicates()

#sorting values by asc or desc to pick the best then removing duplicates

df = df.sort_values(
    by=['product_name', 'rating', 'reviews_count', 'final_price'], 
    ascending =[True, False, False, False, True])

df =df.drop_duplicates(subset=['product_name'], keep='first') 

#filling missing values smartly:
#fill missing brand with corresponding category(only if brand is missing)
df['brand'] = df['brand'].fillna(df['category'])
df['categories'] = df['categories'].fillna("unknown")

#normalize text 
# lowercase and strip spaces in title and brand and remove special characters(use regex)
df['product_name'] = df['product_name'].str.lower()                 # lowercase
df['product_name'] = df['product_name'].str.strip()                 # remove leading/trailing spaces
df['product_name'] = df['product_name'].str.replace(r'[^a-z0-9 ]', '', regex=True)  # remove special chars

df['brand'] = df['brand'].str.lower()
df['brand'] = df['brand'].str.strip()
df['brand'] = df['brand'].str.replace(r'[^a-z0-9 ]', '', regex=True)

