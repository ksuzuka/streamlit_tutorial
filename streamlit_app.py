import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("state_data.csv")

st.header("Changes in US State Demographics Over Time")

# Let user select which state to view and which demographic data to view
state = st.selectbox("State:", df["State"].unique()) 
demographic = st.selectbox("Demographic:", ["Total Population", "Median Household Income"])

# Create tabs
tab1, tab2 = st.tabs(["📈 Graph", "🔍 Data"],width="stretch")
with tab1:
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
        st.plotly_chart(fig)
with tab2:
# Show the entire dataframe
        st.write("All Data")
        st.dataframe(df)
