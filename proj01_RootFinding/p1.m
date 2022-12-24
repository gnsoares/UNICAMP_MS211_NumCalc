% Limpeza do workspace
clear all
clc

% Atribuição das constantes
EPSILON = 1e-12	% Erro aceitável
ALPHA = 0.2	% Constante da equação
BETA = 2	% Constante da equação

% Estabelecimento do intervalo em que a raiz se encontra
x = -5:0.01:5	% Intervalo de x para investigação da curva
y = exp(ALPHA*x) - exp((ALPHA-1)*x) - BETA	% Atribuicao de x na equação -> f(x) = y
plot(x,y)

% Método da Bissecção
a = 3	% Valor mínimo do intervalo
b = 4	% Valor máximo do intervalo
[x_bissec, n_bissec] = bissecBV(a,b, ALPHA, BETA, EPSILON)

% Método de Newton
x_newt = (3+4)/2
n_max = 10
[x_newt, n_newt] = newtonBV(x_newt, ALPHA, BETA, EPSILON, n_max)

% Implementação das funções de resolução

% Método da Bissecção
function [r, n] = bissecBV(a, b, ALPHA, BETA, EPSILON)
	n = 0	% Número de iterações
	n_max = ceil((log10(b-a)-log10(EPSILON))/(log10(2)))	% Número máximo de iterações

	while b - a >= EPSILON & n < n_max

		y_k = exp(ALPHA*((a+b)/2)) - exp((ALPHA-1)*((a+b)/2)) - BETA

		if y_k > 0
			b = (a+b)/2
			n = n + 1
		elseif y_k < 0
			a = (a+b)/2
			n = n + 1
		else
			break
		end

	end
	r = (a+b)/2
end

% Método de Newton
function [r, n] = newtonBV(x0, ALPHA, BETA, EPSILON, n_max)
	n = 0

	while abs(exp(ALPHA*x0) - exp((ALPHA-1)*x0) - BETA) >= EPSILON & n < n_max

		x0 = x0 - (exp(ALPHA*x0) - exp((ALPHA-1)*x0) - BETA)/(exp((ALPHA-1)*x0)*(ALPHA*(exp(x0)-1)+1))
		n = n + 1
		
	end
	r = x0
end