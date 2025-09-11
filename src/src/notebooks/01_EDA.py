# 01_EDA.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
df = pd.read_csv("data/sample.csv")

print("✅ Data Loaded Successfully")
print("\n📊 First 5 rows of data:\n", df.head())
print("\n🔢 Basic Info:")
print(df.info())
print("\n📈 Summary Statistics:\n", df.describe())

# Check missing values
print("\n🔍 Missing Values:\n", df.isnull().sum())

# Plot correlation heatmap
plt.figure(figsize=(8,5))
sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()

# Plot failure count
plt.figure(figsize=(5,3))
sns.countplot(x="failure", data=df)
plt.title("Failure Distribution")
plt.show()

# Plot temperature vs failure
plt.figure(figsize=(5,3))
sns.boxplot(x="failure", y="temperature", data=df)
plt.title("Temperature vs Failure")
plt.show()
