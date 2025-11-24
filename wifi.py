'''
     Buscar la mejor señal de Wi-Fi en una habitación

        - Problema: Quieres la mayor intensidad de señal de Wi-Fi en tu casa.
        - Hill Climbing:

        Caminas por la habitación con tu celular mirando la barra de señal.

        Te mueves hacia donde la señal mejora.

        Cuando ya no mejora al moverte, te quedas ahí.

        * Función objetivo: Intensidad de señal (más barras de Wi-Fi).

        Máximo global: El punto exacto en la habitación donde la señal es más fuerte (ej. justo al lado del router).

        Estado inicial: Una ubicación inicial cualquiera dentro de la habitación (ej. sentado en el sillón o en una esquina).

        * Matemáticamente, se puede representar como una coordenada inicial (x,y) en la habitación.
'''

import random
import numpy as np
import matplotlib.pyplot as plt

# Simulamos la intensidad de Wi-Fi como una función en 2D
# Máximo global en (5,5)
def wifi_signal(x, y):
    return -((x-5)**2 + (y-5)**2) + 100

# Hill Climbing con registro de trayectoria
def hill_climbing(max_steps=50):
    path = []

    # Estado inicial (posición aleatoria en la habitación 0-10)
    x, y = random.randint(0,10), random.randint(0,10)
    path.append((x,y))

    for step in range(max_steps):
        current_signal = wifi_signal(x,y)

        # Posibles movimientos (vecinos)
        moves = [(1,0),(-1,0),(0,1),(0,-1)]
        neighbors = [(x+dx, y+dy) for dx,dy in moves 
                     if 0 <= x+dx <= 10 and 0 <= y+dy <= 10]

        # Evaluar vecinos
        best_neighbor = max(neighbors, key=lambda pos: wifi_signal(*pos))
        best_signal = wifi_signal(*best_neighbor)

        if best_signal > current_signal:
            x, y = best_neighbor
            path.append((x,y))
        else:
            break  # se quedó en un óptimo local

    return path

# Ejecutar hill climbing
path = hill_climbing()

# Crear una malla para la señal Wi-Fi
x = np.linspace(0,10,100)
y = np.linspace(0,10,100)
X, Y = np.meshgrid(x, y)
Z = wifi_signal(X, Y)

# Graficar mapa de calor de señal
plt.figure(figsize=(8,6))
plt.contourf(X, Y, Z, levels=50, cmap="viridis")
plt.colorbar(label="Intensidad de señal Wi-Fi")

# Graficar trayectoria
px, py = zip(*path)
plt.plot(px, py, marker="o", color="red", label="Camino Hill Climbing")
plt.scatter([5], [5], color="white", marker="*", s=200, label="Router (máximo global)")

plt.title("Hill Climbing - Búsqueda de mejor señal Wi-Fi")
plt.xlabel("X (posición en la habitación)")
plt.ylabel("Y (posición en la habitación)")
plt.legend()
plt.show()
