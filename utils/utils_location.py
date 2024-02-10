import streamlit as st
import pandas as pd
import plotly.express as px

# Load the data
def load_data(file_path):
    data = pd.read_csv(file_path)
    return data

# Filter data based on city and/or state
def filter_data(df, city=None, state=None):
    if city and state:
        filtered_df = df[(df['City'].str.lower() == city.lower()) & (df['State'].str.lower() == state.lower())]
    elif city:
        filtered_df = df[df['City'].str.lower() == city.lower()]
    elif state:
        filtered_df = df[df['State'].str.lower() == state.lower()]
    else:
        filtered_df = df
    return filtered_df

# Plot CO2 emissions by year using Plotly
def plot_co2_emissions_by_year(df):
    emissions_by_year = df.groupby('Year')['CO2_emissions'].sum().reset_index()
    fig = px.bar(emissions_by_year, x='Year', y='CO2_emissions', 
                 labels={'CO2_emissions': 'Total CO2 Emissions'}, 
                 title='Total CO2 Emissions by Year')
    fig.update_layout(xaxis_title='Year', yaxis_title='Total CO2 Emissions')
    st.plotly_chart(fig, use_container_width=True)

# Plot distribution of emissions types using Plotly
def plot_emissions_distribution(df):
    total_co2 = df['CO2_emissions'].sum()
    total_methane = df['CH4_emissions'].sum()
    total_nitrous_oxide = df['N2O_emissions'].sum()
    emissions = pd.DataFrame({
        'Emissions Type': ['CO2 Emissions', 'Methane Emissions', 'Nitrous Oxide Emissions'],
        'Total': [total_co2, total_methane, total_nitrous_oxide]
    })
    fig = px.pie(emissions, names='Emissions Type', values='Total', 
                 title='Distribution of Emissions Types', 
                 color_discrete_sequence=px.colors.qualitative.Pastel)
    st.plotly_chart(fig, use_container_width=True)

# Plot emissions by sector using Plotly (no change needed)
def plot_emissions_by_sector(df):
    emissions_by_sector = df.groupby('Sector')['CO2_emissions'].sum().reset_index()
    fig = px.sunburst(emissions_by_sector, path=['Sector'], values='CO2_emissions',
                      color='CO2_emissions', hover_data=['Sector'],
                      color_continuous_scale='RdBu',
                      title='Emissions Breakdown by Sector')
    st.plotly_chart(fig, use_container_width=True)

# Plot dynamic scatter comparing CO2 and N2O emissions
def plot_dynamic_scatter(df):
    fig = px.scatter(df, x='CO2_emissions', y='N2O_emissions',
                     color='Sector', hover_data=['Facility.Name', 'City', 'State'],
                     title='CO2 vs. N2O Emissions by Sector')

    # Update layout for titles and figure size
    fig.update_layout(
        xaxis_title='CO2 Emissions',
        yaxis_title='Nitrous Oxide Emissions',
        coloraxis_colorbar=dict(title="Sector"),
        # Set fixed figure size: width x height in pixels
        width=800,  # Adjust width as needed
        height=600,  # Adjust height as needed
        # Adjust margins to ensure titles fit
        margin=dict(l=20, r=20, t=50, b=80)
    )

    st.plotly_chart(fig, use_container_width=False)  # Set use_container_width to False to use fixed size
