"""
Este algoritmo dibuja un cuadrado con asteriscos.
"""
N = int(input("Escribe la dimensión N >= 2 del cuadrado a dibujar: "))
# Escribe la primera línea de asteriscos.
for i in range(N + 1):
    print('*', end="")

print()

# Dibuja las partes laterales
j = 1
while j <= N - 2:
    for k in range(N):
        if k == 0:
            print('*', end=" ")  # * + un espacio.
        elif k == N - 1:
            print('*', end="")  # Dos espacios + *.
        else:
            print(' ', end=" ")  # Dos espacios.
    print()
    j += 1

# Fin del ciclo while.

# Dibuja el lado de abajo.
i = 0
while i < N + 1:
    print('*', end="")  # * + un espacio.
    i += 1

# FIN del algoritmo
