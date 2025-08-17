import pandas as pd
df = pd.read_csv('data/shein-products.csv')


missing = df.isnull().sum()
print(missing)

print(df.dtypes)
df = df.drop_duplicates()

#sorting values by asc or desc to pick the best then removing duplicates
df_sorted = df.sort_values(
    by=['product_id', 'rating', 'review_count', 'price'],
    ascending=[True, False, False, True]
)

df_unique = df_sorted.drop_duplicates(subset=['product_id'], keep='first')


