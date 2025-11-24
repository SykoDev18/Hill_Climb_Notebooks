'''
    Ejemplo 1: Subir una montaña a ciegas con Hill Climbing.

        La función será una parábola simple que representa la montaña:

        𝑓(𝑥)= −(𝑥−3)**2 + 9

       -Aquí:

            El máximo global está en x = 3 con f(3) = 9.

            El estado inicial será un punto aleatorio en el rango [0, 6].



        Qué hace el programa:

            Empieza en un punto aleatorio dentro del rango [0,6].

            Se mueve con pequeños pasos buscando siempre subir.

            Si un movimiento lo lleva a mayor altura (f(x) mayor), lo acepta.

            Si ya no encuentra una mejora, se queda ahí.

        El gráfico muestra:

                La curva de la montaña.

                El recorrido en rojo del Hill Climbing.

                El máximo global real en verde (x=3).
                

        Otros aspectos importantes:
        
            np.linspace(0, 6, 200) genera 200 puntos entre 0 y 6.

            Esos puntos sirven solo para dibujar la curva suave de la función 𝑓(𝑥).

            Mientras más puntos pongas (200, 500, 1000…), más detallada y continua se verá la gráfica.

            En cambio:

            max_iter = 100 significa que el Hill Climbing dará hasta 100 pasos de búsqueda.

            Esos se guardan en la lista history y se grafican con ro-, mostrando el camino real que siguió el algoritmo.

        En resumen:

                200 = resolución de la curva para que se vea suave en la gráfica.

                100 = número de pasos del algoritmo de optimización.

        La implementación que vimos del Hill Climbing siempre sube y nunca baja.

            Razón:

                En el código, la condición es:

                if f(neighbor) > f(x):  
                    x = neighbor


            Esto significa:

                Si el vecino tiene mejor valor, me muevo ahí.

                Si no mejora, me quedo donde estoy.

                Por eso el algoritmo:

                Nunca baja, porque ignora los movimientos que reducen la función.

                Se queda atrapado en el primer máximo local que encuentre.

            Consecuencias:

                Si la función tiene un solo máximo global (como la parábola que usamos), no hay problema: siempre llegará a la cima.

                Si la función tiene varios picos (máximos locales), el Hill Climbing puede quedarse atrapado en uno más bajo.

                Ejemplo visual:
                
                    Si la función parece montañas y colinas, el Hill Climbing puede quedarse en una colina baja porque no se permite bajar para luego subir más alto.

                    Existen variantes que sí permiten “bajar” temporalmente:

                        Hill Climbing estocástico (acepta un vecino aleatorio aunque no sea mejor).

                        Simulated Annealing (acepta peores soluciones con cierta probabilidad que va bajando con el tiempo).
'''

import random
import numpy as np
import matplotlib.pyplot as plt

# Función objetivo (la "montaña")
def f(x):
    return -(x-3)**2 + 9

# Máximo global (cima de la montaña)
x_global_max = 3
y_global_max = f(x_global_max)

# Estado inicial (posición aleatoria en la montaña)
x = random.uniform(0, 6)
step_size = .1
max_iter = 50
history = [x]

# Hill Climbing
for i in range(max_iter):
    neighbor = x + random.uniform(-step_size, step_size)
    neighbor = max(0, min(6, neighbor))  # Mantener dentro del rango
    if f(neighbor) > f(x):  # Acepta si mejora
        x = neighbor
    history.append(x)

# Mostrar resultados
print("Estado inicial:", history[0])
print("Mejor solución encontrada: x =", x)
print("f(x) =", f(x))
print("Máximo global real: x =", x_global_max, ", f(x) =", y_global_max)

# Graficar
xs = np.linspace(0, 6, 200)
ys = f(xs)

plt.plot(xs, ys, label='Función f(x)')
plt.plot(history, f(np.array(history)), 'ro-', label='Progreso Hill Climbing')
plt.plot(x_global_max, y_global_max, 'go', markersize=10, label='Máximo global')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Ejemplo 1: Subir una montaña a ciegas')
plt.legend()
plt.show()
