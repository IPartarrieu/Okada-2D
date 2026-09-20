# Okada-2D

Modelo analítico 2D de dislocación elástica para una falla transcurrente vertical (caso límite del modelo de **Okada, 1985**), con una demo interactiva en Streamlit.

🔗 **Demo en vivo:** [okada-2d.streamlit.app](https://okada-2d-elk2vgsmc4zwq2ytuwxe66.streamlit.app/)

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://okada-2d-elk2vgsmc4zwq2ytuwxe66.streamlit.app/)

## Qué hace

Mueve el deslizamiento de la falla, la profundidad de bloqueo y si la falla es finita o desliza indefinidamente en profundidad (creep interseísmico), y la app recalcula al instante el perfil de deformación superficial usando la solución cerrada del modelo de dislocación elástica.

La fórmula y sus verificaciones matemáticas (antisimetría, decaimiento, caso límite de Savage & Burford) están en [`okada2d/model.py`](okada2d/model.py) y [`okada2d/tests/test_model.py`](okada2d/tests/test_model.py).

## Correr en local

```bash
cd okada2d
pip install -r requirements.txt
streamlit run app.py
```

## Ejercicio original (FEM)

El ejercicio original del curso "Métodos Matemáticos Avanzados para Geofísicos" (mallas y archivos de FEniCS) quedó en [`fem_exercise/`](fem_exercise/).
