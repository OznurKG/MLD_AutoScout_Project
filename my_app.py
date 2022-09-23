
import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
#from sklearn.linear_model import Lasso
#from sklearn.compose import make_column_transformer
#from sklearn.preprocessing import OneHotEncoder, MinMaxScaler
#from sklearn.pipeline import Pipeline
import pickle

#st.title("Car Price Prediction Web App")
st.markdown("<h2 style='text-align:center; color:Black;'>Car Price Prediction</h2>", unsafe_allow_html=True)
#image
img = Image.open("car-price-hike.jpg")
col1, col2, col3 = st.columns([0.2,6,0.2]) 
with col2:
    st.image(img,caption="Get Car Price Predictions from the model",width = 600)

#dataframe
df=pd.read_csv("final_scout_not_dummy.csv")

st.error("Please select the filters on the sidebar in order to see the prediction ")

#button
if st.button("Data"):
    st.write(df[["make_model", "Gearing_Type", "age","hp_kW","km","Gears"]].sample(10))

model = pickle.load(open("final_model_autoscout", "rb"))

def user_input_features() :
        make_model = st.sidebar.selectbox("Make_Model", ("Audi A3","Audi A1","Opel Insignia", "Opel Astra", "Opel Corsa", "Renault Clio", "Renault Espace", "Renault Duster"))
        Gearing_Type = st.sidebar.selectbox("Gearing_Type", ("Manual","Automatic", "Semi-automatic"))
        age = st.sidebar.number_input("Age:",min_value=0, max_value=3)
        # age = st.sidebar.selectbox("age", ("0","1", "2", "3"))
        # Gears = st.sidebar.slider("Gears", 5.0, 8.0, 5.0)
        Gears = st.sidebar.radio("Gears",(5,6,7,8))
        hp_kW = st.sidebar.slider("Horse_Power(kW)", df["hp_kW"].min(), df["hp_kW"].max(), float(df["hp_kW"].median()),1.0)
        km = st.sidebar.slider("Kilometers(km)", df["km"].min(), df["km"].max(), float(df["km"].median()),1.0)
    
        data = {"make_model" : make_model,
            "Gearing_Type" : Gearing_Type,
            "age" : age,
            "hp_kW" : hp_kW,
            "km" : km,
            "Gears" : Gears}
        features = pd.DataFrame(data, index=[0])
        return features

input_df = user_input_features()


st.markdown("---")
# buton
if st.button('Get Prediction'):
    st.success(f'Your search results:&emsp;${model.predict(input_df)[0].round()}')


st.markdown("---")