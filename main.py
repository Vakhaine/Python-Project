import streamlit as st
import plotly.express as px

st.title("Weather Forecast for the Next Days")

place = st.text_input("Place: ")

days = st.slider("Forcast Days", min_value=1, max_value=5,
                 help="Number of forecasted days")
option = st.selectbox("Select data to view",
                      ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")


def get_data(days):
    dates = ["1999-03-04", "1999-03-05", "1999-03-06"]
    temperatures = [10, 11, 50]
    temperatures = [days * i for i in temperatures]
    return dates, temperatures


d, t = get_data(days)
figure = px.line(x=d, y=t, labels={"x": "Dates", "y": "Temperature (C)"})

st.plotly_chart(figure)






