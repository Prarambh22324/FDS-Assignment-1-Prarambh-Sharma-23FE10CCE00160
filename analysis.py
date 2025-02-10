import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('FDS Assignment 1/rad.csv')
print(df.columns)
df['Accident Date'] = pd.to_datetime(df['Accident Date'], errors='coerce')
print(df.head())
print(df.info())

#Q1

df['Year'] = df['Accident Date'].dt.year
df['Month'] = df['Accident Date'].dt.month
df['Day_of_Week'] = df['Accident Date'].dt.day_name()
df['Hour'] = df['Accident Date'].dt.hour

plt.figure(figsize=(10, 5))
df['Year'].value_counts().sort_index().plot(kind='bar')
plt.title("Accidents Per Year")
plt.xlabel("Year")
plt.ylabel("Number of Accidents")
plt.show()

plt.figure(figsize=(10, 5))
df['Day_of_Week'].value_counts().plot(kind='bar')
plt.title("Accidents by Day of the Week")
plt.xlabel("Day")
plt.ylabel("Count")
plt.show()

#Q2

top_locations = df['Local_Authority_(District)'].value_counts().head(10)
plt.figure(figsize=(12, 6))
sns.barplot(x=top_locations.index, y=top_locations.values)
plt.xticks(rotation=90)
plt.title("Top 10 Accident-Prone Locations")
plt.ylabel("Number of Accidents")
plt.show()

#Q3

df['Accident_Severity'].value_counts().plot(kind='pie', autopct='%1.1f%%', figsize=(6, 6))
plt.title("Accident Severity Distribution")
plt.show()
sns.boxplot(x=df['Hour'], y=df['Accident_Severity'])
plt.title("Accident Severity vs. Time of Day")
plt.show()

#Q4

#No Gender or Age related information in the dataset

#Q5

df['Weather_Conditions'].value_counts().plot(kind='bar')
plt.title("Accidents under Different Weather Conditions")
plt.ylabel("Number of Accidents")
plt.show()
df['Road_Type'].value_counts().plot(kind='bar')
plt.title("Accidents by Road Type")
plt.ylabel("Number of Accidents")
plt.show()

#Q6

df['Vehicle_Type'].value_counts().head(10).plot(kind='bar')
plt.title("Most Involved Vehicle Types in Accidents")
plt.ylabel("Number of Accidents")
plt.show()

#Q7

df['IsWeekend'] = df['Day_of_Week'].isin(['Saturday', 'Sunday'])
df['IsWeekend'].value_counts().plot(kind='bar')
plt.title("Accidents on Weekdays vs Weekends")
plt.ylabel("Number of Accidents")
plt.xticks(ticks=[0, 1], labels=['Weekday', 'Weekend'])
plt.show()

#Q8

#No data available for contributing factors like Alcohol

#Q9

df['Accident_Severity'].value_counts().plot(kind='pie', autopct='%1.1f%%', figsize=(6, 6))
plt.title("Injury and Fatality Distribution")
plt.show()

#Q10

df['Urban_or_Rural_Area'].value_counts().plot(kind='bar')
plt.title("Accidents in Urban vs Rural Areas")
plt.ylabel("Number of Accidents")
plt.show()