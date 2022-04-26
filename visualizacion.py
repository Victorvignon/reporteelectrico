#Código de deployment de los resultados de análisis de datos, por Victos Joaquín Ortíz Vignon, Agencia de Energía del Estado de Puebla
#Librerías----
import streamlit as st  # Librería que permite crear el dashboard
import pandas as pd  # Permite visualizar y extraer dataframes
import plotly.express as px #Librería para graficar
#Dataframes----
pestado=pd.read_csv("https://docs.google.com/uc?id=1_ytwH-09_zRQRfBhTRKfo24pjWEMRwdr&export=download")
agraf=pd.read_csv("https://docs.google.com/uc?id=1umr8evAGxzw8nSj4nTwzl078rCnHMqYE&export=download")
paragraf=pd.read_csv("https://docs.google.com/uc?id=1Q2KdN7uPhFjcD0KQRnyZpFRJ6u-vsOto&export=download")
variables=pd.read_csv("https://docs.google.com/uc?id=1e0mxRGwX7-6QoVjbWJDj5jf-QA-ypIHv&export=download")
#https://drive.google.com/file/d/1e0mxRGwX7-6QoVjbWJDj5jf-QA-ypIHv/view?usp=sharing
#Gráficas----
graf2=px.bar(agraf,x="yaelect",y="Municipio",color="yaelect",title="10 municipios con menor porcentaje de electrificación")
graf1=px.bar(pestado,x="NOMGEO",y="2021",color="2021",title="Electrificación por estado")
graf3=px.bar(variables,x="% de elect.",y="municipio",color="% de elect.",title="Electrificación en Puebla por municpio")
#Código Streamlit----
st.set_page_config(page_title="Reporte",page_icon=":bar_chart:")
st.write("# :bar_chart: Reporte de análisis de datos sobre electrificación")
st.caption("Agencia de Energía del Estado de Puebla, Elaborado por Victor Joaquín Ortíz Vignon")
st.write("### Acerca de este reporte")
st.write(":wave: ¡Bienvenido! Este reporte es resultado de un proceso de análisis de datos, realizado en un periodo de prácticas profesionales, cuyo propósito es generar información de valor que a portara a un proyecto más grande que pueda transformarse en una política pública.")
st.write("Los objetivos específicos de deste proyecto son:")
st.write(":books: Generar bases de datos con indicadores relacionados a la electrificación a nivel estatal y nacional.")
st.write(":chart_with_upwards_trend: Visualizar la información de manera preliminar y de valor. ")
st.write(":mag: Analizar la correlación de los indicadores con la electrificación.")
st.write("Este documento trata de mostrar las visualizaciones y otros objetos que consideramos peuden ser de tu atención.")
st.write(":notebook: Puedes encontrar el reporte completo aquí: https://drive.google.com/file/d/1k1BWHaDZj3PMa52i2CsEyVec8WQyMlrm/view?usp=sharing")
st.write(":notebook: Puedes encontrar la presentación que resume el reporte aquí: https://docs.google.com/presentation/d/1MQbGzt1KKpHi-woxANC7ySsu19Xug2BJvi8C8pm8IrQ/edit?usp=sharing")
st.write("## Hallazgos")
st.write("### Nivel nacional")
st.write(graf1)
st.caption("Gráfica 1, elaboración propia, datos de CFE 2021")
st.write("### Nivel estatal")
st.write(graf2)
st.caption("Gráfica 2, elaboración propia, datos del censo de población y vivienda 2020")
st.write("El siguiente dataframe son los resultados de la correlación entre la falta de electricidad y las variables registradas en el censo de población y vivienda:")
st.write(paragraf)
st.write("De las variables anteriores, se seleccionaron las que tuvieran una correlación superior a 59% y se probaron en modelos lineales, el modelo con la mayor r cuadrada ajustada, tiene 4 variables, la siguiente es una tabla que incluye las cuatro variables además de las 3 relacionadas a la electrificación (viviendas con electricidad, sin electricidad y porcentaje de electrificación)")
st.write(variables)
st.write(graf3)
st.caption("Gráfica 3, elaboración propia, datos del censo de población y vivienda 2020")