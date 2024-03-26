# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
import pandas as pd
import altair as alt
import plotly.express as px


def load_data(file_name):
    data = pd.read_csv(file_name)
    return data

def filter_data(data, company_name, date_range, emission_type):
    if company_name:
        data = data[data['Facility.Name'].str.contains(company_name, case=False, na=False)]
    data = data[(data['Year'] >= date_range[0]) & (data['Year'] <= date_range[1])]
    emission_col = f'{emission_type}_emissions'
    filtered_data = data[['Facility.Name', 'Sector', 'Year', emission_col]]
    return data, filtered_data

def pivot_data(filtered_data, emission_type):
    emission_col = f'{emission_type}_emissions'
    pivoted_data = filtered_data.pivot_table(index=['Facility.Name', 'Sector'], 
                                             columns='Year', 
                                             values=emission_col, 
                                             fill_value=0)
    return pivoted_data

def calculate_sector_data(data, all_data, company_name, emission_type):
    selected_company_sector = data.loc[data['Facility.Name'].str.contains(company_name, case=False, na=False), 'Sector'].iloc[0]
    sector_data = all_data[all_data['Sector'] == selected_company_sector]
    emission_col = f'{emission_type}_emissions'
    total_emissions_by_company = sector_data.groupby('Facility.Name')[emission_col].sum().sort_values(ascending=False)
    selected_company_emissions = total_emissions_by_company[total_emissions_by_company.index.str.contains(company_name, case=False)]
    if selected_company_emissions.empty:
        top_companies = total_emissions_by_company.head(10)
    else:
        top_companies = pd.concat([total_emissions_by_company.head(10), selected_company_emissions]).drop_duplicates()
    top_companies_df = top_companies.reset_index()
    top_companies_df.columns = ['Facility.Name', emission_col]
    top_companies_df['Highlight'] = top_companies_df['Facility.Name'].apply(lambda x: 'Selected Company' if x == company_name else 'Other Companies')
    return top_companies_df

def calculate_metrics(data, emission_type):
    emission_col = f'{emission_type}_emissions'
    total_emissions = data[emission_col].sum()
    max_emissions_year = data.loc[data[emission_col].idxmax(), 'Year']
    max_emissions_value = data[emission_col].max()
    avg_annual_increase = data[emission_col].diff().mean()
    return total_emissions, max_emissions_year, max_emissions_value, avg_annual_increase

def generate_line_chart(data, emission_type):
    emission_col = f'{emission_type}_emissions'
    emission_data = data.groupby('Year').agg({emission_col: 'sum'}).reset_index()

    # Customizing the line chart
    line_chart = alt.Chart(emission_data).mark_line(point=True).encode(
        x=alt.X('Year:O', axis=alt.Axis(title='Year', labelAngle=-45)),  # Orienting year labels for better readability
        y=alt.Y(f'{emission_col}:Q', axis=alt.Axis(title='Emissions (Metric Tons)')),  # Adding units to the y-axis title
        tooltip=[alt.Tooltip('Year:O', title='Year'), alt.Tooltip(f'{emission_col}:Q', title='Emissions (Metric Tons)')],  # Adding units to the tooltip
        color=alt.value('steelblue'),  # Setting a consistent color for the line
    ).properties(
        title=f'Annual {emission_type} Emissions Over Time',
        width=600,  # Adjusting the width for better visibility
        height=400  # Adjusting the height for better visibility
    ).configure_axis(
        grid=False  # Removing the grid for a cleaner look
    ).configure_view(
        strokeWidth=0  # Removing the border around the chart
    )

    return line_chart


def generate_bar_chart(top_companies_df, emission_type, company_name):
    emission_col = f'{emission_type}_emissions'
    fig = px.bar(top_companies_df, x='Facility.Name', y=emission_col,
                 color='Highlight', color_discrete_map={'Selected Company': 'orange', 'Other Companies': 'steelblue'},
                 labels={emission_col: 'Emissions', 'Facility.Name': 'Company'},
                 title=f'Top Companies {emission_type} Emissions Comparison in Sector')
    fig.update_layout(xaxis_title="Company", yaxis_title="Emissions", xaxis={'categoryorder':'total descending'})
    fig.update_xaxes(tickangle=45)
    return fig


def calculate_average_emissions(data, sector_data, company_name, emission_type, date_range):
    emission_col = f'{emission_type}_emissions'

    # Calculate average emissions for the selected company over the selected year range
    company_avg_emissions = data[(data['Facility.Name'].str.contains(company_name, case=False, na=False)) &
                                 (data['Year'] >= date_range[0]) & (data['Year'] <= date_range[1])][emission_col].mean()

    # Calculate sector average emissions over the selected year range
    sector_avg_emissions = sector_data[(sector_data['Year'] >= date_range[0]) & (sector_data['Year'] <= date_range[1])][emission_col].mean()

    return company_avg_emissions, sector_avg_emissions
