import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# 0. Preliminaries

# File Paths
file_path = r'H:/University of Allahabad/Data Science - Python/Pandas/CaseStudies/IndianStartupFunding/Data/processed_indian_startup_funding.csv'
investors_file_path = r'H:/University of Allahabad/Data Science - Python/Pandas/CaseStudies/IndianStartupFunding/Data/investors.csv'

# Page Configuration
st.set_page_config(
    page_title = 'Indian Startup Funding Analysis',
    layout = 'wide',
    initial_sidebar_state = 'expanded'
)

# CSS
st.markdown(
    body = """
            <style>
            [data-testid="stMetricValue"] {
                font-size: 20px;
            }
            </style>
            """,
    unsafe_allow_html=True,
)

# 1. Reading indian_startup_funding.csv file
startup_funding_df = pd.read_csv(
    filepath_or_buffer = file_path
)

investors_list = pd.read_csv(
    filepath_or_buffer = investors_file_path
)

# 2. Utility Functions


def load_investor_details(investor):
    
    # Callback function to update display
    def update_record_display():
        count = st.session_state.records_count
        selected_columns = st.session_state.selected_columns
        st.session_state.latest_investments = filtered_df[selected_columns].head(count)
        load_investor_details(investor)

    
    # Investor Mask
    inv_mask = startup_funding_df.Investors.str.lower().str.contains(investor, na=False)
    filtered_df = startup_funding_df[inv_mask]

    # Define all relevant columns
    columns_to_show = [
        'Date',
        'Startup',
        'Industry',
        'SubVertical',
        'Location',
        'Investors',
        'Round',
        'AmountInCrores',
        'URL'
    ]
    
    # Initialize session state if not set
    if 'investor' not in st.session_state:
        st.session_state.investor = investor
    else:
        if investor != st.session_state.investor:
            st.session_state.clear()
            st.session_state.investor = investor
    if 'records_count' not in st.session_state:
        st.session_state.records_count = 5
    if 'selected_columns' not in st.session_state:
        st.session_state.selected_columns = [
            'Date',
            'Startup',
            'Industry',
            'Round',
            'AmountInCrores'
        ]
    if 'latest_investments' not in st.session_state:
        st.session_state.latest_investments = filtered_df[st.session_state.selected_columns].head(st.session_state.records_count)
    
    
    
    # Display Code -----------------------------------------------
    
    # Setting Investor Name as Title 
    st.title(investor.title())
    
    # Recent Investments -----------------------------------------
    st.subheader('Recent Investments')
    
    # User input for columns to display
    st.multiselect(
        label = 'Select columns to display',
        options = columns_to_show,
        key = 'selected_columns',
        on_change = update_record_display
    )

    # User input for transaction count
    st.number_input(
        label = 'Transaction Count',
        min_value = 5,
        key = 'records_count',
        on_change = update_record_display
    )
        
    # Display recent investments dataframe
    st.dataframe(st.session_state.latest_investments)
    
    # Biggest Investments -----------------------------------------
    st.subheader('Biggest Investments')
    
    # User input for transaction count
    st.number_input(
        label = 'Startup Count',
        min_value = 5,
        key = 'startup_count',
        on_change = update_record_display
    )
    
    # Logic -----
    st.session_state.big_df = filtered_df.groupby(
        by = 'CleanedStartup'
    )['AmountInCrores'].sum().sort_values(
        ascending = False
    ).reset_index().rename(
            columns = {
                'CleanedStartup': 'Startup'
            }
    ).head(st.session_state.startup_count)
    
    # Display biggest investments dataframe
    st.dataframe(
        data = st.session_state.big_df
    )
    
    # Generally Invests In -------------------------------------
    st.subheader('Generally Invests In')
    
    # Logic
    ind = filtered_df.groupby(
        by = 'Industry'
    ).count()['Date'].sort_values(
        ascending = False
    )
    
    sub_vert = filtered_df.groupby(
        by = 'SubVertical'
    ).count()['Date'].sort_values(
        ascending = False
    )
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.metric(
            label = 'Industry',
            value = ind.head(1).index[0],
            border = True
        )
        
        # Sector Investments BAR Chart
        st.subheader('Investment Sector Graph')
        st.bar_chart(
            data = ind
        )
        
    with col2:
        st.metric(
            label = 'Sub Vertical',
            value = sub_vert.head(1).index[0],
            border = True
        )
        
        # Stage Investments BAR Chart
        rnd = filtered_df.groupby(
            by = 'Round'
        ).count()['Date']
        st.subheader('Investment Round Graph')
        st.bar_chart(
            data = rnd
        )
        
    # City Investments BAR Chart
    city = filtered_df.groupby(
        by = 'Location'
    ).count()['Date']
    
    st.subheader('Investment City Graph')
    st.bar_chart(
        data = city
    )
        
    # YearOnYear Investment Graph
    year_inv_data = filtered_df.groupby(
        by = 'Year'
    )['AmountInCrores'].sum()
    
    st.subheader('YearOnYear Investments')
    st.line_chart(
        data = year_inv_data
    )
    
    # Similar Investors
    sim_inv = set(filtered_df.InvestorsCleaned.apply(
        func = lambda x : eval(x)
    ).sum())
    
    
    
    
    



# 3. Creating the Sidebar of the Dashboard
with st.sidebar:
    st.title('Startup Menu')
    selected_option = st.selectbox(
        label = 'Select POV',
        options = [
            'General', 'Startup', 'Investor'
        ]
    )

# 4. Setting Main Page Title according to POV
if selected_option == 'General':
    st.title('General Analysis')
elif selected_option == 'Startup':
    st.title('Startup Analysis')
    selected_startup = st.selectbox(
        label = 'Choose Startup',
        options = startup_funding_df.StandardizedStartup.unique().tolist()
    )
    find_startup_btn = st.button(
        label = 'Find Startup Details',
        type = 'primary',
        use_container_width = True
    )
elif selected_option == 'Investor':
    selected_investor = st.sidebar.selectbox(
        label = 'Choose Investor',
        options = investors_list
    )
    find_investor_btn = st.sidebar.button(
        label = 'Find Investor Details',
        type = 'primary',
        use_container_width = True
    )
    if find_investor_btn:
        load_investor_details(selected_investor)
    