import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    'Category': ['A', 'A', 'B', 'B', 'C', 'C', 'D', 'D', 'E', 'E'],
    'Subcategory': ['A1', 'A2', 'B1', 'B2', 'C1', 'C2', 'D1', 'D2', 'E1', 'E2'],
    'Values': [23, 19, 17, 22, 35, 32, 29, 24, 12, 15]
}

df = pd.DataFrame(data)

grouped_df = df.groupby('Category').sum().reset_index()

plt.figure(figsize=(10, 6))
sns.barplot(x='Category', y='Values', data=grouped_df, palette='viridis')
plt.title('Bar Plot of Total Values per Category')
plt.show()

pivot_df = df.pivot(index='Category', columns='Subcategory', values='Values')
pivot_df.plot(kind='bar', stacked=True, figsize=(10, 6), colormap='Spectral')
plt.title('Stacked Bar Plot of Categories and Subcategories')
plt.ylabel('Values')
plt.show()

plt.figure(figsize=(8, 8))
plt.pie(grouped_df['Values'], labels=grouped_df['Category'], autopct='%1.1f%%', startangle=140, colors=sns.color_palette('Set2'))
plt.title('Pie Chart of Total Values per Category')
plt.show()

plt.figure(figsize=(10, 6))
plt.plot(df['Category'], df['Values'], 'bo')  
plt.title('Dot Plot of Categories and Subcategories')
plt.xlabel('Category')
plt.ylabel('Values')
plt.show()

plt.figure(figsize=(10, 6))
sns.boxplot(x='Category', y='Values', data=df, palette='Set3')
plt.title('Box Plot of Value Distribution by Category')
plt.show()

plt.figure(figsize=(8, 6))
sns.heatmap(pivot_df, annot=True, cmap='Blues', cbar=True)
plt.title('Heatmap of Values across Subcategories')
plt.show()

summary = df.describe()
print("Summary Statistics:\n", summary)