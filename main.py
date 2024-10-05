import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_csv('players_20.csv')


# Display the first few rows of the dataset
print(df.head())

# Show basic statistics for the dataset
print(df.describe())

# Check for missing values
print(df.isnull().sum())

# Get the data types of each column
# print(df.dtypes)

# Remove any duplicate rows
df = df.drop_duplicates()

# Handle missing values (if any)
df.fillna(0, inplace=True)  # Simple approach - fill missing values with 0

# Drop unnecessary columns
# df = df.drop(['Unwanted_Column1', 'Unwanted_Column2'], axis=1)

# Count occurrences of a specific category
# print(df['weight_kg'].value_counts())

# Histogram of player ages
df['age'].hist(bins=20)
plt.title('Distribution of Player Ages')
plt.xlabel('Age')
plt.ylabel('Number of Players')
plt.show()

# Pick Numbers Only
numeric_df = df.select_dtypes(include='number')

# Select specific columns you want to focus on
selected_columns = ['overall', 'age', 'potential', 'value_eur', 'wage_eur', 'height_cm', 'weight_kg']

# Create a new DataFrame with only the selected columns
limited_df = numeric_df[selected_columns]

# Generate the heatmap for the selected columns
plt.figure(figsize=(12, 8))
sns.heatmap(limited_df.corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.xticks(rotation=45, ha='right')
plt.title('Correlation Heatmap of Selected Features')
plt.show()

# Average Overall Rating by Preferred Foot
plt.figure(figsize=(8, 6))

# Create the bar plot with error bars (standard deviation) and assign the 'preferred_foot' to hue
sns.barplot(x='preferred_foot', y='overall', data=df, errorbar='sd', hue='preferred_foot', palette="Blues", dodge=False)

# Add title and labels
plt.title('Average Overall Rating by Preferred Foot', fontsize=16)
plt.xlabel('Preferred Foot', fontsize=14)
plt.ylabel('Average Overall Rating', fontsize=14)

# Set the y-axis limit to focus on the range of the data
plt.ylim(50, 70)

# Remove the legend since it's unnecessary for this plot
plt.legend([], [], frameon=False)

# Display the plot
plt.show()
# #
#
# Get the top 10 countries by number of players
top_countries = df['nationality_name'].value_counts().head(10)
#
# Create a bar plot
sns.barplot(x=top_countries.index, y=top_countries.values)
plt.title('Top 10 Countries by Number of Players')
plt.xlabel('Country')
plt.ylabel('Number of Players')
plt.xticks(rotation=45)
plt.show()