import streamlit as st
import plotly.graph_objects as go

st.title("🎈 Índice de Masa Corporal ")

def clasificacionIMC(imc):
    if imc < 18.5:
        clasificacion = "Bajo peso"
    elif 18.5 <= imc < 25:
        clasificacion = "Peso normal"
    elif 25 <= imc < 30:
        clasificacion = "Sobrepeso"
    elif 30 <= imc < 35:
        clasificacion = "Obesidad grado I"
    elif 35 <= imc < 40:
        clasificacion = "Obesidad grado II"
    else:
        clasificacion = "Obesidad grado III"
    return  clasificacion   

# Título de la app
# Valor para el gauge
altura = st.number_input('Altura (cm) : ', value = 1)
peso = st.number_input('Peso (kg) : ', value = 1)
imc = peso / ((altura/100)**2)
if imc < 100:
   st.info(f"Tu IMC es **{imc:.2f}** → {clasificacionIMC(imc)}")

# Crear el gráfico gauge
fig = go.Figure(go.Indicator(
    mode="gauge+number",
    value=imc,
    title={'text': "IMC"},
    gauge={
        'axis': {'range': [0, 50]},
        'bar': {'color': "darkblue"},
        'steps': [
            {'range': [0, 18.5], 'color': "lightgray"},
            {'range': [18.6, 24.9], 'color': "gray"},
            {'range': [25, 29.9], 'color': "yellow"},
            {'range': [30, 50], 'color': "red"}
        ],
        'threshold': {
            'line': {'color': "red", 'width': 4},
            'thickness': 0.75,
            'value': 50
        }
    }
))

# Mostrar en Streamlit
st.plotly_chart(fig)
