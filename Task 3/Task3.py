import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('employees.csv') 

print("Dataset Information:")
df.info()

print("\nFirst 5 Rows of the Dataset:")
print(df.head())

print("\nStatistical Summary of the Dataset:")
print(df.describe())

print("\nMissing Values in the Dataset:")
print(df.isnull().sum())


df.dropna(inplace=True)

plt.figure(figsize=(8, 6))
sns.countplot(x='Gender', data=df, palette='pastel')
plt.title('Gender Distribution')
plt.xlabel('Gender')
plt.ylabel('Number of Employees')
plt.xticks(rotation=45)
plt.savefig('gender_distribution.png')  
plt.show()

plt.figure(figsize=(8, 6))
sns.barplot(x='Gender', y='Salary', data=df, palette='husl')
plt.title('Average Salary by Gender')
plt.xlabel('Gender')
plt.ylabel('Average Salary')
plt.xticks(rotation=45)
plt.savefig('average_salary_by_gender.png')  
plt.show()

plt.figure(figsize=(10, 6))
sns.histplot(df['Salary'], kde=True, color='green')
plt.title('Salary Distribution of Employees')
plt.xlabel('Salary')
plt.ylabel('Frequency')
plt.savefig('salary_distribution.png') 
plt.show()

plt.figure(figsize=(10, 6))
sns.heatmap(df.corr(), annot=True, cmap='viridis', fmt='.2f')
plt.title('Correlation Heatmap')
plt.savefig('correlation_heatmap.png')  
plt.show()

plt.figure(figsize=(10, 6))
sns.scatterplot(x='Experience', y='Salary', data=df, hue='Gender', palette='deep')
plt.title('Salary vs. Experience')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.savefig('salary_vs_experience.png')  
plt.show()

plt.figure(figsize=(10, 6))
sns.boxplot(x='Gender', y='Salary', data=df, palette='Spectral')
plt.title('Box Plot of Salary by Gender')
plt.xlabel('Gender')
plt.ylabel('Salary')
plt.savefig('box_plot_salary_by_gender.png') 
plt.show()