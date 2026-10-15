#streamlit UI
import pickle
import pandas as pd
import streamlit as st

#page setup
st.set_page_config(page_title="Customer Spending Prediction",
                   page_icon=r"C:\Users\DELL\Desktop\Customer spending Prediction\assets\logo.jpg")


#sidebar
with st.sidebar:
    st.title("Customer Spending Prediction")
    st.image(r"C:\Users\DELL\Desktop\Customer spending Prediction\assets\logo.jpg")


#load the model (model deserialization)
with open(r"C:\Users\DELL\Desktop\Customer spending Prediction\best_model\best_model_pipeline.pkl","rb") as file:
    best_pipeline = pickle.load(file)


#load the dataset
df = pd.read_csv(r"C:\Users\DELL\Desktop\Customer spending Prediction\dataset\cleaned_data.csv")

#user input
col1,col2=st.columns(2,border=True)
with col1:
    Age=st.number_input('Age:',min_value=1,max_value=100)
    Annual_Income=st.number_input('Annual Income:',min_value=100000)
    Website_Visits=st.number_input('Website Visits:',min_value=1)
    Previous_Purchases=st.number_input('Previous Purchases:',min_value=1)
with col2:
    Membership_Type=st.selectbox('Membership :',options=df['Membership_Type'].unique())
    Preferred_Category=st.selectbox('Preffered Catagory:',options=df['Preferred_Category'].unique())
    City_Tier=st.selectbox('City Tier :',options=df['City_Tier'].unique())
    Discount_Used=st.selectbox('Discount Used :',options=df['Discount_Used'].unique())

#new data
new_data={'Age':Age, 'Annual_Income':Annual_Income, 'Website_Visits':Website_Visits, 'Previous_Purchases':Previous_Purchases,
       'Membership_Type':Membership_Type, 'Preferred_Category':Preferred_Category, 'City_Tier':City_Tier, 'Discount_Used':Discount_Used}


new_data=pd.DataFrame(new_data)[0]

if st.button('Predict spend'):
    prediction=best_pipeline.predict(new_data)[0]
    st.success(f'Predict Spend:{prediction[0]:.2f}Rs.')