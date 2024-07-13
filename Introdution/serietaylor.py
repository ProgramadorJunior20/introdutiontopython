#Vamos a desarrollar una función que calcule 
#una aproximación de e^(iy) usando los primeros n términos de la serie.

import math 

def e_iy(y, n_terms):
    result = 1 #El primer termino siempre es 1
    term = 1   #Inicializamos el primer termino

    for n in range(1, n_terms):
        term *= (1j * y) / n #Calculamos el siguiente termino
        result += term       #Añadimos el termino al resultado

    return result

# Como Ejecutarlo
y = math.pi / 2 # y es igual a  pi dividido 2:  π/2
n_terms = 10    # Número de téminos que calcularemos en el ciclo for

result = e_iy( y, n_terms)
print(f"e^(i*π/2) ≈ {result}")
print(f"Parte real: {result.real}")
print(f"Parte imaginaria: {result.imag}")