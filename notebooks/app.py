#Librerías
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

#leer datos
car_data = pd.read_csv("https://practicum-content.s3.us-west-1.amazonaws.com/new-markets/Data_sprint_4_Refactored/vehicles_us.csv")
car_data["type"] = car_data["type"].astype(str)

# Título
st.header('Protyecto 7 Analisis de Automoviles', divider = "blue")

#Botón para Descargar
st.download_button(
    label = "Descargar Dataset",
    data = car_data.to_csv(index=False),
    file_name = "car_data.csv"
)

st.divider()

#Botón para histograma 
hist_button = st.button('Construcción de Histograma')#creacion de boton 

if hist_button:#al hacer clic en el boton 
    #mensaje 
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de autos')
    #crear histograma 
    fig = px.histogram(car_data, x="odometer")
    #mostrar grafico Plotly 
    st.plotly_chart(fig, use_container_whidth=True, config={"displayModeBar": False})
    
st.divider()

#Boton para grafico de dispersión 
scatter_button = st.button('Grafico de dispersión')# creación de boton

if scatter_button:#al hacer clic en el boton
    #mensaje
    st.write('Creación de un grafico de disperion para el conjunto de datos de aununcios de venta de autos')
    #crear grafico de dispersion 
    fig = px.scatter(car_data, x="model_year", y="cylinders", color="type")
    #mostrar grafio Plotly
    st.plotly_chart(fig, use_container_whidth=True, config={"displayModeBar": False})
    
st.divider() 

#crear una casilla de verificacion 
build_histogram = st.checkbox('Construir un Histograma')

if build_histogram:
    #mensaje
    st.write('Construir un histograma para la columna odometer')
    #crar histograma 
    fig = px.histogram(car_data, x="odometer")
    #mostrar grafico Plotly
    st.plotly_chart(fig, use_container_whidth=True, config={"displayModeBar": False})
    

