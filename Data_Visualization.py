import matplotlib.pyplot as plt
import seaborn as sns

from pandas import DataFrame 

# Data Collected
data = {'names':['steve', 'john', 'richard', 'sarah', 'randy', 'micheal', 'julie'],
        'age':[20, 22, 20, 21, 24, 23, 22],
        'gender':['Male', 'Male', 'Male', 'Female', 'Male', 'Male', 'Female'],
        'rank':[2, 1, 4, 5, 3, 7, 6]}
df=DataFrame(data)
df

# Matplotlib's Bar Chart
plt.bar(df['names'], df['age'])
plt.xlabel('Names')
plt.ylabel('Age')
plt.title('Comparing Ages')
plt.show()

# Seaborn's Bar Chart
plot = sns.barplot(data=df, x='names', y = 'age')
plot.set_title("Comparing Ages")
plt.show()

# Line Plot Matplotlib
plt.plot(df['names'], df['age'])
plt.xlabel('Names')
plt.ylabel('Age')
plt.title('Comparing Ages')
plt.show()

# Line Plot Seaborn
plot = sns.lineplot(data=df, x='names', y = 'age')
plt.show()

# Pie Chart Matplotlib
plt.pie(df['age'], labels = df['names'])
plt.title("Age Comparison")
plt.show()

# Pie Chart Seaborn
colors = sns.color_palette('pastel')[0:5]
plt.pie(df['age'], labels = df['names'], colors = colors)
plt.show()



# Sencond Part

# Histogram
df['column_name'].hist(bins=20)
plt.show()

# Correlation Heatmap
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.show()

# Bar plot for categorical data
sns.barplot(x='category_column', y='numerical_column', data=df)
plt.show()
