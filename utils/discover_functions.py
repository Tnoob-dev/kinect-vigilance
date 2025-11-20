import freenect

print("Funciones disponibles:")
for func in dir(freenect):
    if not func.startswith('_'):  # Filtrar funciones privadas
        print(f"{func}")