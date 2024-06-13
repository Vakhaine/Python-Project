import streamlit as st

import plotly_express as px
from backend import get_data

# Add title, text input, slider, and sub header

st.title("Weather Forecast For the Next 5 Days In Your City 😊")

place = st.text_input("Place: ")

days = st.slider("Forecast Days",min_value=1, max_value=5,
                 help="Number of forecasted days")

option = st.selectbox("Select data to view",
                      ("Temperature", "Humidity", "Weather Condition",
                       "Cloud Cover", "Wind Speed"))

st.subheader(f"{option} for {days} day(s) forecast in {place}")

if place:
    try:
        #  Get Temperature/Weather data/ Humidity/ Cloud Cover/ Wind Speed

        filtered_data = get_data(place, days)

        if filtered_data is None:
            st.write("That place does not exist. Try again!")
        else:

            if option == "Temperature":
                nr_values = days or 1  # Handle cases where days is None

                temperatures = [item["main"]["temp"]/10 for item in filtered_data]
                dates = [item["dt_txt"] for item in filtered_data]

                # Create Temperature plot

                figure = px.line(x=dates, y=temperatures,
                                 labels={"x": "Time", "y": "Temperature (C)"})

                st.plotly_chart(figure)

            if option == "Weather Condition":

                sky_conditions = [item["weather"][0]["main"]
                                  for item in filtered_data]
                images = {'Clouds': "images/cloud.png",
                          'Rain': "images/rain.png",
                          'Clear': "images/clear.png", 'Snow': "images/snow.png"}
                image_paths = [images[condition] for condition in sky_conditions]

                # Create sky plot

                st.image(image_paths, width=150)

            if option == "Humidity":

                humidities = [item["main"]["humidity"] for item in filtered_data]

                dates = [item["dt_txt"] for item in filtered_data]

                # Create Humidity plot

                figure = px.line(x=dates, y=humidities,
                                 labels={"x": "Time", "y": "Humidity (%)"})

                st.plotly_chart(figure)

            if option == "Cloud Cover":

                # Extract the dates and cloud cover values from the data
                dates = [item["dt_txt"] for item in filtered_data]
                cloud_covers = [item["clouds"]["all"] for item in filtered_data]

                # Create the line plot
                fig = px.line(x=dates, y=cloud_covers, title='Cloud Cover Over Time')

                # Customize the plot
                fig.update_layout(
                    xaxis_title='Time',
                    yaxis_title='Cloud Cover (%)'
                )

                # Show the plot
                st.plotly_chart(fig)

            if option == "Wind Speed":
                dates = [item["dt_txt"] for item in filtered_data]
                wind_speeds = [item["wind"]["speed"] for item in filtered_data]

                fig_wind_speed = px.line(x=dates, y=wind_speeds)
                fig_wind_speed.update_layout(
                    xaxis_title='Date',
                    yaxis_title='Wind Speed (m/s)'
                )
                st.plotly_chart(fig_wind_speed)
    except KeyError:
        st.write("Data not found, Try again!")