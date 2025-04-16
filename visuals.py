import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv(r'C:\Users\Lavanya\Downloads\archive\online_retail_II.csv')

# Convert InvoiceDate to datetime
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

# Drop missing values
df = df.dropna(subset=['Invoice', 'Quantity', 'Price'])

# Remove canceled orders
df = df[~df['Invoice'].astype(str).str.startswith('C')]

# Create Year, Month columns
df['Year'] = df['InvoiceDate'].dt.year
df['Month'] = df['InvoiceDate'].dt.month

# Calculate revenue
df['Revenue'] = df['Quantity'] * df['Price']

# Monthly summary
monthly_summary = df.groupby(['Year', 'Month']).agg({
    'Revenue': 'sum',
    'Invoice': 'nunique'
}).reset_index().rename(columns={'Revenue': 'Monthly_Revenue', 'Invoice': 'Order_Volume'})

monthly_summary['Date'] = pd.to_datetime(monthly_summary['Year'].astype(str) + '-' + monthly_summary['Month'].astype(str))

# Plot 1: Monthly Trends
sns.set(style="whitegrid")
fig, ax1 = plt.subplots(figsize=(14, 6))

color = 'tab:blue'
ax1.set_xlabel('Date')
ax1.set_ylabel('Monthly Revenue (£)', color=color)
ax1.plot(monthly_summary['Date'], monthly_summary['Monthly_Revenue'], color=color, marker='o', label='Revenue')
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()
color = 'tab:orange'
ax2.set_ylabel('Order Volume', color=color)
ax2.plot(monthly_summary['Date'], monthly_summary['Order_Volume'], color=color, marker='x', label='Order Volume')
ax2.tick_params(axis='y', labelcolor=color)

plt.title('Monthly Revenue and Order Volume Trend')
plt.tight_layout()
plt.show()

# Plot 2: Top 10 Months by Revenue
top_revenue_months = monthly_summary.nlargest(10, 'Monthly_Revenue')
plt.figure(figsize=(12, 6))
sns.barplot(
    x=top_revenue_months['Date'].dt.strftime('%b %Y'),
    y=top_revenue_months['Monthly_Revenue'],
    palette='Blues_d'
)
plt.title('Top 10 Months by Revenue')
plt.xlabel('Month')
plt.ylabel('Revenue (£)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Plot 3: Top 10 Months by Order Volume
top_order_volume_months = monthly_summary.nlargest(10, 'Order_Volume')
plt.figure(figsize=(12, 6))
sns.barplot(
    x=top_order_volume_months['Date'].dt.strftime('%b %Y'),
    y=top_order_volume_months['Order_Volume'],
    palette='Oranges_d'
)
plt.title('Top 10 Months by Order Volume')
plt.xlabel('Month')
plt.ylabel('Order Volume')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

