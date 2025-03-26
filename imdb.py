# 🚀 First things first: Install necessary libraries if they aren’t already installed
!pip install requests beautifulsoup4 pandas numpy matplotlib seaborn

# ✅ Import required libraries (because Python won’t run itself!)
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from google.colab import files  # Needed only for Google Colab users

# 🔹 Ask user to upload the dataset manually (Colab users)
print("📂 Please upload your IMDb dataset CSV file.")
files.upload()  # Opens file upload prompt

# 🔹 Load the dataset (make sure the filename is correct!)
file_path = "/content/imdb_top_1000.csv"  # Change this if needed
df = pd.read_csv(file_path)

# 🧐 Let's take a sneak peek at the dataset
print("\n🎬 First 5 movies in the dataset:")
df.head()

# 🔍 Quick dataset inspection
print("\n📊 Dataset Summary:")
df.info()

# ❌ Checking for missing values & duplicate entries
print("\n🔍 Missing values before cleaning:\n", df.isnull().sum())
df.drop_duplicates(inplace=True)  # Removing duplicate rows
df.dropna(inplace=True)  # Removing empty/missing data
print("\n✅ Missing values after cleaning:\n", df.isnull().sum())

# 🛠️ Data Type Fixes (because numbers should be numbers!)
df['Gross'] = df['Gross'].str.replace(',', '', regex=True).astype(float)  # Convert revenue to numeric
df['Released_Year'] = pd.to_numeric(df['Released_Year'], errors='coerce')  # Convert year to numbers

# 🎯 Let's start analyzing the data!

## 🔥 Top 10 highest-rated movies
print("\n🎥 These are the top 10 highest-rated movies:")
best_movies = df[['Series_Title', 'IMDB_Rating']].sort_values(by='IMDB_Rating', ascending=False).head(10)
print(best_movies)

## 🎭 What are the most popular genres?
df['Genre'] = df['Genre'].apply(lambda x: x.split(',')[0])  # Extracting the first genre if multiple exist

plt.figure(figsize=(10, 5))
sns.countplot(y=df['Genre'], order=df['Genre'].value_counts().index, palette="magma")
plt.title("🎭 Most Common Movie Genres")
plt.xlabel("Count")
plt.ylabel("Genre")
plt.show()

## 📈 How has movie production changed over the years?
movies_per_year = df['Released_Year'].value_counts().sort_index()

plt.figure(figsize=(12, 6))
sns.lineplot(x=movies_per_year.index, y=movies_per_year.values, marker="o", color="purple")
plt.xticks(rotation=90)
plt.title("📅 Number of Movies Released Each Year")
plt.xlabel("Year")
plt.ylabel("Total Movies")
plt.show()

## 💰 Does a higher IMDB rating mean more box office revenue?
plt.figure(figsize=(8, 5))
sns.scatterplot(x=df['IMDB_Rating'], y=df['Gross'], alpha=0.7, color='red')
plt.title("⭐ IMDB Rating vs. Box Office Revenue 💰")
plt.xlabel("IMDB Rating")
plt.ylabel("Gross Revenue ($)")
plt.show()

# 📢 Final Report: What did we learn?
print("\n📌 Key Takeaways from the Movie Data Analysis:")
print("✅ The highest-rated movies are:", best_movies['Series_Title'].tolist())
print("✅ The most common genres are:", df['Genre'].value_counts().index[:5].tolist())
print("✅ The number of movies produced each year fluctuates significantly.")
print("✅ A higher IMDB rating does not always guarantee massive box office earnings.")


