import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file into a DataFrame
df = pd.read_csv(r'C:\Users\SIC\prajwal_python\sic\day 8 Hackathon\Hackathon_dataset.csv')
# Filter to keep only the first 10 rows
df = df.head(10)
# Create a bar graph for Price vs Discount
plt.figure(figsize=(12, 6))
plt.bar(df['Price'], df['Discount'], color='g', width=5)
plt.xlabel('Price', fontsize=14)
plt.ylabel('Discount', fontsize=14)
plt.title('Graph Between Price and Discount', fontsize=16)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.grid(axis='y')
plt.show()