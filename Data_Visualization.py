import matplotlib.pyplot as plt
import seaborn as sns

# Histogram
df['column_name'].hist(bins=20)
plt.show()

# Correlation Heatmap
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.show()

# Bar plot for categorical data
sns.barplot(x='category_column', y='numerical_column', data=df)
plt.show()