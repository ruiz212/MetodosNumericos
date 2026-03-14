import math

# 1. Pedimos los datos al usuario
x_grados = float(input("Ingrese el ángulo a calcular (ej. 47): "))
a_grados = float(input("Ingrese el ángulo base (ej. 45): "))
grado = int(input("Ingrese el grado del polinomio: "))

# ¡IMPORTANTE! Las fórmulas matemáticas en programación exigen radianes
x = math.radians(x_grados)
a = math.radians(a_grados)

Aproximacion = 0.0

print("\n" + "="*50)
print(f" Calculando Taylor para sen({x_grados}°) centrado en {a_grados}°")
print(f" Valor real en calculadora: {math.sin(x):.8f}")
print("="*50 + "\n")

# 2. El bucle matemático
for n in range(grado + 1):
    
    # Automatizamos la derivada usando el ciclo de 4 pasos
    ciclo = n % 4
    
    if ciclo == 0:
        derivada_a = math.cos(a)
    elif ciclo == 1:
        derivada_a = -math.sin(a)
    elif ciclo == 2:
        derivada_a = -math.cos(a)
    elif ciclo == 3:
        derivada_a = math.sin(a)
        
    # Aplicamos la fórmula completa de Taylor
    termino = (derivada_a / math.factorial(n)) * ((x - a) ** n)
    
    # Acumulamos el resultado
    Aproximacion += termino
    
    print(f"--- GRADO {n} ---")
    print(f"Derivada usada: paso {ciclo} del ciclo")
    print(f"Término sumado/restado: {termino: .8f}")
    print(f"Aproximación actual:    {Aproximacion: .8f}\n")