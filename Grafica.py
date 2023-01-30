import numpy as np
import matplotlib.pyplot as plt
import sys

puntos_de_inicio = np.array([2.5,2.5])
iteraciones = 100
temperatura = 10000
alpha = float(sys.argv[1])
kT = float(sys.argv[2])
k = 0
plt.scatter(puntos_de_inicio[0], puntos_de_inicio[1])

def plot_cuadrado(p, a):
	plt.plot([p[0]-a, p[0] - a], [p[1] - a, p[1] + a], color = "navy")
	plt.plot([p[0]-a, p[0] + a], [p[1] - a, p[1] - a], color = "navy")
	plt.plot([p[0]+a, p[0] + a], [p[1] - a, p[1] + a], color = "navy")
	plt.plot([p[0]-a, p[0] + a], [p[1] + a, p[1] + a], color = "navy")
	

def delta_energia(p1, p2_x, p2_y):
	e = (p1[0] / p2_x) - (p2_y / p1[1])
	return 	e


while (k <= iteraciones):
	plt.xlim(-10,10)
	plt.ylim(-10,10)
	plt.xlabel(r'$x_{1}$')
	plt.ylabel(r'$x_{2}$')
	plt.title("Recocido Simulado de Metropolis")
	plt.grid()	
	x_nuevo = puntos_de_inicio[0] + alpha * np.random.uniform(-1,1)
	y_nuevo = puntos_de_inicio[1] + alpha * np.random.uniform(-1,1)

	delta = delta_energia(puntos_de_inicio, x_nuevo, y_nuevo)

	if delta < 0 :
		plot_cuadrado(puntos_de_inicio, alpha)
		plt.scatter(puntos_de_inicio[0], puntos_de_inicio[1], c = 'b', label = "Antiguo movimiento")
		puntos_de_inicio = [x_nuevo, y_nuevo]
		plt.scatter(puntos_de_inicio[0], puntos_de_inicio[1], c = 'r', label = "Nuevo movimiento")
		plt.pause(0.05)
	else:

		r = np.random.uniform(0,1)

		if r < np.exp( delta / kT):
			plot_cuadrado(puntos_de_inicio, alpha)
			plt.scatter(puntos_de_inicio[0], puntos_de_inicio[1], c = 'b')
			puntos_de_inicio = [x_nuevo, y_nuevo]
			plt.scatter(puntos_de_inicio[0], puntos_de_inicio[1], c = 'r')
			plt.pause(0.05)
		else:
			print("Aquí no ha pasado nada c-ñores")
	
	k += 1
	plt.clf()

print()
plt.show()
