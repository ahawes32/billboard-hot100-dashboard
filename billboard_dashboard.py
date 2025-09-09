import streamlit as st
import pandas as pd
import plotly.express as px

# Load data
df = pd.read_csv("data/billboard_hot100_sample.csv")

st.title("🎶 Billboard Hot 100 Trends Dashboard")
st.write("Explore trends in Billboard Hot 100 songs and artists.")

# Sidebar filters
artist = st.sidebar.selectbox("Select an Artist", ["All"] + sorted(df["Artist"].unique().tolist()))
song = st.sidebar.selectbox("Select a Song", ["All"] + sorted(df["Song"].unique().tolist()))

filtered_df = df.copy()
if artist != "All":
    filtered_df = filtered_df[filtered_df["Artist"] == artist]
if song != "All":
    filtered_df = filtered_df[filtered_df["Song"] == song]

# Line chart - Rankings over time
fig = px.line(filtered_df, x="Week", y="Rank", color="Song", markers=True,
              title="Song Rankings Over Time", labels={"Rank": "Chart Position"})
fig.update_yaxes(autorange="reversed")  # Rank 1 at the top
st.plotly_chart(fig)

# Bar chart - Average rank per artist
avg_rank = df.groupby("Artist")["Rank"].mean().reset_index()
fig2 = px.bar(avg_rank, x="Artist", y="Rank", title="Average Chart Position by Artist")
fig2.update_yaxes(autorange="reversed")
st.plotly_chart(fig2)

st.write("Data Source: Sample Billboard Hot 100 dataset (for demo purposes).")
