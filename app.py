import seaborn as sns
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title('Titanic Dataset Analysis - Streamlit')

df = sns.load_dataset('titanic')
# st.dataframe(df)

st.sidebar.header('User Input Parameters')
# c = st.sidebar.selectbox('Select the class', df['class'].unique())
# g = st.sidebar.selectbox('Select the class', df['sex'].unique())

plot_type = st.sidebar.radio('Select the plot type', ('bar', 'line', 'hist', 'box', 'kde'))

if plot_type == 'bar':
    st.write('Bar Plot')
    fig, ax = plt.subplots()    
    df.groupby(['class', 'sex'])['survived'].mean().unstack().plot(kind='bar', ax=ax)   
    st.pyplot(fig)

elif plot_type == 'line':
    st.write('Line Plot')
    fig, ax = plt.subplots()
    df.groupby(['class', 'sex'])['survived'].mean().unstack().plot(kind='line', ax=ax)
    st.pyplot(fig)


elif plot_type == 'hist':
    st.write('Histogram Plot')
    fig, ax = plt.subplots()
    df.groupby(['class', 'sex'])['survived'].mean().unstack().plot(kind='hist', ax=ax)
    st.pyplot(fig)

elif plot_type == 'box':
    st.write('Box Plot')    
    fig, ax = plt.subplots()
    df.groupby(['class', 'sex'])['survived'].mean().unstack().plot(kind='box', ax=ax)
    st.pyplot(fig)

elif plot_type == 'kde':
    st.write('KDE Plot')    
    fig, ax = plt.subplots()
    df.groupby(['class', 'sex'])['survived'].mean().unstack().plot(kind='kde', ax=ax)
    st.pyplot(fig)