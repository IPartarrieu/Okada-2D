import matplotlib.pyplot as plt
import numpy as np
import streamlit as st

from model import surface_displacement

st.set_page_config(page_title="Okada 2D", page_icon="🌋", layout="centered")

st.title("🌋 Deformación 2D de una falla transcurrente")
st.markdown(
    "Modelo analítico de dislocación elástica (caso límite 2D del modelo "
    "de **Okada, 1985**, para una falla vertical infinita a lo largo del "
    "rumbo). Mueve los controles para ver cómo cambia la deformación "
    "superficial."
)

with st.sidebar:
    st.header("Parámetros de la falla")
    s = st.slider("Deslizamiento s [m]", 0.1, 10.0, 3.0, 0.1)
    modo = st.radio(
        "Comportamiento en profundidad",
        ["Falla enterrada (finita)", "Creep interseísmico (infinita)"],
    )
    d1 = st.slider("Profundidad de bloqueo d₁ [km]", 0.01, 20.0, 3.0, 0.1)
    if modo == "Falla enterrada (finita)":
        d2 = st.slider("Profundidad inferior d₂ [km]", d1 + 0.5, 60.0, 20.0, 0.5)
    else:
        d2 = 1e6
    rango = st.slider("Rango de la gráfica [km]", 10, 200, 60, 10)

x = np.linspace(-rango, rango, 600)
u = surface_displacement(x, s, d1, d2)

fig, (ax1, ax2) = plt.subplots(
    2, 1, figsize=(7, 6), height_ratios=[2.2, 1], sharex=True
)

ax1.axhline(0, color="0.8", lw=1)
ax1.axvline(0, color="0.8", lw=1)
ax1.plot(x, u, color="#c0392b", lw=2.5)
ax1.set_ylabel("Desplazamiento superficial $u_y$ [m]")
ax1.set_title("Perfil de deformación en superficie")
ax1.grid(alpha=0.3)

d2_plot = min(d2, rango)
ax2.plot([0, 0], [-d1, -d2_plot], color="#2c3e50", lw=4, solid_capstyle="butt")
if d2 > rango:
    ax2.annotate(
        "",
        xy=(0, -rango),
        xytext=(0, -rango * 0.85),
        arrowprops=dict(arrowstyle="-|>", color="#2c3e50"),
    )
ax2.set_ylim(-rango * 0.6, 1)
ax2.set_xlim(-rango, rango)
ax2.set_xlabel("Distancia perpendicular a la falla x [km]")
ax2.set_ylabel("Profundidad [km]")
ax2.set_title("Sección transversal (esquema, sin escala real)")
ax2.grid(alpha=0.3)

st.pyplot(fig)

st.markdown(
    f"""
**Lectura rápida:** con un deslizamiento de `{s:.1f} m` bloqueado hasta
`{d1:.1f} km` de profundidad, el desplazamiento máximo lejos de la falla
tiende a `±{s/2:.2f} m`.
"""
)

with st.expander("¿Qué hay detrás de este modelo?"):
    st.markdown(
        r"""
Para una falla transcurrente vertical, infinita a lo largo del rumbo, el
problema elástico se desacopla en deformación antiplana y tiene solución
cerrada:

$$u_y(x) = \frac{s}{\pi}\left[\arctan\left(\frac{x}{d_1}\right) -
\arctan\left(\frac{x}{d_2}\right)\right]$$

Este es el caso límite 2D del modelo general de Okada (1985) para
dislocaciones en un semi-espacio elástico, y es el mismo tipo de curva
que se usa para ajustar velocidades GPS a través de fallas activas
(modelo de Savage & Burford, 1973). El código completo, con las
verificaciones matemáticas de la fórmula, está en
[`model.py`](https://github.com/IPartarrieu/Okada-2D/blob/main/okada2d/model.py).
"""
    )
