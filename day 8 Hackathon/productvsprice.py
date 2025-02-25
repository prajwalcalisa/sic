import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file into a DataFrame
df = pd.read_csv(r'C:\Users\SIC\prajwal_python\sic\day 8 Hackathon\Hackathon_dataset.csv')

# Filter to keep only the first 10 rows
df = df.head(10)

# Create a bar graph for Product ID vs Price
plt.figure(figsize=(12, 6))
plt.bar(df['Product ID'], df['Price'], color='b', width=0.5)
plt.xlabel('Product ID', fontsize=14)
plt.ylabel('Price', fontsize=14)
plt.title('Graph Between Product ID and Price', fontsize=16)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.grid(axis='y')
plt.show()