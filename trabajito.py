import streamlit as st 


st.write("Tarea sobre Streamlit")
import pandas as pd
from pandas.core.base import value_counts


#¿Hay una correlación entre las calificaciones de un alumno y sus hábitos alimenticios?

sp=pd.read_csv('StudentsPerformance.csv')
#print(sp[['gender','lunch','math score','reading score','writing score']].value_counts())

#¿Hay una correlación entre las calificaciones de un alumno y el nivel de estudios de sus padres?
#print(sp[['gender','parental level of education']].value_counts()) #tengo dudas como relacionar las calificaciones sin que salga un monton de numeros

#¿Hay una correlación entre las calificaciones de un alumno y su sexo?
#print(sp[['gender','parental level of education']].value_counts())

st.header('Nuestro primer repositorio en el curso',)

genre = st.radio(
    "¿Qué deseas saber?",
    ('¿Hay una correlación entre las calificaciones de un alumno y sus hábitos alimenticios?', '¿Hay una correlación entre las calificaciones de un alumno y el nivel de estudios de sus padres?', '¿Hay una correlación entre las calificaciones de un alumno y su sexo?'))
     
if genre == '¿Hay una correlación entre las calificaciones de un alumno y sus hábitos alimenticios?':
    st.write('La correlacción entre calificaciones de un alumno y sus hábitos alimenticios es:')

elif genre == '¿Hay una correlación entre las calificaciones de un alumno y el nivel de estudios de sus padres?':
    st.write("La correlación entre las calificaciones de un alumno y el nivel de estudios de sus padres")

else:
    genre == '¿Hay una correlación entre las calificaciones de un alumno y su sexo?'
    st.write("La correlación entre las calificaciones de un alumno y su sexo")


import csv

# Ruta... (misma carpeta)
filename = 'StudentsPerformance.csv' 

with open(filename) as f:
    
    # objeto iterable
    header = next(f)

    # Imprimir 1era fila.
    for h in header:
        print(h, end='')