import streamlit as st
import random
from PIL import Image
from collections import Counter

# Título de la aplicación
st.title("Simulación de Máquina Expendedora de Chicles 🎡")

# Descripción
st.markdown("""
Bienvenido a la máquina expendedora de chicles. Aquí puedes cargar chicles de diferentes colores y simular compras para analizar probabilidades.
""")

# **1. Configuración de colores**
st.sidebar.header("Configura la Máquina")
red_balls = st.sidebar.number_input("Chicles Rojos:", min_value=0, value=10, step=1)
blue_balls = st.sidebar.number_input("Chicles Azules:", min_value=0, value=5, step=1)
yellow_balls = st.sidebar.number_input("Chicles Amarillos:", min_value=0, value=8, step=1)
green_balls = st.sidebar.number_input("Chicles Verdes:", min_value=0, value=7, step=1)

# Inicializar máquina
machine = ["rojo"] * red_balls + ["azul"] * blue_balls + ["amarillo"] * yellow_balls + ["verde"] * green_balls
results = st.session_state.get("results", [])

# **2. Cargar imágenes**
chicle_images = {
    "rojo": "/workspaces/maquina.chicles/images/red_ball.png",
    "azul": "/workspaces/maquina.chicles/images/blue_ball.png",
    "amarillo": "/workspaces/maquina.chicles/images/yellow_ball.png",
    "verde": "/workspaces/maquina.chicles/images/green_ball.png"
}

machine_image = "/workspaces/maquina.chicles/images/machine.png"

# **3. Mostrar la máquina con las bolas gráficamente**
st.subheader("Vista de la Máquina de Chicles")

if machine:
    # Mostrar la imagen de la máquina
    st.image(machine_image, caption="Máquina Expendedora", use_container_width=True)
    
    # Mostrar los chicles
    st.write("Chicles disponibles:")
    rows = []
    for ball in machine:
        rows.append(chicle_images[ball])
    for i in range(0, len(rows), 10):  # Mostrar en filas de 10
        cols = st.columns(10)
        for j, col in enumerate(cols):
            if i + j < len(rows):
                col.image(rows[i + j], width=50)
else:
    st.write("La máquina está vacía. Por favor, configura los chicles en la barra lateral.")

# **4. Comprar un chicle**
if st.button("Comprar un Chicle 🍬"):
    if machine:
        chosen_ball = random.choice(machine)
        results.append(chosen_ball)
        st.session_state["results"] = results
        st.success(f"¡Salió un chicle de color {chosen_ball.upper()}!")
        # Eliminar el chicle de la máquina
        machine.remove(chosen_ball)
    else:
        st.warning("La máquina está vacía. Recarga más chicles desde la barra lateral.")

# **5. Mostrar resultados acumulados**
if results:
    st.subheader("Resultados Acumulados")
    counter = Counter(results)
    st.bar_chart(counter)

# **6. Reiniciar máquina**
if st.button("Reiniciar Máquina 🔄"):
    st.session_state["results"] = []
    st.experimental_rerun()

