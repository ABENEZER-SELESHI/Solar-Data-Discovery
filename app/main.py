import streamlit as st
import plotly.express as px
from app.utils import load_data, get_top_regions

st.set_page_config(page_title="GHI Dashboard", layout="wide")

df = load_data()

st.sidebar.header("Filter Options")
countries = df["Country"].unique().tolist()
selected_countries = st.sidebar.multiselect("Select Countries", countries, default=countries)

filtered_df = df[df["Country"].isin(selected_countries)]

st.title("Global Health Index Dashboard")
st.subheader("GHI Score Distribution")

if not filtered_df.empty:
    fig = px.box(filtered_df, x="Country", y="GHI", color="Country", title="GHI Boxplot by Country")
    st.plotly_chart(fig, use_container_width=True)
else:
    st.warning("Please select at least one country to display the chart.")

st.subheader("🏆 Top Regions by Average GHI")
st.dataframe(get_top_regions(df))

st.markdown("---")
st.markdown("Built using Streamlit")
