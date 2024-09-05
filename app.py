import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv(
    'D:/Tripleten/Proyecto6/vehicles_us.csv')  # leer los datos

# crear una casilla de verificación
build_histogram = st.checkbox('Histograma Vehiculos')
if build_histogram:  # si la casilla de verificación está seleccionada
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    # crear un histograma
    fig = px.histogram(car_data, x="odometer")
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)


# crear una casilla de verificación
build_dispercion = st.checkbox('Grafico de Dispercion Vehiculos')
if build_dispercion:  # si la casilla de verificación está seleccionada
    st.write('Creación de un grafico de dispercion para el conjunto de datos de anuncios de venta de coches')
    # crear un gráfico de dispersión
    dispercion = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(dispercion, use_container_width=True)
