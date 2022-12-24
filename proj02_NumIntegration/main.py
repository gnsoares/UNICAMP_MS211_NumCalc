import matplotlib.pyplot as plt
import numpy as np

# Constantes iniciais
r0 = .5 # taxa de reproducao da populacao
K0 = 10 # constante de capacidade do meio
h0 = .05 # passo dos metodos

# Funcao de iteracao
f = lambda r, y, K: r*y*(1-y/K)

# Item a
"""
t_euler = np.arange(0, 4, h0)
y_euler = np.zeros(t_euler.size, dtype=float)
y_euler[0] = 1 # condicao inicial
y_anal = (K0*y_euler[0]*np.exp(r0*t_euler))/(K0+y_euler[0]*(np.exp(r0*t_euler)-1))
for i in range(1, y_euler.size):
	y_euler[i] = y_euler[i-1] + h0*f(r0, y_euler[i-1], K0)
plt.figure(1)
plt.plot(t_euler, y_anal, 'k', linewidth=2)
plt.scatter(t_euler, y_euler, facecolors='none', edgecolors='b')
plt.axis([0, 4, 1, 5])
"""

# Item b
r = np.array([.2, .4, .6, .8])
h = np.array([.025, .1, .5, 1])
K = np.array([4, 8, 12, 16])
t_eulerb = np.zeros((h.size, int((4-0)/h[0])), dtype=float)
y_eulerb = np.zeros((t_eulerb.shape), dtype=float)

for i in range(h.size):
	t_eulerb[i, :int((4-0)/h[i])] = np.arange(0, 4, h[i])
	y_eulerb[i, 0] = 1 # condicao inicial
	for j in range(1, y_eulerb[i].size):
		y_eulerb[i, j] = y_eulerb[i, j-1] + h[i]*f(r[i], y_eulerb[i, j-1], K[i])
        
plt.figure(2, figsize=(9,5))
colors = ('b', 'r', 'g', 'm')
for i in range(h.size):
    plt.subplot(221 + i)
    y_anal = (K[i]*y_euler[0]*np.exp(r0*t_eulerb[i]))/(K[i]+y_euler[0]*(np.exp(r[i]*t_eulerb[i])-1))
    plt.plot(t_eulerb[i], y_anal, 'k', linewidth=2)
    plt.scatter(t_eulerb[i, :int((4-0)/h[i])], y_eulerb[i, :int((4-0)/h[i])], facecolors='none', edgecolors=colors[i])
    plt.xlabel('Tempo')
    plt.ylabel('Tamanho da população')
    plt.grid(True)
    plt.axis([0, 4, 1, 5])
    plt.title('h = %.2f; r = %.2f; K = %.2f' %(h[i], r[i], K[i]))
print('Comparação do Método de Euler com diferentes passos e parâmetros com a Solução Analítica')



# Item c
"""
t_rk4 = np.arange(0, 10, h0)
y_rk4 = np.zeros(t_rk4.size, dtype=float)
y_rk4[0] = 1 # condicao inicial
y_anal = (K0*y_rk4[0]*np.exp(r0*t_rk4))/(K0+y_rk4[0]*(np.exp(r0*t_rk4)-1))
for i in range(1, y_rk4.size):
	k1 = h0*f(r0, y_rk4[i-1], K0)
	k2 = h0*f(r0, y_rk4[i-1] + k1/2, K0)
	k3 = h0*f(r0, y_rk4[i-1] + k2/2, K0)
	k4 = h0*f(r0, y_rk4[i-1] + k3, K0)
	y_rk4[i] = y_rk4[i-1] + (1/6)*(k1 + 2*k2 + 2*k3 + k4)
plt.figure(3)
plt.plot(t_rk4, y_anal, 'k', linewidth=2)
plt.scatter(t_rk4, y_rk4, facecolors='none', edgecolors='b')
plt.axis([0, 10, 1, 10])
"""

plt.show()
