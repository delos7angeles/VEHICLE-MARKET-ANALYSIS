import streamlit as st
import pandas as pd
import plotly.express as px

# Leer los datos
df = pd.read_csv('vehicles_us.csv')

# Título de la aplicación
st.title('Análisis de vehículos usados en venta')

# Mostrar una vista previa del DataFrame
st.write('Vista previa de los datos:')
st.write(df.head())

# Crear casilla para mostrar el histograma
build_histogram = st.checkbox('Mostrar histograma del año del modelo')
if build_histogram:
    fig = px.histogram(df, x='model_year', nbins=30,
                       title='Distribución del año del modelo')
    st.plotly_chart(fig)

# Crear casilla para mostrar el gráfico de dispersión
build_scatter = st.checkbox('Mostrar gráfico de dispersión: precio vs kilometraje')
if build_scatter:
    fig2 = px.scatter(df, x='odometer', y='price',
                      title='Relación entre precio y kilometraje',
                      labels={'odometer': 'Kilometraje', 'price': 'Precio'})
    st.plotly_chart(fig2)