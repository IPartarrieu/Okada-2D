import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from model import surface_displacement as uy  # noqa: E402

s, d1, d2 = 1.0, 2.0, 15.0

# 1) Antisimetria: uy(-x) == -uy(x)
for x in [0.5, 3, 10, 50]:
    a, b = float(uy(x, s, d1, d2)), float(uy(-x, s, d1, d2))
    assert abs(a + b) < 1e-12, (x, a, b)

# 2) Decae a 0 lejos de la falla (falla finita, no llega a superficie;
#    decae como 1/x, por eso hay que ir bien lejos)
assert abs(float(uy(1_000_000, s, d1, d2))) < 1e-3

# 3) Continuidad en x=0
assert abs(float(uy(1e-9, s, d1, d2))) < 1e-6

# 4) Caso limite: al hacer d2 -> infinito, debe reducirse a Savage-Burford
#    uy(x) = (s/pi) atan(x/d1)   (falla que desliza bajo profundidad d1
#    de forma indefinida, modelo de creep interseismico)
d2_big = 1e9
for x in [1, 5, 20]:
    approx = float(uy(x, s, d1, d2_big))
    savage_burford = (s / math.pi) * math.atan(x / d1)
    assert abs(approx - savage_burford) < 1e-6, (x, approx, savage_burford)

# 5) Salto total a traves de la falla cuando d1 -> 0 (rompe superficie)
d1_small = 1e-6
left = float(uy(-0.01, s, d1_small, d2))
right = float(uy(0.01, s, d1_small, d2))
assert abs(abs(right - left) - s) < 1e-2, (right, left, right - left)

print("Todas las verificaciones pasaron OK")
print("uy(5km) =", float(uy(5, s, d1, d2)), "m")
print("uy(-5km) =", float(uy(-5, s, d1, d2)), "m")
