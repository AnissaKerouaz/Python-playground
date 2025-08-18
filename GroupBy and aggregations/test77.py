import pandas as pd
df_customer = pd.read_csv('data/customers_large.csv')
df_order = pd.read_csv('data/orders_large.csv')
df_reviews = pd.read_csv('data/reviews_large.csv')
#number of orders per customer
print(df_order.groupby("customer_id").size().reset_index(name="order_id"))

#avergae rating per product
print(df_reviews.groupby("product_id")["rating"].mean().reset_index(name="rating"))

#first we do the join of orders and reviews df so that we have the data we need
join = df_order.merge(df_reviews, how='left', on="product_id")
print(join)

#we want tesults per customer! soo
print(join.groupby("customer_id").size().reset_index(name="reviews"))

'''reviews_per_customer= join.groupby("customer_id").size().reset_index(name="review")
print("\n reviews per customer")
print(reviews_per_customer)

average_rating_per_customer= join.groupby("customer_id")["rating"].mean().reset_index(name="rating")
print("\n average rating per customer")
print(average_rating_per_customer)'''

table = join.groupby("customer_id").agg(
    reviews_per_customer= ("rating", "count"),
    average_rating_per_customer= ("rating", "mean")

).reset_index()

print("table we want")
print(table)

top_5_customers = df_order.groupby("customer_id").size().reset_index(name="order_id").sort_values(by="order_id", ascending=False).head(5)
top_5_customer_info= top_5_customers.merge(df_customer, on="customer_id", how='left')

print(top_5_customer_info)