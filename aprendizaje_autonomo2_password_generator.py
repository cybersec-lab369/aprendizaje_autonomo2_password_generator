import random

# Mensaje de bienvenida en pantalla
print("=" * 50)
print("   GENERADOR DE CONTRASEÑAS")
print("=" * 50)

# Todos los caracteres disponibles para que ingrese el usuario
caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+-=[]{}|;:',.<>?/"

# Variable de control para mantener el programa corriendo
ejecutando = True

while ejecutando:
    # Menú de opciones
    print("\n¿Qué deseas hacer?")
    print("  1. Generar contraseña aleatoria")
    print("  2. Ingresar contraseña manualmente")

    # \n: Da un salto de línea para que no quede todo amontonado.
    # .strip() elimina los espacios en la respuesta que el usuario haya escrito de forma erronea
    opcion = input("\nElige opción (1 o 2): ").strip()
    
    # Variable para almacenar la contraseña en cada intento
    contrasena = ""
    
    if opcion == "1":
        # OPCIÓN 1: GENERAR CONTRASEÑA
        # \n: Da un salto de línea para que no quede todo amontonado.
        # .strip() elimina los espacios en la respuesta que el usuario haya escrito de forma erronea
        longitud_input = input("\n¿Cuántos caracteres quieres? (por defecto 12): ").strip()
        
        # Si el usuario presiona Enter sin escribir nada, se asignan aleatoriamente 12 caracteres
        if longitud_input == "":
            longitud = 12
        
        elif longitud_input.isdigit():
            longitud = int(longitud_input)
            
        else:
            print("⚠️ Por favor, ingresa un número entero válido.")
            continue
            
        # Validar los límites permitidos de caracteres
        if longitud < 4:
            print("⚠️ La contraseña debe tener al menos 4 caracteres.")
            continue
        elif longitud > 128:
            print("⚠️ La contraseña no debe exceder 128 caracteres.")
            continue
            
        # Este bucle for es el encargado de repetir una acción tantas veces como el usuario (o el programa) haya definido en la variable longitud.
        for _ in range(longitud):
            # Toma la variable caracteres (que contiene letras, números y símbolos) y elige uno al azar.
            # El += es un operador de asignación compuesta (o de adición).
            # Sirve para sumarle algo a una variable y, al mismo tiempo, guardar el nuevo resultado en esa misma variable. 
            # Si la longitud es de 12, el bucle hará esto 12 veces, armando la contraseña caracter por caracter.
            contrasena += random.choice(caracteres)
            
        # \n: Da un salto de línea para que no quede todo amontonado.
        print(f"\n✓ Contraseña generada:")
        print(f"  {contrasena}")
        print(f"  Longitud: {longitud} caracteres")