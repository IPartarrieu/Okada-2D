# Okada-2D

Modelo analítico 2D de dislocación elástica para una falla transcurrente vertical (caso límite del modelo de **Okada, 1985**), con una demo interactiva en Streamlit.

🔗 **Demo en vivo:** _pendiente de desplegar — ver instrucciones abajo_

![demo](https://img.shields.io/badge/streamlit-demo-ff4b4b?logo=streamlit&logoColor=white)

## Qué hace

Mueve el deslizamiento de la falla, la profundidad de bloqueo y si la falla es finita o desliza indefinidamente en profundidad (creep interseísmico), y la app recalcula al instante el perfil de deformación superficial usando la solución cerrada del modelo de dislocación elástica.

La fórmula y sus verificaciones matemáticas (antisimetría, decaimiento, caso límite de Savage & Burford) están en [`okada2d/model.py`](okada2d/model.py) y [`okada2d/tests/test_model.py`](okada2d/tests/test_model.py).

## Correr en local

```bash
cd okada2d
pip install -r requirements.txt
streamlit run app.py
```

## Desplegar gratis (Streamlit Community Cloud)

1. Andá a [share.streamlit.io](https://share.streamlit.io) y conectate con tu cuenta de GitHub.
2. "New app" → elegí este repo, branch `main`, main file path `okada2d/app.py`.
3. Deploy. En un par de minutos tenés el link público — pegalo en el badge de arriba y en tu perfil de GitHub.

## Ejercicio original (FEM)

El ejercicio original del curso "Métodos Matemáticos Avanzados para Geofísicos" (mallas y archivos de FEniCS) quedó en [`fem_exercise/`](fem_exercise/).
