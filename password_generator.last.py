import random

# Mensaje de bienvenida en pantalla
print("=" * 50)
print("   GENERADOR DE CONTRASEÑAS")
print("=" * 50)

# Todos los caracteres disponibles guardados en una sola variable de texto
caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+-=[]{}|;:',.<>?/"

# Variable de control para mantener el programa corriendo
ejecutando = True

while ejecutando:
    # Mostrar el menú de opciones
    print("\n¿Qué deseas hacer?")
    print("  1. Generar contraseña aleatoria")
    print("  2. Ingresar contraseña manualmente")
    
    opcion = input("\nElige opción (1 o 2): ").strip()
    
    # Variable para almacenar la contraseña en cada intento
    contrasena = ""
    
    if opcion == "1":
        # --- OPCOIÓN 1: GENERAR CONTRASEÑA ---
        longitud_input = input("\n¿Cuántos caracteres quieres? (por defecto 12): ").strip()
        
        # Si el usuario presiona Enter sin escribir nada, se asigna 12
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
            
        # Bucle FOR para construir la contraseña carácter por carácter
        for _ in range(longitud):
            contrasena += random.choice(caracteres)
            
        print(f"\n✓ Contraseña generada:")
        print(f"  {contrasena}")
        print(f"  Longitud: {longitud} caracteres")
        
    elif opcion == "2":
        # --- OPCIÓN 2: INGRESO MANUAL ---
        contrasena = input("\nIngresa tu contraseña: ").strip()
        longitud = len(contrasena)
        
        # Validaciones de longitud para la contraseña manual
        if longitud == 0:
            print("⚠️ La contraseña no puede estar vacía.")
            continue
        elif longitud < 4:
            print("⚠️ La contraseña debe tener al menos 4 caracteres.")
            continue
        elif longitud > 128:
            print("⚠️ La contraseña no debe exceder 128 caracteres.")
            continue
            
        print(f"\n✓ Contraseña ingresada:")
        print(f"  {contrasena}")
        print(f"  Longitud: {longitud} caracteres")
        
    else:
        print("⚠️ Por favor, elige opción 1 o 2.")
        continue
        
    # Preguntar al usuario si desea realizar otra operación
    repetir = input("\n¿Generar o ingresar otra contraseña? (s/n): ").strip().lower()
    if repetir != 's' and repetir != 'si':
        print("\n¡Hasta luego! 👋")
        ejecutando = False