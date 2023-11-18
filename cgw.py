import streamlit as st
import pandas as pd
import numpy as np
st.title("차건우")

tab1, tab2, tab3 = st.tabs(["Home", "About me", "Projects"])

with tab1:
   st.header("Titanic Dataset", divider='gray')
   st.image("https://static.streamlit.io/examples/titanic.jpeg", width=200)
   tab1, tab2, tab3 = st.tabs(["Sex", "Pclass", "Embarked"])
   with tab1:
      st.bar_chart(t, x="Sex", y="Survived" )
with tab2:
   st.header("A dog")
   st.image("https://static.streamlit.io/examples/dog.jpg", width=200)

with tab3:
   st.header("An owl")
   st.image("https://static.streamlit.io/examples/owl.jpg", width=200)

t = pd.read_csv("train.csv")

st.dataframe(t)

st.header('Survival Rate', divider='gray')
