# ==========================================
# UNEMPLOYMENT ANALYSIS PROJECT
# ==========================================

# Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ==========================================
# LOAD DATASET
# ==========================================

df = pd.read_csv("Unemployment_Rate_upto_11_2020.csv")

print("========== FIRST 5 ROWS ==========")
print(df.head())

print("\n========== DATASET INFO ==========")
print(df.info())

# ==========================================
# CLEAN COLUMN NAMES
# ==========================================

df.columns = df.columns.str.strip()

print("\n========== COLUMN NAMES ==========")
print(df.columns.tolist())

# ==========================================
# CLEAN STRING VALUES
# ==========================================

for col in df.select_dtypes(include='object').columns:
    df[col] = df[col].astype(str).str.strip()

# ==========================================
# MISSING VALUES
# ==========================================

print("\n========== MISSING VALUES ==========")
print(df.isnull().sum())

# Remove duplicates
df.drop_duplicates(inplace=True)

# Forward fill missing values if any
df = df.ffill()

# ==========================================
# CONVERT DATE COLUMN
# ==========================================

df['Date'] = pd.to_datetime(
    df['Date'],
    dayfirst=True,
    errors='coerce'
)

# Check for invalid dates
if df['Date'].isnull().sum() > 0:
    print("Warning: Some dates could not be converted.")

# ==========================================
# DESCRIPTIVE STATISTICS
# ==========================================

print("\n========== STATISTICAL SUMMARY ==========")
print(df.describe())

# ==========================================
# CORRELATION HEATMAP
# ==========================================

plt.figure(figsize=(8,6))

numeric_df = df.select_dtypes(include=['number'])

sns.heatmap(
    numeric_df.corr(),
    annot=True,
    cmap='coolwarm'
)

plt.title("Correlation Heatmap")
plt.tight_layout()
plt.show()

# ==========================================
# DISTRIBUTION OF UNEMPLOYMENT RATE
# ==========================================

plt.figure(figsize=(8,5))

sns.histplot(
    df['Estimated Unemployment Rate (%)'],
    bins=20,
    kde=True
)

plt.title("Distribution of Unemployment Rate")
plt.xlabel("Unemployment Rate (%)")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

# ==========================================
# STATE-WISE UNEMPLOYMENT RATE
# ==========================================

plt.figure(figsize=(15,6))

sns.barplot(
    data=df,
    x='Region',
    y='Estimated Unemployment Rate (%)'
)

plt.xticks(rotation=90)
plt.title("State-wise Unemployment Rate")
plt.xlabel("State")
plt.ylabel("Unemployment Rate (%)")
plt.tight_layout()
plt.show()

# ==========================================
# BOXPLOT BY STATE
# ==========================================

plt.figure(figsize=(15,6))

sns.boxplot(
    data=df,
    x='Region',
    y='Estimated Unemployment Rate (%)'
)

plt.xticks(rotation=90)
plt.title("Unemployment Rate Distribution by State")
plt.tight_layout()
plt.show()

# ==========================================
# UNEMPLOYMENT TREND OVER TIME
# ==========================================

plt.figure(figsize=(12,6))

sns.lineplot(
    data=df,
    x='Date',
    y='Estimated Unemployment Rate (%)'
)

plt.title("Unemployment Rate Over Time")
plt.xlabel("Date")
plt.ylabel("Unemployment Rate (%)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# ==========================================
# AVERAGE UNEMPLOYMENT RATE BY STATE
# ==========================================

state_avg = df.groupby('Region')['Estimated Unemployment Rate (%)'].mean()

print("\n========== AVERAGE UNEMPLOYMENT RATE ==========")
print(state_avg.sort_values(ascending=False))

# ==========================================
# TOP 10 STATES WITH HIGHEST UNEMPLOYMENT
# ==========================================

top10 = state_avg.sort_values(ascending=False).head(10)

plt.figure(figsize=(12,6))

top10.plot(kind='bar')

plt.title("Top 10 States with Highest Unemployment")
plt.xlabel("State")
plt.ylabel("Average Unemployment Rate (%)")
plt.tight_layout()
plt.show()

# ==========================================
# EMPLOYMENT BY STATE
# ==========================================

plt.figure(figsize=(15,6))

sns.barplot(
    data=df,
    x='Region',
    y='Estimated Employed'
)

plt.xticks(rotation=90)
plt.title("Estimated Employment by State")
plt.tight_layout()
plt.show()

# ==========================================
# LABOUR PARTICIPATION RATE
# ==========================================

plt.figure(figsize=(15,6))

sns.barplot(
    data=df,
    x='Region',
    y='Estimated Labour Participation Rate (%)'
)

plt.xticks(rotation=90)
plt.title("Labour Participation Rate by State")
plt.tight_layout()
plt.show()

# ==========================================
# REGION-WISE ANALYSIS
# ==========================================

plt.figure(figsize=(8,5))

sns.barplot(
    data=df,
    x='Region.1',
    y='Estimated Unemployment Rate (%)'
)

plt.title("Region-wise Unemployment Rate")
plt.xlabel("Indian Region")
plt.ylabel("Unemployment Rate (%)")
plt.tight_layout()
plt.show()

# ==========================================
# TOP 5 HIGHEST UNEMPLOYMENT STATES
# ==========================================

top5 = state_avg.sort_values(ascending=False).head(5)

plt.figure(figsize=(10,5))

sns.barplot(
    x=top5.index,
    y=top5.values
)

plt.title("Top 5 States with Highest Unemployment")
plt.ylabel("Average Unemployment Rate (%)")
plt.tight_layout()
plt.show()

# ==========================================
# TOP 5 LOWEST UNEMPLOYMENT STATES
# ==========================================

bottom5 = state_avg.sort_values().head(5)

plt.figure(figsize=(10,5))

sns.barplot(
    x=bottom5.index,
    y=bottom5.values
)

plt.title("Top 5 States with Lowest Unemployment")
plt.ylabel("Average Unemployment Rate (%)")
plt.tight_layout()
plt.show()

# ==========================================
# PROJECT INSIGHTS
# ==========================================

highest_state = state_avg.idxmax()
highest_rate = state_avg.max()

lowest_state = state_avg.idxmin()
lowest_rate = state_avg.min()

print("\n========== PROJECT INSIGHTS ==========")

print(
    f"Highest Average Unemployment Rate: "
    f"{highest_state} ({highest_rate:.2f}%)"
)

print(
    f"Lowest Average Unemployment Rate: "
    f"{lowest_state} ({lowest_rate:.2f}%)"
)

print("\n========== CONCLUSION ==========")
print("COVID-19 had a significant impact on unemployment across India.")
print(f"{highest_state} recorded the highest average unemployment rate.")
print(f"{lowest_state} recorded the lowest average unemployment rate.")
print("The analysis reveals notable regional differences in employment trends.")

print("\n🎉 Project Completed Successfully! 🎉")
