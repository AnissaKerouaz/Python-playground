import numpy as np
import time
from datetime import datetime, timedelta
np.random.seed(42)

rows = 1000

user_ids= np.random.randint(1000, 1100, size= rows)

product_ids= np.random.randint(2000, 2100, size=rows)

ratings= np.random.uniform(1.0, 5.0, size=rows)


now = int(time.time())
one_year_ago = int((datetime.now() - timedelta(days=360)).timestamp())
timestamp = np.random.randint(one_year_ago, now, size=rows)

data = np.column_stack((user_ids, product_ids, ratings, timestamp))
print(data.shape)
print(data)

#basic statistics and aggregations
#1. the average of all the ratings given in the dataset 
avg_ratings= np.mean(data[:, 2])
print(avg_ratings)
#2. number of unique users and unique products
#column 0 is for users, column 1 is for products
unique_users =np.unique(data[:, 0]).size
unique_products = np.unique(data[:, 1]).size
positive_ratings= np.sum(data[:, 2] >4.5)
print(unique_users)
print(unique_products)
print(positive_ratings)


