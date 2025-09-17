# run pip install pandas plotly in terminal for this project
# Export As Websites
print("Name: Dave Pujan M.,\nEnrollment No.: 230130107024\n")

import pandas as pd
import numpy as np
import plotly.express as px

# 📥 Load Dataset (Ensure 'matches.csv' and 'deliveries.csv' paths are correct)
matches = pd.read_csv(r"E:\Clg\Sem 5\3150713 - Python for Data Science\IPL Project\matches.csv")
deliveries = pd.read_csv(r"E:\Clg\Sem 5\3150713 - Python for Data Science\IPL Project\deliveries.csv")

# 🔍 Basic Dataset Info
print("First 5 rows of Matches dataset:\n", matches.head())
print("First 5 rows of Deliveries dataset:\n", deliveries.head())
print("Available Seasons in Dataset:", matches['season'].unique())

# 📊 Top Winning Teams
top_teams = matches['winner'].value_counts().head(5).reset_index()
top_teams.columns = ['Team', 'Wins']
fig = px.bar(top_teams, x='Team', y='Wins', color='Team',
             title='Top 5 Teams by Match Wins')
fig.show()

# 🏏 Top 10 Batsmen by Total Runs
batsman_runs = deliveries.groupby('batsman')['batsman_runs'].sum().sort_values(ascending=False).head(10)
batsman_df = batsman_runs.reset_index()
batsman_df.columns = ['Batsman', 'Total Runs']
fig = px.bar(batsman_df, x='Batsman', y='Total Runs', color='Batsman',
             title='Top 10 Batsmen by Total Runs')
fig.show()

# 🎯 Top 10 Batsmen by Strike Rate (min 500 runs)
balls = deliveries.groupby('batsman')['ball'].count()
runs = deliveries.groupby('batsman')['batsman_runs'].sum()
strike_rate = (runs / balls) * 100
top_sr = strike_rate[runs > 500].sort_values(ascending=False).head(10).reset_index()
top_sr.columns = ['Batsman', 'Strike Rate']
fig = px.bar(top_sr, x='Batsman', y='Strike Rate', color='Batsman',
             title='Top 10 Batsmen Strike Rate (min 500 runs)')
fig.show()

# 🎳 Top 10 Bowlers by Wickets
wickets = deliveries[deliveries['dismissal_kind'].notnull()]
top_bowlers = wickets['bowler'].value_counts().head(10).reset_index()
top_bowlers.columns = ['Bowler', 'Wickets']
fig = px.bar(top_bowlers, x='Bowler', y='Wickets', color='Bowler',
             title='Top 10 Bowlers by Wickets')
fig.show()

# 🏟️ Top Venues Favoring Chasing Teams
chasing_wins = matches[matches['win_by_wickets'] > 0]['venue'].value_counts().head(10).reset_index()
chasing_wins.columns = ['Venue', 'Matches Won by Chasing']
fig = px.bar(chasing_wins, x='Matches Won by Chasing', y='Venue', orientation='h', color='Venue',
             title='Top Venues Favoring Chasing Teams')
fig.show()
