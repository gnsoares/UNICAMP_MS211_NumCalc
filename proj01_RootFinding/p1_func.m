function [r, n] = bissecBV(a, b)
	n = 0	% Número de iterações
	n_max = ceil((log10(b-a)-log10(epsilon))/(log10(2)))	% Número máximo de iterações
	while b - a >= epsilon & n < n_max
		y_k = exp(alpha*((a+b)/2)) - exp((alpha-1)*((a+b)/2)) - beta
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

function [r, n] = newtonBV(x0)
	while abs(exp(alpha*x0) - exp((alpha-1)*x0) - beta) >= epsilon & n_newt < n_max
		x0 = x0 - (exp(alpha*x0) - exp((alpha-1)*x0) - beta)/(exp((alpha-1)*x0)*(alpha*(exp(x0)-1)+1))
		n_newt = n_newt + 1
	end
	r = x0
end