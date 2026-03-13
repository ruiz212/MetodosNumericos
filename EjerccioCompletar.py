import math

# 1. Definimos los valores base
x = 10  
a = 9

# 2. Pedimos los datos al usuario (todo en la misma línea para que se vea más limpio)
grado = int(input("Ingrese el grado del polinomio de Taylor: "))
resto = int(input("Ingrese hasta qué grado desea calcular el resto: "))

# 3. Variables iniciales para el Polinomio
Aproximacion = 0.0
exponente = 0.5
multiplicador_Derivada = 1.0

print("\n" + "="*50)
print(f" Calculando Taylor para sqrt({x}) centrado en {a}")
print(f" Valor real en calculadora: {math.sqrt(x):.8f}")
print("="*50 + "\n")

# 4. Bucle matemático para el Polinomio de Taylor
for n in range(grado + 1):
    if n == 0: 
        termino = math.sqrt(a)
    else:
        # Construimos el patrón de la derivada paso a paso
        multiplicador_Derivada *= (exponente - (n - 1))
        derivada_n = multiplicador_Derivada * (a ** (exponente - n))
        
        # Fórmula completa de Taylor
        termino = (derivada_n / math.factorial(n)) * ((x - a) ** n)
        
    # Acumulamos el resultado
    Aproximacion += termino
    
    # Mostramos el desglose
    print(f"--- GRADO {n} ---")
    print(f"Término sumado/restado: {termino: .8f}")
    print(f"Aproximación actual:    {Aproximacion: .8f}\n")


# 5. Bucle matemático para el Resto (Error máximo garantizado)
print("="*50)
print(" CÁLCULO DEL RESTO (COTA DE ERROR MÁXIMO)")
print("="*50)

# Reiniciamos el multiplicador a 1.0 para esta nueva fase
multiplicador_Resto = 1.0 

for n in range(resto + 1):
    # El Resto de grado 'n' siempre usa el grado 'n + 1'
    grado_siguiente = n + 1
    
    # Construimos la derivada para el grado_siguiente
    multiplicador_Resto *= (exponente - (grado_siguiente - 1))
    
    # Evaluamos en el "peor caso" posible (c = 9) para maximizar el margen de error
    c = 9
    derivada_c = multiplicador_Resto * (c ** (exponente - grado_siguiente))
    
    # Fórmula del Resto de Lagrange
    valor_resto = (derivada_c / math.factorial(grado_siguiente)) * ((x - a) ** grado_siguiente)
    
    # Imprimimos en valor absoluto (abs) porque nos interesa el tamaño del error, no el signo
    print(f"Error máximo garantizado al usar P{n} (R{n}): {abs(valor_resto): .8f}")

print("\n")
    
    