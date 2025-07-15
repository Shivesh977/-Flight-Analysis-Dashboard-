import streamlit  as st 
import plotly.express as px
import pandas as pd
# WE HAVE A SEPERATE FILE FOR DATABASE RELATAD QUERY TO EXTRACT DATA FROM SQL 
# THAT FILE IS DATABASE_HELPER

from database_helper import DB
db=DB() # it can access database class methods


# making a side_bar 
st.sidebar.title('Flights Analysis')

user_option=st.sidebar.selectbox('Menu',['Select one','Check Flights' , 'Analytics']) 

if user_option=='Check Flights' :
    st.title('Check Flights')
    
    col1,col2=st.columns(2)
    
    city = db.fetch_city_name()
    
    with col1:
       source= st.selectbox('Source',sorted(city))
       
    with col2:
        destination =st.selectbox('Destination',sorted(city))
        
    if st.button('Search'):
       results = db.fetch_all_flights(source, destination)
       if len(results) == 0:
            st.markdown("Data not available, check for Bangalore to Delhi flights")
       else:
            st.dataframe(results)


    
    
elif user_option=='Analytics':
    st.title('Analytics')
    
    col1,col2=st.columns(2)
    
    with col1:
        airline, frequency = db.airline_frequence()
        # Create a dictionary from the data
        data = {"Airline": airline, "Frequency": frequency}

        # Generate a Plotly pie chart
        fig = px.pie(
            names=data["Airline"],
            values=data["Frequency"],
            title="Flight Frequency by Airline",
            hole=0.3  # Optional: makes it a donut chart
        )

        # Display the pie chart in Streamlit
        # st.title("Airline Frequency Pie Chart")
        st.plotly_chart(fig)
    
    with col2: # generating a bar chart showing bussiest airport 
        
            # Get data
        City, frequency = db.bussiest_airport()

        # Create DataFrame
        df = pd.DataFrame({'City': City, 'Frequency': frequency})

        # Plot
        fig = px.bar(df, x='City', y='Frequency', title='Busiest Airports by City', color='City')

        # Display
        st.plotly_chart(fig)
        
        
    Airline,price=db.average_price()
    df = pd.DataFrame({'Airline': Airline, 'Average_price': price})
    fig = px.bar(df, x='Airline', y='Average_price', title='Average Price of Airlines ', color='Airline')
    st.plotly_chart(fig)
    
    
        
            
    
else :
    st.title('Tell about the project')
    st.markdown("""
    # ✈️ Flight Data Analysis Dashboard

    Welcome to the Flight Data Analysis Dashboard!  
    This interactive web application provides deep insights into flight information including airline names, source and destination cities, prices, routes, and more.  
    Using Streamlit and real-world flight datasets, this dashboard helps identify key patterns such as:

    - The **busiest airports** based on flight traffic  
    - Popular **routes** between cities  
    - Comparative **airline frequency and pricing trends**  
    - Source and destination city analysis  

    Whether you're a data enthusiast, a traveler, or just curious about aviation trends, this tool offers a visual and statistical exploration of flight dynamics.
    """)
