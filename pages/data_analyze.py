import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import time

def write():
    st.title("Data Analysis :door:")
    st.write("\n")
    st.write("\n")
    st.markdown(
           """### Let's explore the dataframe with us
            The dataset is based on the 13 users who collected the data during their daily activities. The dataset includes all sensors available in phones and distinguishes five transportation modes: 
                / being on a car
                / on a bus
                / on a train
                / standing still
                / walking.
           """
    )




    st.header("**DataFrame**:")

    #Prompt the user to upload a csv file
    uploaded_file = st.file_uploader("Please choose a .CSV file", type=['csv'])
    if uploaded_file is not None:
        # do stuff
        df = pd.read_csv(uploaded_file)
        df1 = df.head()

    #Functions for rounding the avg_rating
    def round_float():
        st.dataframe(df.style.format({'avg_rating': '{:.2f}'}))
    def round_float_head():
        st.dataframe(df1.style.format({'avg_rating': '{:.2f}'}))

    st.markdown(""" You can select one of the following two options where you can choose between displaying
    the complete DataFrame or just the head (first five rows of the DataFrame).""")

    #Widgets for showing the DataFrame
    if st.button("Click here to see the full df"):
        with st.spinner('Loading the full DataFrame...'):
            time.sleep(4)
            round_float()
    elif st.button("Click here to see the head"):
        with st.spinner('Loading the head of the DataFrame...'):
            time.sleep(3)
        round_float_head()

    st.write("\n")
    st.write("\n")
    st.markdown("Now that you know how the data looks like. It's time for some analysis...")




    #User interactive analysis
    st.write("\n")
    st.write("\n")
    st.header("**A playground for Data Analysis** :football:")
    st.markdown("""Inorder to analyse the data we've implemented an interface where _you_ as a user 
    can interact with the dataset and play with it.\n""")

    #A tab where an user can select the columns that he wants to display
    interactive_col = st.multiselect("Please select the columns that you want to display from the above data.", df.columns)


    #Make the plots
    st.header("**Insights** :chart:")
    st.markdown("### Piano piano ... step by step we analyze the data together:")


    #Feature Engineering 
    st.markdown("Feature Engineering")
    st.image("Mutual Information Scores.PNG")
    st.image("FE_target.PNG")

    #Creating pinelines
    st.markdown("Creating pineline")
    num_attribs=df_train.drop('target',axis=1).columns.to_list()
    num_pip=Pipeline([('imputer',impute.SimpleImputer(strategy='median')),
                  ('scalar',MinMaxScaler()),
               ])  # ('PCA',PCA(n_components=12))
    tree_prepro=compose.ColumnTransformer([
    ('num',num_pip,num_vars)
    ])
    tree_prepro
    
    st.write("\n")
    st.write("\n")

