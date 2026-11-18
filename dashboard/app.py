import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Superstore Dashboard", layout="wide")

df = pd.read_csv("dataset/cleaned_superstore.csv")
df["Order Date"] = pd.to_datetime(df["Order Date"])

st.title("Superstore Interactive Sales Dashboard")
st.write("Sales and Business Performance Analysis")

# Sidebar filters
st.sidebar.header("Filters")

regions = st.sidebar.multiselect("Region", df["Region"].unique(), default=df["Region"].unique())
categories = st.sidebar.multiselect("Category", df["Category"].unique(), default=df["Category"].unique())
segments = st.sidebar.multiselect("Segment", df["Segment"].unique(), default=df["Segment"].unique())

filtered = df[
    df["Region"].isin(regions) &
    df["Category"].isin(categories) &
    df["Segment"].isin(segments)
]

# Key metrics
c1, c2, c3, c4 = st.columns(4)

c1.metric("Total Sales", f"${filtered['Sales'].sum():,.2f}")
c2.metric("Total Profit", f"${filtered['Profit'].sum():,.2f}")
c3.metric("Total Orders", filtered["Order ID"].nunique())
c4.metric("Average Sales", f"${filtered['Sales'].mean():,.2f}")

st.divider()

# Monthly sales
monthly = filtered.groupby(filtered["Order Date"].dt.to_period("M"))["Sales"].sum().reset_index()
monthly["Order Date"] = monthly["Order Date"].astype(str)

fig1 = px.line(monthly, x="Order Date", y="Sales", title="Monthly Sales Trend", markers=True)
st.plotly_chart(fig1, use_container_width=True)

# Category and region charts
c1, c2 = st.columns(2)

category = filtered.groupby("Category")["Sales"].sum().reset_index()
fig2 = px.bar(category, x="Category", y="Sales", color="Category", title="Sales by Category")
c1.plotly_chart(fig2, use_container_width=True)

region = filtered.groupby("Region")["Profit"].sum().reset_index()
fig3 = px.bar(region, x="Region", y="Profit", color="Region", title="Profit by Region")
c2.plotly_chart(fig3, use_container_width=True)

# Segment chart
segment = filtered.groupby("Segment")["Sales"].sum().reset_index()
fig4 = px.pie(segment, names="Segment", values="Sales", title="Sales by Customer Segment")
st.plotly_chart(fig4, use_container_width=True)

# Top products
top = filtered.groupby("Product Name")["Sales"].sum().nlargest(10).reset_index()
fig5 = px.bar(top, x="Sales", y="Product Name", orientation="h", title="Top 10 Products")
st.plotly_chart(fig5, use_container_width=True)

st.subheader("Sales Data")
st.dataframe(filtered, use_container_width=True)

st.success("Dashboard loaded successfully!")
