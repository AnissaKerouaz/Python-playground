import pandas as pd
df= pd.read_csv("data/shein-products.csv")
#print(df.info())
#print(df.memory_usage(deep=True))
#check this one u wrote: print((df.columns).sort_values(ascending=False).head(3).memory_usage(deep=True))

top_3 = df.memory_usage(deep=True)
top_3= top_3.sort_values(ascending=False)
print(top_3.head(3))




