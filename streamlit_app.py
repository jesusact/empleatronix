import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

st.title("Empleatronix")
st.write("Todos los datos sobre los empleados en una aplicación.")

# Leemos y mostramos los datos
employees = pd.read_csv('employees.csv')
st.dataframe(employees)

# Creamos los botones de elección
color, name_election, salary_election = st.columns(3)

with color:
    color = st.color_picker("Elige un color para las barras", "#00f900")

with name_election:
    name_election = st.toggle("Mostrar el nombre", value=True)

with salary_election:
    salary_election = st.toggle("Mostrar sueldo en la barra")

# Creamos la gráfica
fig, ax = plt.subplots()

bars = ax.barh(employees['full name'], employees['salary'], color=color)

# Modificamos las etiquetas en función de la elección
if not name_election:
    ax.set_yticklabels([''] * len(employees['full name']))  

if salary_election:
    # Añadimos el salario al final de cada barra
    for bar, salary in zip(bars, employees['salary']):
        ax.text(bar.get_width() + 50, bar.get_y() + bar.get_height() / 2,
                f'{salary} €', va='center')

# Configuramos las etiquetas de los ejes
ax.set_xlabel('')
ax.set_ylabel('')

# Configuramos el rango del eje X
ax.set_xlim(0, 4500)

# Mostramos el gráfico en Streamlit
st.pyplot(fig)