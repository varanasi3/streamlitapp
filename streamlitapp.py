import streamlit as st
import pandas as pd
import joblib


# Function to preprocess input data
def preprocess_input(input_data):
    # Preprocess input data as needed, e.g., scaling, encoding, etc.
    processed_data = input_data
    return processed_data

# Load model and other necessary files
model = joblib.load('xgboost_model.joblib')

# Replace this with your model loading and any other necessary files

# Main function to run the app
def main():
    st.title('Insurance Claim Prediction App')

    # Input fields
    col1, col2, col3 ,col4 = st.columns(4)
    with col1:
        st.subheader('General information')
        exposure = st.number_input("Exposure", min_value=0.0)
        veh_power = st.number_input("Vehicle Power", min_value=0)
        veh_age = st.number_input("Vehicle Age", min_value=0)
        driv_age = st.number_input("Driver Age", min_value=18)
        bonus_malus = st.number_input("Bonus/Malus", min_value=0)
        density = st.number_input("Density", min_value=0)
        claim_total = st.number_input('Claim Total', min_value=0, value=0)
          # Area options
        st.subheader('Area')
        area_a = st.number_input('Area A', min_value=0, max_value=1, value=0)
        area_b = st.number_input('Area B', min_value=0, max_value=1, value=0)
        area_c = st.number_input('Area C', min_value=0, max_value=1, value=0)
        area_d = st.number_input('Area D', min_value=0, max_value=1, value=0)
        area_e = st.number_input('Area E', min_value=0, max_value=1, value=0)
        area_f = st.number_input('Area F', min_value=0, max_value=1, value=0)

        

    with col2:

      


        # Vehicle gas options
        st.subheader('Vehicle Gas')
        veh_gas_diesel = st.number_input('Diesel', min_value=0, max_value=1, value=0)
        veh_gas_regular = st.number_input('Regular', min_value=0, max_value=1, value=0)
        
        # Vehicle brand options
        st.subheader('Vehicle Brands')
        veh_brand_b1 = st.number_input('B1', min_value=0, max_value=1, value=0)
        veh_brand_b10 = st.number_input('B10', min_value=0, max_value=1, value=0)
        veh_brand_b11 = st.number_input('B11', min_value=0, max_value=1, value=0)
        veh_brand_b12 = st.number_input('B12', min_value=0, max_value=1, value=0)
        veh_brand_b13 = st.number_input('B13', min_value=0, max_value=1, value=0)
        veh_brand_b14 = st.number_input('B14', min_value=0, max_value=1, value=0)
        veh_brand_b2 = st.number_input('B2', min_value=0, max_value=1, value=0)
        veh_brand_b3 = st.number_input('B3', min_value=0, max_value=1, value=0)
        veh_brand_b4 = st.number_input('B4', min_value=0, max_value=1, value=0)
        veh_brand_b5 = st.number_input('B5', min_value=0, max_value=1, value=0)
        veh_brand_b6 = st.number_input('B6', min_value=0, max_value=1, value=0)

        
        
    with col3:

        
        

        st.subheader('Region')
        region_r11 = st.number_input('R11', min_value=0, max_value=1, value=0)
        region_r21 = st.number_input('R21', min_value=0, max_value=1, value=0)
        region_r22 = st.number_input('R22', min_value=0, max_value=1, value=0)
        # Region options
        region_r23 = st.number_input('R23', min_value=0, max_value=1, value=0)
        region_r24 = st.number_input('R24', min_value=0, max_value=1, value=0)

        region_r25 = st.number_input('R25', min_value=0, max_value=1, value=0)
        region_r26 = st.number_input('R26', min_value=0, max_value=1, value=0)
        region_r31 = st.number_input('R31', min_value=0, max_value=1, value=0)
        region_r41 = st.number_input('R41', min_value=0, max_value=1, value=0)
        region_r42 = st.number_input('R42', min_value=0, max_value=1, value=0)
        region_r43 = st.number_input('R43', min_value=0, max_value=1, value=0)
        region_r52 = st.number_input('R52', min_value=0, max_value=1, value=0)

        region_r53 = st.number_input('R53', min_value=0, max_value=1, value=0)
        region_r54 = st.number_input('R54', min_value=0, max_value=1, value=0)
        
    with col4:  
        
        region_r72 = st.number_input('R72', min_value=0, max_value=1, value=0)
        region_r73 = st.number_input('R73', min_value=0, max_value=1, value=0)
        region_r74 = st.number_input('R74', min_value=0, max_value=1, value=0)
        region_r82 = st.number_input('R82', min_value=0, max_value=1, value=0)
        region_r83 = st.number_input('R83', min_value=0, max_value=1, value=0)
        region_r91 = st.number_input('R91', min_value=0, max_value=1, value=0)
        region_r93 = st.number_input('R93', min_value=0, max_value=1, value=0)
        region_r94 = st.number_input('R94', min_value=0, max_value=1, value=0)
    # Button to make predictions
    if st.button('Predict'):
        input_data = {
            'Exposure': exposure,
            'VehPower': veh_power,
            'VehAge': veh_age,
            'DrivAge': driv_age,
            'BonusMalus': bonus_malus,
            'Density': density,
            'ClaimTotal': claim_total,
            'Area_A': area_a,
            'Area_B': area_b,
            'Area_C': area_c,
            'Area_D': area_d,
            'Area_E': area_e,
            'Area_F': area_f,
            'VehBrand_B1': veh_brand_b1,
            'VehBrand_B10': veh_brand_b10,
            'VehBrand_B11': veh_brand_b11,
            'VehBrand_B12': veh_brand_b12,
            'VehBrand_B13': veh_brand_b13,
            'VehBrand_B14': veh_brand_b14,
            'VehBrand_B2': veh_brand_b2,
            'VehBrand_B3': veh_brand_b3,
            'VehBrand_B4': veh_brand_b4,
            'VehBrand_B5': veh_brand_b5,
            'VehBrand_B6': veh_brand_b6,
            'VehGas_Diesel': veh_gas_diesel,
            'VehGas_Regular': veh_gas_regular,
            'Region_R11': region_r11,
            'Region_R21': region_r21,
            'Region_R22': region_r22,
            'Region_R23': region_r23,
            'Region_R24': region_r24,
            'Region_R25': region_r25,
            'Region_R26': region_r26,
            'Region_R31': region_r31,
            'Region_R41': region_r41,
            'Region_R42': region_r42,
            'Region_R43': region_r43,
            'Region_R52': region_r52,
            'Region_R53': region_r53,
            'Region_R54': region_r54,
            'Region_R72': region_r72,
            'Region_R73': region_r73,
            'Region_R74': region_r74,
            'Region_R82': region_r82,
            'Region_R83': region_r83,
            'Region_R91': region_r91,
            'Region_R93': region_r93,
            'Region_R94': region_r94
        }

        # Preprocess input data
        processed_input = preprocess_input(input_data)

        # Check if ClaimTotal is zero, if yes, set prediction to zero
        if claim_total == 0:
            prediction = 0
        else:
            # Make prediction using the loaded model
            prediction = model.predict(pd.DataFrame.from_dict(processed_input, orient='index').T)[0]

        # Display prediction
        st.success(f'The predicted claim count is: {prediction}')

# Run the app
if __name__ == '__main__':
    main()
