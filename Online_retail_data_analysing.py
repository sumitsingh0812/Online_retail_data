import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# File path for the dataset
filepath = r"C:\Users\Admin\Documents\Power BI Dataset.csv"

# Load the dataset
df = pd.read_csv(filepath)

# Handling missing data by dropping rows with NaN values
df1 = df.dropna()
print("Data after dropping NaN values:")
print(df1)

# Display the first five rows of the dataset
df2 = df.head()
print("\nFirst five rows of the dataset:")
print(df2)

# Display the last two rows of the dataset
df3 = df.tail()
print("\nLast two rows of the dataset:")
print(df3)

# Sorting data by 'Profit' in descending order
df4 = df.sort_values('Profit', ascending=False)
print("\nData sorted by 'Profit' in descending order:")
print(df4)

# Sorting data by 'Sales' in descending order
df5 = df.sort_values('Sales', ascending=False)
print("\nData sorted by 'Sales' in descending order:")
print(df5)

# Counting missing values in each column
df6 = df.isnull()
df7 = df.isnull().sum()
print("\nMissing values in each column:")
print(df7)

# Calculating the total profit
df8 = df['Profit'].sum()
print("\nTotal profit:", df8)

# Calculating the total sales for a specific country (Austria in this case)
sales_data = df[df['Country'] == 'Austria']
total_us_sales = sales_data['Profit'].sum()
print("\nTotal profit in Austria:", total_us_sales)

# Calculating the total sales for a specific region (North)
region_data = df[df['Region'] == 'North']
region_sales = region_data['Sales'].sum()
print("\nTotal sales in the North region:", region_sales)

# Total sales revenue
total_sales = df['Sales'].sum()
print("\nTotal sales revenue:", total_sales)

# Finding the region with the highest sales
highest_sales_region = df['Region'].max()
print("\nRegion with the highest sales:", highest_sales_region)

# Top 10 best-selling products
product_sales = df.groupby('Product Name')['Sales'].sum()
top_10_selling_products = product_sales.sort_values(ascending=False).head(10)
print("\nTop 10 best-selling products:")
print(top_10_selling_products)



# Top customer segments contributing to total sales
customer_sales = df.groupby('Customer Name')['Sales'].sum()
top_customers = customer_sales.sort_values(ascending=False).head(3)
print("\nTop 3 customers contributing to total sales:")
print(top_customers)

# Categories and sub-categories with highest sales
sub_category_sales = df.groupby('Sub-Category')['Sales'].sum().sort_values(ascending=False)
category_sales = df.groupby('Category')['Sales'].sum().sort_values(ascending=False)
print("\nSales by Sub-Category:")
print(sub_category_sales)
print("\nSales by Category:")
print(category_sales)

# Total profit
total_profit = df['Profit'].sum()
print("\nTotal profit:", total_profit)

# Region with the most profit
profit_by_region = df.groupby('Region')['Profit'].sum().sort_values(ascending=False)
print("\nProfit by Region:")
print(profit_by_region)

# Top 3 products generating highest profit
top_profit_products = df.groupby('Product Name')['Profit'].max().sort_values(ascending=False).head(3)
print("\nTop 3 products generating highest profit:")
print(top_profit_products)

# Profit margin by sub-category
profit_margin = df.groupby('Sub-Category')['Profit'].sum()
print("\nProfit by Sub-Category:")
print(profit_margin)

# Profit by shipping mode
profit_by_ship_mode = df.groupby('Ship Mode')['Profit'].sum()
print("\nProfit by Shipping Mode:")
print(profit_by_ship_mode)

# Top 10 customers based on sales
top_customers_sales = df.groupby('Customer Name')['Sales'].sum().sort_values(ascending=False).head(10)
print("\nTop 10 customers based on sales:")
print(top_customers_sales)

# Most valuable customers by state
valuable_customers = df.groupby(['State', 'Customer Name'])['Sales'].sum().nlargest(10)
print("\nMost valuable customers by state:")
print(valuable_customers)

# Unique customers in each region
unique_customers_region = df.groupby(['Region', 'Customer Name'])['Sales'].max().groupby(level=0, group_keys=False).nlargest(10).reset_index().head(10)
print("\nUnique customers in each region:")
print(unique_customers_region)

# Customer segments generating the most profit
profit_by_segment = df.groupby(['Customer Name', 'Segment'])['Profit'].sum().sort_values(ascending=False)
print("\nProfit by Customer Segment:")
print(profit_by_segment)

# Most popular categories and sub-categories
popular_products = df.groupby(['Category', 'Sub-Category'])['Sales'].max().sort_values(ascending=False).head(10)
print("\nMost popular product categories and sub-categories:")
print(popular_products)

# Least profitable products
least_profitable_products = df.groupby('Sub-Category')['Profit'].min().sort_values(ascending=True).head(10)
print("\nLeast profitable products:")
print(least_profitable_products)

# Check if 'Order Date' column is already in datetime format, if not convert it
if df['Order Date'].dtype != 'datetime64[ns]':
    df['Order Date'] = pd.to_datetime(df['Order Date'], format="%d-%m-%Y", dayfirst=True)

# 1. Total Sales and Profit by Region (Bar Chart)
region_sales_profit = df.groupby('Region')[['Sales', 'Profit']].sum().reset_index()
region_sales_profit.plot(
    x='Region', 
    y=['Sales', 'Profit'], 
    kind='bar', 
    figsize=(10, 6), 
    title='Total Sales and Profit by Region'
)
plt.xlabel('Region')
plt.ylabel('Amount')
plt.show()



# 2. Top 10 Selling Products (Horizontal Bar Chart)
top_products = df.groupby('Product Name')['Sales'].sum().sort_values(ascending=False).head(10)
top_products.plot(kind='barh', figsize=(10, 6), color='green', title='Top 10 Selling Products')
plt.xlabel('Total Sales')
plt.ylabel('Product Name')
plt.show()


# 3. Shipping Mode Usage (Bar Chart)
ship_mode_counts = df['Ship Mode'].value_counts()
ship_mode_counts.plot(kind='bar', figsize=(8, 6), color='orange', title='Shipping Mode Usage')
plt.xlabel('Shipping Mode')
plt.ylabel('Count')
plt.show()

# 4. Sales and Profit Heatmap by Region and Category
heatmap_data = df.pivot_table(index='Region', columns='Category', values='Profit', aggfunc='sum')
plt.figure(figsize=(10, 8))
sns.heatmap(heatmap_data, annot=True, fmt='.2f', cmap='coolwarm', cbar=True)
plt.title('Profit Heatmap by Region and Category')
plt.show()

# 5.Sales volume across sub-categories
sales_volume = df.groupby('Sub-Category')['Sales'].sum().reset_index()
plt.bar(sales_volume['Sub-Category'], sales_volume['Sales'])
plt.xlabel('Sub-Category')
plt.ylabel('Sales')
plt.title('Sales Volume Across Sub-Categories')
plt.show()

#6 Sales trends over time (monthly)
df['Order Date'] = pd.to_datetime(df['Order Date'], format="%d-%m-%Y", dayfirst=True)
df['Year'] = df['Order Date'].dt.year
df['Month'] = df['Order Date'].dt.month
monthly_sales = df.groupby([df['Year'], df['Month']])['Sales'].sum().reset_index()

plt.bar(monthly_sales['Month'], monthly_sales['Sales'], color='blue')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.title('Sales Trends Over Time')
plt.show()

# Most commonly used shipping mode
shipping_mode_counts = df['Ship Mode'].value_counts()
most_common_ship_mode = shipping_mode_counts.idxmax()
most_common_ship_mode_count = shipping_mode_counts.max()
print(f"\nThe most common shipping mode is {most_common_ship_mode}, with {most_common_ship_mode_count} counts.")

# States or cities generating the most sales and profit
most_profitable_locations = df.groupby(['State', 'City'])['Profit'].sum().sort_values(ascending=False).head(10)
print("\nStates or cities generating the most sales and profit:")
print(most_profitable_locations)
