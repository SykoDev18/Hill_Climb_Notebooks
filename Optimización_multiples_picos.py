'''
    Ejercicio 5: Optimización de función con múltiples picos

        Problema: Maximizar f(x)=xsin(4x)+1.1x en [0,10].

        Función objetivo:

        import math
        def f(x):
            return x * math.sin(4*x) + 1.1 * x

    Explicación: Función con varios picos locales; Hill Climbing puede quedarse en máximos locales dependiendo del punto inicial.
'''

import random
import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return x * np.sin(4*x) + 1.1 * x

# Para este ejemplo, se calcula aproximado del máximo global
xs_fine = np.linspace(0, 10, 1000)
x_global_max = xs_fine[np.argmax(f(xs_fine))]
y_global_max = f(x_global_max)

x = random.uniform(0, 10)
step_size = 0.1
max_iter = 200
history = [x]

for i in range(max_iter):
    neighbor = x + random.uniform(-step_size, step_size)
    neighbor = max(0, min(10, neighbor))
    if f(neighbor) > f(x):
        x = neighbor
    history.append(x)

xs = np.linspace(0, 10, 400)
ys = f(xs)

plt.plot(xs, ys, label='Función f(x)')
plt.plot(history, f(np.array(history)), 'ro-', label='Progreso Hill Climbing')
plt.plot(x_global_max, y_global_max, 'go', markersize=10, label='Máximo global')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Ejercicio 5: Maximizar x*sin(4x) + 1.1*x')
plt.legend()
plt.show()
