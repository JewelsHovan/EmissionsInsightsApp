import streamlit as st
import pandas as pd
from utils.utils_company import *

def show():
    st.title("Eco Emissions Company Dashboard 🌿")

    st.markdown("""
    ## Introduction
    This page allows a user to select a company, emission type, and a range of years for the selected company. 
    Explore the emissions data through various interactive visualizations and metrics to gain insights into the environmental impact.
    """)

    # Load the data
    data = load_data('data/Processed_Unit.csv')
    all_data = data.copy()

    # User Input Features in the sidebar
    company_name, date_range, emission_type = user_input_features()

    # Filtering data based on user input
    data, filtered_data = filter_data(data, company_name, date_range, emission_type)

    # Pivot the filtered_data DataFrame
    pivoted_data = pivot_data(filtered_data, emission_type)

    # Display the pivoted table
    st.write(f"### {company_name}")
    st.dataframe(pivoted_data)

    # Additional Step: Filter data for companies in the same sector as the selected company
    top_companies_df = calculate_sector_data(data, all_data, company_name, emission_type)

    # After calculating sector data
    top_companies_df = calculate_sector_data(data, all_data, company_name, emission_type)

    # Display Metrics
    st.write(f'### {emission_type} emissions')
    display_metrics(data, emission_type)


    # Add some space and a horizontal line for separation
    st.write("---")  # Adds a horizontal line for clear separation
    st.write("")  # Adds an empty line for extra spacing, adjust the number of calls to increase spacing

    # Calculate and display average emissions
    company_avg_emissions, sector_avg_emissions = calculate_average_emissions(data, all_data, company_name, emission_type, date_range)
    
    # Create columns for padding, left metric, right metric, and padding again
    padding_left, col1, col2, padding_right = st.columns([1, 2, 2, 1])  # Adjust the ratio as needed for better centering

    with col1:  # In the first main column, display the average emissions for the selected company
        st.metric(label=f"{company_name} Avg Emissions (Metric Tons)",
                value=f"{company_avg_emissions:.2f}",
                delta=None,
                delta_color="off")

    with col2:  # In the second main column, display the average sector emissions
        st.metric(label="Sector Avg Emissions (Metric Tons)",
                value=f"{sector_avg_emissions:.2f}",
                delta=None,
                delta_color="off")
        
    st.write("---")  # Adds a horizontal line for clear separation
    st.write("")  # Adds an empty line for extra spacing, adjust the number of calls to increase spacing

    # Generate and display the line chart
    line_chart = generate_line_chart(data, emission_type)
    st.altair_chart(line_chart, use_container_width=True)

    # Generate and display the bar chart using Plotly
    fig = generate_bar_chart(top_companies_df, emission_type, company_name)
    st.plotly_chart(fig, use_container_width=True)

def user_input_features():
    st.sidebar.header('User Input Features')
    default_company_name = 'ABBVIE LTD.'
    company_name = st.sidebar.text_input('Company Name', value=default_company_name)
    date_range = st.sidebar.slider('Select a date range', 2010, 2022, (2010, 2022))
    emission_type = st.sidebar.selectbox('Select emission type', ['CO2', 'CH4', 'N2O'])
    return company_name, date_range, emission_type

def display_metrics(data, emission_type):
    col1, col2, col3 = st.columns(3)
    total_emissions, max_emissions_year, max_emissions_value, avg_annual_increase = calculate_metrics(data, emission_type)
    with col1:
        st.metric(label="Total Emissions (Metric Tons)", value=f"{total_emissions:.2f} MT")
    with col2:
        st.metric(label="Year with Highest Emissions", value=f"{max_emissions_year}", delta=f"{max_emissions_value:.2f} MT")
    with col3:
        st.metric(label="Average Annual Increase in Emissions (Metric Tons)", value=f"{avg_annual_increase:.2f} MT")


