# Import required libraries
import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

# Create a navigation sidebar
nav = st.sidebar.radio("Navigation",["About","Predict"])

# Load the insurance dataset
df = pd.read_csv('insurance.csv')

# If 'About' is selected in the navigation sidebar
if nav=="About":
    # Display the title of the app
    st.title("Health Insurance Premium Predictor")
    # Add two blank lines for spacing
    st.text(" ")
    st.text(" ")
    # Display an image
    st.image('health_insurance.jpeg',width=600)
    

# Replace 'male' with 0 and 'female' with 1 in the 'sex' column of the dataset
df.replace({'sex':{'male':0,'female':1}},inplace=True)

# Replace 'yes' with 0 and 'no' with 1 in the 'smoker' column of the dataset
df.replace({'smoker':{'yes':0,'no':1}},inplace=True)

# Replace 'southeast' with 0, 'southwest' with 1, 'northeast' with 2, and 'northwest' with 3 in the 'region' column of the dataset
df.replace({'region':{'southeast':0,'southwest':1,'northeast':2,'northwest':3}},inplace=True)

# Split the dataset into features and target variable
x = df.drop(columns='charges',axis=1)
y = df['charges']

# Create a Random Forest Regressor model
rfr = RandomForestRegressor()

# Train the model on the dataset
rfr.fit(x,y)

# If 'Predict' is selected in the navigation sidebar
if nav=="Predict":
    # Display the title of the prediction page
    st.title("Enter Details")

    # Create input fields for user to enter details for prediction
    age = st.number_input("Age: ",step=1,min_value=0)
    sex = st.radio("Sex",("Male","Female"))
    bmi = st.number_input("BMI: ",min_value=0)
    children = st.number_input("Number of children: ",step=1,min_value=0)
    smoke = st.radio("Do you smoke",("Yes","No"))
    region = st.selectbox('Region',('SouthEast','SouthWest','NorthEast','NorthWest'))

    # Convert categorical input fields to numeric values using if-else statements
    if (sex == "Male"):
        s=0
    if (sex == "Female"):
        s=1
    if (smoke=="Yes"):
        sm = 0
    if (smoke == "No"):
        sm = 1
    if (region == "SouthEast"):
        reg = 0
    if (region == "SouthWest"):
        reg = 1
    if (region == "NorthEast"):
        reg = 2
    if (region == "NorthWest"):
        reg = 3

    # If 'Predict' button is clicked
    if st.button("Predict"):
        # Display a subheader and the predicted premium
        st.subheader("Predicted Premium")
        st.text(rfr.predict([[age,s,bmi,children,sm,reg]]))
