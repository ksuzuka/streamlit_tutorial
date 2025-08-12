import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("state_data.csv")

st.header("US State Demographics")

# Let user select which state and demographic to graph
state = st.selectbox("State:", df["State"].unique())
demographic = st.selectbox(
    "Demographic:", ["Total Population", "Median Household Income"]
)

graph_tab, table_tab = st.tabs(["📈 Graphs", "🔍 Table"])

with graph_tab:
    # Create the graph the user requested
    df_state = df[df["State"] == state]
    if demographic == "Total Population":
        fig = px.line(
            df_state,
            x="Year",
            y="Total Population",
            title=f"Total Population of {state}",
        )
    elif demographic == "Median Household Income":
        fig = px.line(
            df_state,
            x="Year",
            y="Median Household Income",
            title=f"Median Household Income of {state}",
        )
    else:
        raise ValueError("Unknown demographic!")
    st.plotly_chart(fig)
with table_tab:
    # Render the entire dataframe
    st.dataframe(df)
