# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 08:30:32 2020

@author: Ryan
"""


import streamlit as st
import pandas as pd
#import pickle
import joblib
import datetime as dt

st.set_option('deprecation.showfileUploaderEncoding', False)

st.set_option('deprecation.showPyplotGlobalUse', False)


def main():
    model = joblib.load(open('taxiregressor.pkl', 'rb'))
    st.title('NYC Taxi Fare Predictor')
    passengers = st.selectbox('Number of passengers:', (1,2,3,4,5,6))
    distance = st.number_input('Enter trip distance:')
    payment = st.selectbox('Payment Type:', ('Cash', 'Credit'))
    pickup = st.selectbox('Pickup Borough:', ('Manhattan', 'Brooklyn','Queens','Bronx','Staten Island'))
    dropoff = st.selectbox('Dropoff Borough:', ('Manhattan', 'Brooklyn','Queens','Bronx','Staten Island'))
    weekday = st.selectbox('Day of the week:', ('Monday', 'Tuesday','Wednesday','Thursday','Friday','Saturday', 'Sunday'))
    temp = st.number_input('Enter temperature:')
    if weekday == 'Monday':
        weekday = 0
    elif weekday == 'Tuesday':
        weekday = 1
    elif weekday == 'Wednesday':
        weekday = 2
    elif weekday == 'Thursday':
        weekday = 3
    elif weekday == 'Friday':
        weekday = 4
    elif weekday == 'Saturday':
        weekday = 5
    elif weekday == 'Sunday':
        weekday = 6
    
    t = st.time_input('Time:', dt.time(15, 45))
    t = t.hour
    if st.button('Predict'):
        data = [{'passenger_count': passengers, 'trip_distance':distance, 'payment_type':payment,'TripStart_dayofweek': weekday, 'TripStart_hourofday': t,'PickupBorough': pickup, 'DropoffBorough': dropoff,'Avg Temp': temp}]
        result = model.predict(pd.DataFrame(data))
        result= str(result)

        st.write('The cost of your ride is estimated to be : ', result)


if __name__ == '__main__':
    main()
