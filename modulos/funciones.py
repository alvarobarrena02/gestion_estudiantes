def ver_menu():
    print('------ GESTIÓN DE NOTAS Y ESTUDIANTES ------')
    print('0. AÑADIR ESTUDIANTE')
    print('1. AGREGAR NOTA')
    print('2. CALCULAR PROMEDIO')
    print('3. MOSTRAR NOTAS')
    print('4. ACTUALIZAR NOTA')
    print('5. ELIMINAR NOTA')
    print('6. SALIR')

def limpiar_consola():
    import os
    if os.name == "nt": # Windows
        os.system("cls")
    else: # MacOS y Linux
        os.system("clear")