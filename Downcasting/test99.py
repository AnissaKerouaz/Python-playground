import pandas as pd
import numpy as np

df = pd.DataFrame({
    'order_id': np.arange(1, 1000001),
    'price': np.random.uniform(1, 500, 1000000)
})
#print(df)

#print(df.memory_usage(deep=True).sum())


# generate a df
new = pd.DataFrame({
    #lowest, highest, how much 
    'customer_id': np.random.randint(1, 1_000_000, 1_000_000),
    'age': np.random.randint(18, 90, 1_000_000),
    'price': np.random.uniform(1, 500, 1_000_000),
    'city': np.random.choice(['Paris', 'London', 'Berlin', 'Madrid'], 1_000_000),
    'is_active': np.random.choice([True, False], 1_000_000)
})

# Make it inefficient on purpose
#new['is_active'] = new['is_active'].astype(object)

print(new.memory_usage(deep=True).sum()/ 1024**2)

'''new["customer_id"] = new["customer_id"].astype("int32")
new["age"] = new["age"].astype("int8")
new["price"] = new["price"].astype("float32")
new['city']=new['city'].astype('category')'''


def downcast_df(df):
    for c in df.columns:
        if df[c].dtype == 'int64':
            df[c]= pd.to_numeric(df[c], downcast='integer')

        elif df[c].dtype == 'float64':
            df[c] = pd.to_numeric(df[c], downcast ='float')
        
        elif df[c].dtype == 'object':
            if df[c].nunique() / len(df)<0.5:
                df[c]=df[c].astype('category')

    memory = df.memory_usage(deep=True).sum()
    print(memory)
    return df


f=downcast_df(new)
print(f)

