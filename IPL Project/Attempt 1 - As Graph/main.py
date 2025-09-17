# run pip install pandas matplotlib seaborn in terminal for this project

print("Name: Dave Pujan M.,\nEnrollment No.: 230130107024\n")

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 📥 Load Dataset (Ensure 'matches.csv' and 'deliveries.csv' are in the same directory)
matches = pd.read_csv(r"E:\Clg\Sem 5\3150713 - Python for Data Science\IPL Project\matches.csv")
deliveries = pd.read_csv(r"E:\Clg\Sem 5\3150713 - Python for Data Science\IPL Project\deliveries.csv")

# 🔍 Basic Dataset Info
print("First 5 rows of Matches dataset:\n", matches.head())
print("First 5 rows of Deliveries dataset:\n", deliveries.head())
print("Available Seasons in Dataset:", matches['season'].unique())

# 📊 Top Winning Teams
top_teams = matches['winner'].value_counts().head(5)
plt.figure(figsize=(8, 5))
sns.barplot(x=top_teams.index, y=top_teams.values, palette="Set2")
plt.title("Top 5 Teams by Match Wins")
plt.ylabel("Wins")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 🏏 Top 10 Batsmen by Total Runs
batsman_runs = deliveries.groupby('batsman')['batsman_runs'].sum().sort_values(ascending=False).head(10)
plt.figure(figsize=(8, 5))
batsman_runs.plot(kind='bar', colormap='viridis')
plt.title("Top 10 Batsmen by Total Runs")
plt.ylabel("Total Runs")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 🎯 Top 10 Batsmen by Strike Rate (min 500 runs)
balls = deliveries.groupby('batsman')['ball'].count()
runs = deliveries.groupby('batsman')['batsman_runs'].sum()
strike_rate = (runs / balls) * 100
top_sr = strike_rate[runs > 500].sort_values(ascending=False).head(10)
plt.figure(figsize=(8, 5))
top_sr.plot(kind='bar', color='green')
plt.title("Top 10 Batsmen Strike Rate (min 500 runs)")
plt.ylabel("Strike Rate")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 🎳 Top 10 Bowlers by Wickets
wickets = deliveries[deliveries['dismissal_kind'].notnull()]
top_bowlers = wickets['bowler'].value_counts().head(10)
plt.figure(figsize=(8, 5))
sns.barplot(x=top_bowlers.index, y=top_bowlers.values, palette='coolwarm')
plt.title("Top 10 Bowlers by Wickets")
plt.ylabel("Wickets")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 🏟️ Top Venues Favoring Chasing Teams
chasing_wins = matches[matches['win_by_wickets'] > 0]['venue'].value_counts().head(10)
plt.figure(figsize=(8, 5))
chasing_wins.plot(kind='barh', color='orange')
plt.title("Top Venues Favoring Chasing Teams")
plt.xlabel("Matches Won by Chasing")
plt.tight_layout()
plt.show()
