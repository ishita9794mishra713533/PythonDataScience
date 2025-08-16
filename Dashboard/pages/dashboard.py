import streamlit as st
import pandas as pd
import seaborn as sns
import plotly.express as px

st.subheader('Titanic Data Data Insights and Visualization')
st.markdown('Get all the insights as stats and visuals of Titanic data in this application ')

st.subheader('Dataset')

df= sns.load_dataset('titanic')
st.dataframe(df)

#Filters
st.sidebar.header("Filter Options")

gender= st.sidebar.multiselect('Gender', options = df['sex'].unique())


pclass= st.sidebar.multiselect('Passenger class', options = df['class'].unique())


min_age, max_age = st.sidebar.slider('Age', min_value = int(df['age'].min()),
                                            max_value = int(df['age'].max()),
                                            value= (int(df['age'].min()),int(df['age'].max())))

filtered_data = df[
    (df['sex'].isin(gender))&
    (df['pclass'].isin(pclass))&
    (df['age']>=min_age)&
    (df['age']<=max_age)
]

st.dataframe(filtered_data)

st.subheader('Visuals of Insights')

#Age Distribution
#color label is used to represent the columns through different colors 

fig1 = px.scatter(df, x='age', y='fare', color='survived',
                 title='Age vs Fare (Color = Survived)',
                 hover_data=['sex', 'class'])
st.plotly_chart(fig1)


fig2 = px.histogram(df, x='age', title='Age Distribution', color='embarked')
st.plotly_chart(fig2)
st.markdown('This fig shows the distribution of age of the people at the titanic ship ')


fig3 = px.box(df,x='pclass',y='age', color='survived', title='Age wise Fare')
st.plotly_chart(fig3)


fig4 = px.sunburst(df, path= ['class','sex','survived'], title='Survival by Class and Gender')
st.plotly_chart(fig4)
st.markdown('This fig shows the survival of people by class and gender at the titanic ship')