"""Modelo analitico 2D de dislocacion elastica para una falla transcurrente
vertical, enterrada en un semi-espacio elastico homogeneo.

Es el caso limite del modelo de Okada (1985) cuando la falla es vertical
(dip = 90 grados) e infinita a lo largo del rumbo: el problema se reduce a
deformacion antiplana en la seccion 2D perpendicular a la falla, y tiene
solucion cerrada (Rybicki 1971; Savage & Burford 1973).

Convencion: s > 0 corresponde a un movimiento lateral derecho (el lado
x > 0 se desplaza en +y respecto al lado x < 0).
"""

import numpy as np


def surface_displacement(x, s, d1, d2):
    """Desplazamiento horizontal paralelo al rumbo en la superficie.

    Parameters
    ----------
    x : array_like
        Distancia horizontal perpendicular a la falla [km].
    s : float
        Deslizamiento de la falla [m].
    d1 : float
        Profundidad superior de la zona que desliza [km]. Usar un valor
        chico (> 0) para simular una falla que rompe la superficie.
    d2 : float
        Profundidad inferior de la zona que desliza [km]. Usar un valor
        muy grande (>= 1e6) para simular creep profundo indefinido
        (modelo interseismico de Savage & Burford).

    Returns
    -------
    ndarray
        Desplazamiento superficial u_y(x) [m].
    """
    x = np.asarray(x, dtype=float)
    return (s / np.pi) * (np.arctan(x / d1) - np.arctan(x / d2))
