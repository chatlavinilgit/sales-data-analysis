import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv('Sample - Superstore.csv')

# Convert date column (IMPORTANT)
df['Order Date'] = pd.to_datetime(df['Order Date'])

print("="*60)
print("DATA ANALYSIS REPORT - SUPERSTORE DATA")
print("="*60)

# 1. Dataset Overview
print("\n1. DATASET OVERVIEW")
print("-" * 60)
print(f"Total Records: {len(df)}")
print(f"Total Columns: {len(df.columns)}")
print("\nFirst 5 rows:")
print(df.head())

# 2. Data Quality
print("\n2. DATA QUALITY")
print("-" * 60)
print("Missing Values:\n", df.isnull().sum())
print("\nData Types:\n", df.dtypes)

# 3. Summary Statistics
print("\n3. SUMMARY STATISTICS")
print("-" * 60)
total_sales = df['Sales'].sum()
total_profit = df['Profit'].sum()

print(f"Total Sales: ${total_sales:,.2f}")
print(f"Total Profit: ${total_profit:,.2f}")
print(f"Average Profit Margin: {(total_profit / total_sales * 100):.2f}%")
print(f"Total Quantity Sold: {df['Quantity'].sum()}")
print(f"Average Discount: {df['Discount'].mean():.2%}")

# 4. Sales by Category
print("\n4. SALES BY CATEGORY")
print("-" * 60)
category_sales = df.groupby('Category')[['Sales', 'Profit']].sum().round(2)
print(category_sales)

# 5. Sales by Region
print("\n5. SALES BY REGION")
print("-" * 60)
region_sales = df.groupby('Region')[['Sales', 'Profit']].sum().round(2)
print(region_sales)

# 6. Sales by Segment
print("\n6. SALES BY SEGMENT")
print("-" * 60)
segment_sales = df.groupby('Segment')[['Sales', 'Profit']].sum().round(2)
print(segment_sales)

# 7. Top Customers
print("\n7. TOP 5 CUSTOMERS")
print("-" * 60)
top_customers = df.groupby('Customer Name')[['Sales', 'Profit']] \
    .sum().sort_values('Sales', ascending=False).head(5)
print(top_customers)

# 8. Monthly Sales (NEW 🔥)
df['Month'] = df['Order Date'].dt.month
monthly_sales = df.groupby('Month')['Sales'].sum()

# ------------------ VISUALIZATION ------------------ #

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('Superstore Data Analysis Dashboard', fontsize=16, fontweight='bold')

# Sales by Category
category_data = df.groupby('Category')['Sales'].sum()
axes[0, 0].bar(category_data.index, category_data.values)
axes[0, 0].set_title('Sales by Category')

# Profit by Region
region_profit = df.groupby('Region')['Profit'].sum()
axes[0, 1].bar(region_profit.index, region_profit.values)
axes[0, 1].set_title('Profit by Region')

# Segment Distribution
segment_orders = df.groupby('Segment')['Order ID'].count()
axes[1, 0].pie(segment_orders.values, labels=segment_orders.index, autopct='%1.1f%%')
axes[1, 0].set_title('Orders by Segment')

# Monthly Trend (REPLACED SCATTER 🔥)
axes[1, 1].plot(monthly_sales.index, monthly_sales.values, marker='o')
axes[1, 1].set_title('Monthly Sales Trend')
axes[1, 1].set_xlabel('Month')
axes[1, 1].set_ylabel('Sales')

plt.tight_layout()
plt.savefig('analysis_dashboard.png', dpi=300)

print("\nDashboard saved as 'analysis_dashboard.png'")
print("\nAnalysis complete!")