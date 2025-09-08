import streamlit as st

def calculate_taxi_fare(taxi_type, distance, waiting_time, baggage_count, animals, booking, toll):
    """
    Calculate the taxi fare in Hong Kong based on the distance traveled, waiting time, and additional charges.

    Args:
        taxi_type (str): Type of taxi ('Urban', 'New Territories', 'Lantau').
        distance (float): Distance traveled in kilometers.
        waiting_time (float): Waiting time in minutes.
        baggage_count (int): Number of baggage pieces.
        animals (bool): Whether animals are carried.
        booking (bool): Whether the taxi was booked via telephone.
        toll (float): Toll charges incurred.

    Returns:
        float: Total taxi fare in HKD.
    """
    # Fare details based on taxi type
    fare_details = {
        "Urban": {"initial_fare": 29.0, "fare_per_200m": 2.1, "fare_per_minute_waiting": 1.4, "threshold": 102.5, "reduced_fare": 1.4},
        "New Territories": {"initial_fare": 25.5, "fare_per_200m": 1.9, "fare_per_minute_waiting": 1.2, "threshold": 82.5, "reduced_fare": 1.4},
        "Lantau": {"initial_fare": 24.0, "fare_per_200m": 1.9, "fare_per_minute_waiting": 1.2, "threshold": 195.0, "reduced_fare": 1.6},
    }

    details = fare_details[taxi_type]

    # Calculate the fare for distance traveled
    if distance <= 2:
        distance_fare = details["initial_fare"]
    else:
        extra_distance = distance - 2
        if details["initial_fare"] + (extra_distance * 1000 / 200) * details["fare_per_200m"] <= details["threshold"]:
            distance_fare = details["initial_fare"] + (extra_distance * 1000 / 200) * details["fare_per_200m"]
        else:
            distance_fare = details["threshold"] + ((extra_distance * 1000 / 200) - (details["threshold"] / details["fare_per_200m"])) * details["reduced_fare"]

    # Calculate the fare for waiting time
    waiting_fare = waiting_time * details["fare_per_minute_waiting"]

    # Additional charges
    baggage_fare = baggage_count * 6
    animal_fare = 5 if animals else 0
    booking_fare = 5 if booking else 0

    # Total fare
    total_fare = distance_fare + waiting_fare + baggage_fare + animal_fare + booking_fare + toll

    return round(total_fare, 2)

# Streamlit app
st.title("Hong Kong Taxi Fare Calculator")

st.sidebar.header("Input Parameters")
taxi_type = st.sidebar.selectbox("Taxi Type:", ["Urban", "New Territories", "Lantau"])
distance = st.sidebar.number_input("Distance traveled (km):", min_value=0.0, step=0.1)
waiting_time = st.sidebar.number_input("Waiting time (minutes):", min_value=0.0, step=0.1)
baggage_count = st.sidebar.number_input("Number of baggage pieces:", min_value=0, step=1)
animals = st.sidebar.checkbox("Are animals carried?")
booking = st.sidebar.checkbox("Was the taxi booked via telephone?")
toll = st.sidebar.number_input("Toll charges (HKD):", min_value=0.0, step=0.1)

if st.sidebar.button("Calculate Fare"):
    fare = calculate_taxi_fare(taxi_type, distance, waiting_time, baggage_count, animals, booking, toll)
    st.write(f"### Total Taxi Fare: HKD {fare}")
