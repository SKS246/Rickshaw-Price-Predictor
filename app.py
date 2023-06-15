import streamlit as st
import math


def main():
    st.set_page_config(page_title='Rickshaw Price Predictor',
                       page_icon='🛺', layout='wide')
    st.subheader("Rickshaw Price Predictor")
    st.write("This is your go-to website for checking approximate auto rickshaw prices based on several factors for the 2 popular meter-only rickshaw cities. Auto rickshaws are a popular and reliable mean of transport for hunreds of thousands of people, knowing the fare of the ride beforehand can turn out to be very helpful.")

    st.write("---")

    left, right = st.columns(2)
    with left:
        st.subheader("Delhi")
        delhi_distance = st.number_input(
            "Enter an estimate of the distance of the journey (KMs):", min_value=1.0, max_value=1000.0, step=1.0)
        st.write(f"You entered: {delhi_distance} KMs")
        st.write("#")
        delhi_night = st.checkbox(
            "Night Trip (Between 11PM and 5AM)", value=False)
        st.write(f"Night trip: {delhi_night}")
        st.write("#")
        delhi_luggage = st.slider(
            "Luggage (Not including shopping bag or small suitcases): ", min_value=0, max_value=10, step=1)
        st.write(f"Luggage bags: {delhi_luggage}")
        st.write("#")
        delhi_wait = st.slider("Estimated Waiting Time: ",
                               min_value=0, max_value=120, step=1)
        st.write(f"Estimated Waiting Time: {delhi_wait}")
        st.write("#")
        st.write("You will be charged 75 paise for every minute of wait, hence the price is just an approximate, therefore, it is recommeneded to carry about ₹10-15 extra if your estimated waiting time is too low.")

        if delhi_distance > 1.5:
            price = 30 + (11*(delhi_distance - 1.5))
        else:
            price = 30
        if delhi_night:
            price *= 1.25
        price += delhi_luggage*10
        price += delhi_wait*0.75
        st.subheader(f"Final Price: ₹{math.ceil(price)}")

    with right:
        st.subheader("Mumbai")

        mumbai_distance = st.number_input(
            "Enter an estimate of the distance of the journey (KMs):", min_value=1.0, max_value=1000.0, step=1.0, key="mumbai_distance")
        st.write(f"You entered: {mumbai_distance} KMs")
        st.write("#")
        mumbai_night = st.checkbox(
            "Night Trip (Between 11PM and 5AM)", value=False, key="mumbai_night")
        st.write(f"Night trip: {mumbai_night}")
        st.write("#")
        mumbai_wait = st.slider("Estimated Waiting Time: ",
                                min_value=0, max_value=120, step=1, key="mumbai_wait")
        st.write(f"Estimated Waiting Time: {mumbai_wait}")
        st.write("#")
        st.write("You will be charged ₹1.42 for every minute of wait, hence the price is just an approximate, therefore, it is recommeneded to carry about ₹10-20 extra if your estimated waiting time is too low.")

        if mumbai_distance > 1.5:
            mumbai_price = 23 + (15.33*(mumbai_distance - 1.5))
        else:
            mumbai_price = 23
        if mumbai_night:
            mumbai_price *= 1.25
        mumbai_price += mumbai_wait*1.42
        st.subheader(f"Final Price: ₹{math.ceil(mumbai_price)}")


if __name__ == '__main__':
    main()
