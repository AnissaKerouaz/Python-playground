import pandas as pd
df = pd.read_csv('data/shein-products.csv')

balloons_we_want = df[
			(df['category']=='Decorative Balloons')
			&
			(df['final_price'] < 800)
			&
			(df['final_price'] > 1)
			] 

print(balloons_we_want.shape[0])


balloons_dettails_we_want = balloons_we_want[["product_name", "final_price", "category", "in_stock"]]

sorted_balloons = balloons_dettails_we_want.sort_values(by="product_name", ascending = False)

balloons = sorted_balloons.head(10)
print(balloons)

'''smartphones_we_want= df[
    (df['cateogry'] == 'Smartphones')
    &
    (df['rating'] > 4.5)
    &
    (df['final_price']< 1000)
]

df = df.set_index('product_id')
row = df.loc[12345]
print(row)'''