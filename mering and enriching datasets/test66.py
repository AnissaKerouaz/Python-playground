import pandas as pd
df_customer = pd.read_csv('data/customers_large.csv')
df_order = pd.read_csv('data/orders_large.csv')

#performing a left join using mergE() to add customer info(name, email) to each order
#missing values are handled gracefully thanks to how='left':It keeps all orders from the orders table, even if there?s no matching customer in the customers table.
merge = df_order.merge(df_customer, on="customer_id" , how='left')

#setting the indexes for the join operation
df_reviews = pd.read_csv('data/reviews_large.csv', index_col='product_id')
merge = merge.set_index('product_id')

join = merge.join(df_reviews, how='left')

#Reset index so product_id becomes a column again
join = join.reset_index()

join = join[["order_id", "customer_id", "name", "product_id", "rating", "review"]]
print("\nFinal orders with reviews:")
print(join.head(3))

missing_customers= join[join['name'].isna()]
missing_reviews= join[join['rating'].isna()]
print("missing values")
print(len(missing_customers))
print(len(missing_reviews))





