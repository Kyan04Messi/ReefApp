import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Set up page
st.set_page_config(page_title="Model Visualisation Dashboard", layout="wide")

st.title("📊 Model Visualisation Dashboard")

# Define the models with initial values
initial_models = [
    {"Model": "Government Initiative", "Risk": 8, "Community": 5, "Business": 6, "Government": 9, "Environment": 7},
    {"Model": "Community Driven", "Risk": 8, "Community": 9, "Business": 5, "Government": 4, "Environment": 7},
    {"Model": "Private Sector", "Risk": 7, "Community": 4, "Business": 9, "Government": 5, "Environment": 6},
    {"Model": "Research Think Tank", "Risk": 6, "Community": 5, "Business": 6, "Government": 6, "Environment": 7},
    {"Model": "Hybrid Model", "Risk": 5, "Community": 7, "Business": 7, "Government": 7, "Environment": 6},
    {"Model": "Grassroots Initiative", "Risk": 7, "Community": 8, "Business": 3, "Government": 3, "Environment": 8},
    {"Model": "Academic Institution", "Risk": 6, "Community": 6, "Business": 5, "Government": 6, "Environment": 7},
    {"Model": "NGO Collaboration", "Risk": 7, "Community": 7, "Business": 4, "Government": 5, "Environment": 8},
    {"Model": "Policy Innovation Lab", "Risk": 6, "Community": 6, "Business": 6, "Government": 8, "Environment": 7}
]

models_df = pd.DataFrame(initial_models)

# Dropdown to choose model
selected_model = st.selectbox("Choose a Model to Explore:", models_df["Model"])
model_row = models_df[models_df["Model"] == selected_model].iloc[0]

st.subheader(f"🛠️ Adjust Parameters for: {selected_model}")

col1, col2 = st.columns(2)

with col1:
    risk = st.slider("Risk Factor", 1, 10, int(model_row["Risk"]))
    community = st.slider("Community Alignment", 1, 10, int(model_row["Community"]))
    business = st.slider("Business Alignment", 1, 10, int(model_row["Business"]))

with col2:
    government = st.slider("Government Alignment", 1, 10, int(model_row["Government"]))
    environment = st.slider("Environmental Alignment", 1, 10, int(model_row["Environment"]))

# Calculate simple probability of success
probability = max(0, 100 - (risk * 10))
st.markdown(f"### 📈 Estimated Probability of Success: **{probability}%**")

# Radar chart data
categories = ["Risk", "Community", "Business", "Government", "Environment"]
values = [risk, community, business, government, environment]

# Reverse risk scale so that higher values look worse visually
radar_values = [11 - risk, community, business, government, environment]  # invert risk (1 = good, 10 = bad)

# Radar chart
fig = go.Figure()
fig.add_trace(go.Scatterpolar(
    r=radar_values,
    theta=categories,
    fill='toself',
    name=selected_model,
    line=dict(color='royalblue')
))
fig.update_layout(
    polar=dict(
        radialaxis=dict(
            visible=True,
            range=[0, 10]
        )
    ),
    showlegend=False,
    height=500,
    margin=dict(t=40, l=20, r=20, b=20)
)

st.plotly_chart(fig, use_container_width=True)

# Optional: show static comparison table
with st.expander("📋 See All Models for Comparison"):
    comparison_df = models_df.copy()
    comparison_df["Probability"] = 100 - (comparison_df["Risk"] * 10)
    st.dataframe(comparison_df.reset_index(drop=True))
