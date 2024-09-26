import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the books.csv file
df = pd.read_csv('books (1).csv')

# Display dataset info
print("Dataset Information:")
df.info()

# Display the first 5 rows of the dataset
print("\nFirst 5 Rows of the Dataset:")
print(df.head())

# Check for missing values in the dataset
print("\nMissing Values in the Dataset:")
print(df.isnull().sum())

# Clean Price column (remove £ symbol and convert to float)
df['Price'] = df['Price'].str.replace('£', '').astype(float)

# Countplot for the availability of books
plt.figure(figsize=(8, 6))
sns.countplot(x='Availability', data=df, palette='pastel')
plt.title('Book Availability')
plt.xlabel('Availability')
plt.ylabel('Number of Books')
plt.savefig('availability_distribution.png')  
plt.show()

# Histogram for the distribution of book prices
plt.figure(figsize=(8, 6))
sns.histplot(df['Price'], kde=True, color='green')
plt.title('Distribution of Book Prices')
plt.xlabel('Price (£)')
plt.ylabel('Frequency')
plt.savefig('price_distribution.png')  
plt.show()

# Boxplot for the price distribution
plt.figure(figsize=(8, 6))
sns.boxplot(y='Price', data=df, palette='Spectral')
plt.title('Box Plot of Book Prices')
plt.ylabel('Price (£)')
plt.savefig('box_plot_prices.png') 
plt.show()
