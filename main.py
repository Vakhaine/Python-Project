import streamlit as st

import plotly_express as px
from backend import get_data

# Add title, text input, slider, and sub header

st.title("Weather Forecast For the Next 5 Days")

place = st.text_input("Place: ")

days = st.slider("Forecast Days",min_value=1, max_value=5,
                 help="Number of forecasted days")

option = st.selectbox("Select data to view",
                      ("Temperature", "Sky"))

st.subheader(f"{option} for the next {days} days in {place}")

if place:
    #  Get Temperature/Sky data

    filtered_data = get_data(place, days)

    if option == "Temperature":

        if filtered_data is None:  # Check if data retrieval failed

            st.error("Error: API request failed")

        else:

            nr_values = days or 1  # Handle cases where days is None

            temperatures = [item["main"]["temp"] for item in filtered_data]

            dates = [item["dt_txt"] for item in filtered_data]

            # Create Temperature plot

            figure = px.line(x=dates, y=temperatures,

                             labels={"x": "Date", "y": "Temperature (C)"})

            st.plotly_chart(figure)

    if option == "Sky":

        if filtered_data is None:  # Check if data retrieval failed

            st.error("Error: API request failed")

        else:

            sky_conditions = [item["weather"][0]["main"]
                              for item in filtered_data]
            images = {'Clouds': "images/cloud.png",
                      'Rain': "images/rain.png",
                      'Clear': "images/clear.png", 'Snow': "images/snow.png"}
            image_paths = [images[condition] for condition in sky_conditions]

            # Create sky plot

            st.image(image_paths, width=150)
