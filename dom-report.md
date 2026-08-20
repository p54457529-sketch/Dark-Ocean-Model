# Dark Ocean Model (DOM)

> A Python cosmological simulation: galaxy formation inside the "Dark Ocean" of dark matter

---

## 1) Main Idea
We treat dark matter as an **ocean** in which galaxies float.
This ocean does two things:

1. Adds extra gravity toward the galactic center (explains galaxy rotation curves).
2. Competes with Hubble expansion; gravity tries to clump matter, expansion tries to spread it out.

---

## 2) Model Equations

- Newtonian gravity from the galactic center:

$$F_g = \frac{GM}{r^2}$$

- Hubble expansion (outward acceleration):

$$a_H = H_0^2 \, r$$

- Dark ocean force (weak spring-like pull toward center):

$$F_{dark} = -k \, r$$

---

## 3) Simulation Setup

| Item | Description |
|---|---|
| Language | Python 3 (Pydroid 3) |
| Libraries | NumPy + Matplotlib |
| Particles | 200 particles on a disk |
| Steps | 500 time steps |

---

## 4) Results

### 4.1 Dynamic Stability Analysis
![Dynamic Stability](Screenshot_20260818-122148_Pydroid 3.jpg)

The galactic disk keeps its normalized dispersion after 500 steps — it is **stable**.

### 4.2 Initial Galaxy Disk
![Initial Galaxy Disk](Screenshot_20260817-154024_Pydroid 3.jpg)

Particles start from a rotating disk; gravity + dark ocean form a disk-like structure.

### 4.3 Key Plots

| File | Content |
|---|---|
| `gravity_vs_expansion.png` | Gravity vs expansion competition |
| `equilibrium_test.png` | Model equilibrium test |
| `dom_stress_test.png` | Stress test of the model |
| `simulation_result.png` | Main simulation result |
| `simulation_result_interaction.png` | Simulation with particle interactions |

---

## 5) Numerical Results

| Parameter | Value | Description |
|---|---|---|
| Expansion rate $H_0$ | 0.01 | Simulation scale |
| Central mass $M$ | 100000 | Galaxy mass |
| Initial radius $R_0$ | 30 | Distance units |
| Final dispersion | [number from Pydroid output] | Stability measure |
| Equilibrium result | [number from Pydroid output] | Gravity/expansion balance |

---

## 6) Core Code (Summary)
```python
import numpy as np
import matplotlib.pyplot as plt

G = 1.0; M = 1e5; H0 = 0.01; N = 200
R0, V0, DT, STEPS = 30.0, 0.8, 0.01, 500

np.random.seed(42)
theta = np.random.uniform(0, 2*np.pi, N)
r = R0 * np.sqrt(np.random.uniform(0, 1, N))
x, y = r*np.cos(theta), r*np.sin(theta)
vx, vy = -V0*np.sin(theta), V0*np.cos(theta)

stability = []
for step in range(STEPS):
ax = np.zeros(N); ay = np.zeros(N)
for i in range(N):
d = np.hypot(x[i], y[i]) + 1e-6
f = G*M / d**2
ax[i] += f * (-x[i])/d
ay[i] += f * (-y[i])/d
ax[i] += -0.002 * x[i]      # dark ocean
ay[i] += -0.002 * y[i]
ax[i] += H0*H0 * x[i]       # Hubble expansion
ay[i] += H0*H0 * y[i]
vx += ax*DT; vy += ay*DT
x += vx*DT; y += vy*DT
stability.append(np.std(np.hypot(x, y)) / np.mean(np.hypot(x, y)))

print("Stability:", stability[-1])

plt.plot(stability)
plt.title("Dynamic Stability Analysis")
plt.xlabel("Step"); plt.ylabel("Normalized Dispersion")
plt.show()
