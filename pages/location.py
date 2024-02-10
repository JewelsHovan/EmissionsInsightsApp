import streamlit as st
from utils.utils_location import *

# show function
def show():
    st.title("Location-Based Emissions Analysis")

    # Load the data
    data = load_data('data/Processed_Unit.csv')

    # Extract unique states and cities for the dropdown
    states = data['State'].unique()
    cities = data['City'].unique()

    # Sort the unique values for better user experience
    states = sorted(states)
    cities = sorted(cities)

    st.sidebar.header("Filter Options")
    selected_state = st.sidebar.selectbox("State", states)

    # Filter data for selected state to get cities
    state_data = data[data['State'] == selected_state]
    cities = sorted(state_data['City'].unique())

    # Add an "All Cities" option to the cities list
    cities = ["All Cities"] + list(cities)

    if (selected_city := st.sidebar.selectbox("City", cities)) == "All Cities":
        # Filter data by state only
        filtered_data = state_data
    else:
        # Filter data by both state and city
        filtered_data = state_data[state_data['City'] == selected_city]

    if not filtered_data.empty:
        # Visualization 1 with caption on the right
        row1_col1, row1_col2 = st.columns([3, 1])
        with row1_col1:
            plot_co2_emissions_by_year(filtered_data)
        with row1_col2:
            st.markdown("## CO2 Emissions by Year")
            st.markdown("This chart shows the trend of CO2 emissions over the years for the selected location.")

        # Border after row 1
        st.markdown("<hr style='margin-top: 1rem; margin-bottom: 1rem; border-top: 1px solid #ccc;'>", unsafe_allow_html=True)

        # Visualization 2 with caption on the right
        row2_col1, row2_col2 = st.columns([3, 1])
        with row2_col1:
            plot_emissions_distribution(filtered_data)
        with row2_col2:
            st.markdown("## Emissions Distribution")
            st.markdown("This chart provides a distribution overview of emissions across different categories.")

        # Border after row 2
        st.markdown("<hr style='margin-top: 1rem; margin-bottom: 1rem; border-top: 1px solid #ccc;'>", unsafe_allow_html=True)

        # Visualization 3 with caption on the right
        row3_col1, row3_col2 = st.columns([3, 1])
        with row3_col1:
            plot_emissions_by_sector(filtered_data)
        with row3_col2:
            st.markdown("## Emissions by Sector")
            st.markdown("This visualization represents emissions divided by different sectors.")

        # Border after row 3
        st.markdown("<hr style='margin-top: 1rem; margin-bottom: 1rem; border-top: 1px solid #ccc;'>", unsafe_allow_html=True)

        # Visualization 4 with caption on the right
        row4_col1, row4_col2 = st.columns([3, 1])
        with row4_col1:
            plot_dynamic_scatter(filtered_data)
        with row4_col2:
            st.markdown("## Dynamic Scatter Plot")
            st.markdown("This scatter plot dynamically represents various emissions metrics.")

    else:
        st.write("No data available for the selected filters.")
