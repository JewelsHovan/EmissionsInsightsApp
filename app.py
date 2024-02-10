import streamlit as st
from pages import company, location  # Importing your page modules
from utils.utils_home import *

# Set page configuration
st.set_page_config(page_title="Eco Emissions Insights", page_icon="🌿", layout="wide")

# Sidebar navigation
st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to", ['Home', 'Company Insights', 'Location Insights'])

# Main page content
def main():
    data = load_data('data/Processed_Unit.csv')

    # Introduction section
    st.header("Empowering you to make a difference ✨")
    st.markdown("""
        Discover the environmental footprint of your community with real-time, data-driven insights into local emissions.
        Stay informed about your local climate policies and how your representatives are addressing climate change, 
        empowering you to align with values that matter 🌱.
    """)
    
    st.subheader("Navigate through complex emissions data with ease 🌉")
    st.markdown("Making it simple to understand the impact in your area")

    # Visualizations in a grid layout
    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            top_sectors_chart = create_top_sectors_pie_chart(data)
            st.plotly_chart(top_sectors_chart, use_container_width=True)
        with col2:
            emissions_trend_chart = create_emissions_trend_chart(data)
            st.plotly_chart(emissions_trend_chart, use_container_width=True)

        col3, col4 = st.columns(2)
        with col3:
            state_wise_emissions_map = create_state_wise_emissions_map(data)
            st.plotly_chart(state_wise_emissions_map, use_container_width=True)
        with col4:
            top_emitters_bar_chart = create_top_emitters_bar_chart(data)
            st.plotly_chart(top_emitters_bar_chart, use_container_width=True)

    # Key Features section
    st.header("Key Features:")
    st.markdown("""
        - **Stay Updated 📈:** With the latest on climate policies and lawmakers' perspectives with our advanced LLM 
          technology, designed for seamless real-time information retrieval.
        - **Access Data 🔍:** Access to the latest emissions data by sector and company within your community, utilizing 
          the EPA's comprehensive dataset for accuracy and detail.
        - **Engaging Visualizations 📊:** Engage with innovative visualizations that bring clarity to emissions data, 
          allowing you to explore the specifics of any chosen location, from your city to your neighborhood.
    """)

    # Pages Overview section
    st.header("Pages Overview")
    with st.expander("Company Insights 🏢"):
        st.markdown("""
            This page allows you to filter and search by company to see visualizations and obtain detailed information. 
            Explore emissions data specific to companies, analyze their environmental impact, and gain insights into 
            their sustainability practices.
        """)

    with st.expander("Location Insights 📍"):
        st.markdown("""
            On this page, you can filter by state and/or city to view graphics and detailed analyses related to the 
            location's emissions. It's designed to help you understand the local environmental footprint, giving you 
            the power to compare and contrast different regions.
        """)

    

# Routing logic
if selection == 'Home':
    main()
elif selection == 'Company Insights':
    company.show()  # Assuming each page module has a show function
elif selection == 'Location Insights':
    location.show()
