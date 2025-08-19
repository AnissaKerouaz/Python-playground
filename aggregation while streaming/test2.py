import pandas as pd
import numpy as np

# Set seed for reproducibility
np.random.seed(42)

# Number of rows (adjust as needed for machine capability)
num_rows = 5_000  # 5 million rows

# Generate synthetic data
df_huge = pd.DataFrame({
    'order_id': np.arange(1, num_rows + 1),  # int64
    'customer_id': np.random.randint(1, 100_000, size=num_rows),  # int64
    'order_date': pd.to_datetime('2023-01-01') + pd.to_timedelta(np.random.randint(0, 365, size=num_rows), unit='D'),  # datetime
    'quantity': np.random.randint(1, 100, size=num_rows),  # int64
    'price': np.random.uniform(1, 500, size=num_rows),  # float64
    'product_category': np.random.choice(['Books', 'Electronics', 'Clothing', 'Toys', 'Groceries'], size=num_rows),  # object
    'country': np.random.choice(['USA', 'UK', 'Canada', 'France', 'Germany'], size=num_rows),  # object
    'payment_method': np.random.choice(['Credit Card', 'PayPal', 'Bank Transfer'], size=num_rows),  # object
    'is_returned': np.random.choice([True, False], size=num_rows),  # bool
    'reordered': np.random.choice([True, False], size=num_rows),  # bool
})

# Introduce poor optimization on purpose
df_huge['is_returned'] = df_huge['is_returned'].astype(object)
df_huge['reordered'] = df_huge['reordered'].astype(object)

# Save (optional)
# df_huge.to_csv("huge_orders.csv", index=False)

# Show memory usage
print(df_huge.info(memory_usage="deep"))
df_huge.to_parquet("huge_orders.parquet", index=False)

import pandas as pd
import numpy as np

# Parameters
chunk_size = 500_000
file_path = "huge_orders.parquet"

# Accumulators
category_sales = {}
country_sales = {}
country_counts = {}

# Read in chunks
for chunk in pd.read_parquet(file_path, engine='pyarrow', columns=None, chunksize=chunk_size):
    # Compute total for each row
    chunk['total'] = chunk['quantity'] * chunk['price']

    # Group by product_category and sum total sales
    cat_group = chunk.groupby('product_category')['total'].sum()
    for cat, total in cat_group.items():
        category_sales[cat] = category_sales.get(cat, 0) + total

    # Group by country: sum total sales and count sales
    country_group = chunk.groupby('country')['total'].agg(['sum', 'count'])
    for country, row in country_group.iterrows():
        country_sales[country] = country_sales.get(country, 0) + row['sum']
        country_counts[country] = country_counts.get(country, 0) + row['count']

# Print final total sales per product category
print("Total sales per product category:")
for cat, total in category_sales.items():
    print(f"{cat}: {total:.2f}")

# Compute and print average sale per country
print("\nAverage sale per country:")
for country in country_sales:
    avg = country_sales[country] / country_counts[country]
    print(f"{country}: {avg:.2f}")