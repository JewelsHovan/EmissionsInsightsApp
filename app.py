import streamlit as st
from pages import company, location  # Importing your page modules


st.set_page_config(page_title="Eco Emissions Insights", page_icon="🌿", layout="wide")
st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to", ['Home', 'Company Insights', 'Location Insights'])


def main():
    # Introduction text
    st.title("Emissions Insights App")
    
    st.markdown("""
        ## Empowering you to make a difference
        
        Discover the environmental footprint of your community with real-time, data-driven insights into local emissions.
        Stay informed about your local climate policies and how your representatives are addressing climate change, 
        empowering you to align with values that matter.
        
        Navigate through complex emissions data with ease, thanks to our user-friendly visualizations, making it simple 
        to understand the impact in your area, like San Francisco, California.
        
        ### Key Features:
        
        - **Stay Updated:** With the latest on climate policies and lawmakers' perspectives with our advanced LLM 
          technology, designed for seamless real-time information retrieval.
        - **Access Data:** Access to the latest emissions data by sector and company within your community, utilizing 
          the EPA's comprehensive dataset for accuracy and detail.
        - **Engaging Visualizations:** Engage with innovative visualizations that bring clarity to emissions data, 
          allowing you to explore the specifics of any chosen location, from your city to your neighborhood.
                
        ### Pages Overview

        - **Company Insights**: This page allows you to filter and search by company to see visualizations and obtain detailed information. Explore emissions data specific to companies, analyze their environmental impact, and gain insights into their sustainability practices.

        - **Location Insights**: On this page, you can filter by state and/or city to view graphics and detailed analyses related to the location's emissions. It's designed to help you understand the local environmental footprint, giving you the power to compare and contrast different regions.

    """)

if selection == 'Home':
    main()
elif selection == 'Company Insights':
    company.show()  # Assuming each page module has a show function
elif selection == 'Location Insights':
    location.show()



    

