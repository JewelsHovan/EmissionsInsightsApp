import plotly.express as px
import streamlit as st
import pandas as pd

# Load the data
def load_data(file_path):
    data = pd.read_csv(file_path)
    return data

def create_top_sectors_pie_chart(data):
    # Summarize CO2 equivalent emissions by Sector
    emissions_by_sector = data.groupby('Sector')['CO2_eq_emissions'].sum().reset_index()
    
    # Filter for the top 10 sectors by CO2 equivalent emissions
    top_sectors = emissions_by_sector.nlargest(10, 'CO2_eq_emissions')

    # Create a pie chart for the top 10 sectors
    fig = px.pie(top_sectors, 
                 values='CO2_eq_emissions', 
                 names='Sector', 
                 title='Top 10 Sectors by Emissions',
                 color_discrete_sequence=px.colors.sequential.RdBu)

    # Update layout to center the title and adjust margins
    fig.update_layout(
        title={
            'text': 'Top 10 Sectors by Emissions',
            'y':0.95,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top'
        },
        margin=dict(l=20, r=20, t=60, b=20)
    )

    return fig


def create_emissions_trend_chart(data):
    # Aggregate emissions by year
    emissions_trend = data.groupby('Year').agg({
        'CO2_eq_emissions': 'sum',
        'CO2_emissions': 'sum'
    }).reset_index()

    # Rename 'CO2_eq_emissions' to 'Total Emissions' for clarity in the chart
    emissions_trend.rename(columns={'CO2_eq_emissions': 'Total Emissions'}, inplace=True)

    # Create the line chart
    fig = px.line(emissions_trend, 
                  x='Year', 
                  y=['Total Emissions', 'CO2_emissions'],
                  title='Trend of Emissions Over Time',
                  labels={'value': 'Emissions', 'variable': 'Emission Type'},
                  color_discrete_sequence=px.colors.qualitative.Set1)

    # Update layout to center the title and adjust margins
    fig.update_layout(
        title={
            'text': 'Trend of Emissions Over Time',
            'y':0.95,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top'
        },
        margin=dict(l=20, r=20, t=60, b=20)
    )

    return fig


def create_state_wise_emissions_map(data):
    # Summarize CO2 equivalent emissions by State
    emissions_by_state = data.groupby('State')['CO2_eq_emissions'].sum().reset_index()

    # Create a choropleth map for state-wise emissions
    fig = px.choropleth(emissions_by_state,
                        locations='State', 
                        locationmode="USA-states", 
                        color='CO2_eq_emissions',
                        scope="usa", 
                        title='State-wise Emissions in the US',
                        color_continuous_scale=px.colors.sequential.YlOrRd)

    # Update layout to adjust title and margins
    fig.update_layout(
        title={
            'text': 'State-wise Emissions in the US',
            'y':0.95,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top'
        },
        margin=dict(l=20, r=20, t=60, b=20),
        geo=dict(
            lakecolor='rgb(255, 255, 255)'  # Set lake color to white for better map readability
        )
    )

    return fig


def create_top_emitters_bar_chart(data):
    # Identify the top emitting facilities
    top_emitting_facilities = data.groupby(['Facility.Name', 'City', 'State'])['CO2_eq_emissions'].sum().reset_index().sort_values(by='CO2_eq_emissions', ascending=False).head(10)

    # Create a bar chart for top emitting facilities
    fig = px.bar(top_emitting_facilities, 
                 x='Facility.Name', 
                 y='CO2_eq_emissions', 
                 color='CO2_eq_emissions',
                 title='Top Emitting Facilities in the US',
                 labels={'CO2_eq_emissions': 'CO2 Equivalent Emissions', 'Facility.Name': 'Company Name'},
                 color_continuous_scale=px.colors.sequential.Blues)

    # Update layout to adjust title and margins
    fig.update_layout(
        title={
            'text': 'Top Emitting Facilities in the US',
            'y':0.95,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top'
        },
        margin=dict(l=20, r=20, t=60, b=20)
    )

    return fig

