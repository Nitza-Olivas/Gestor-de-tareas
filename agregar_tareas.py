# Definimos la función agragar
import pandas as pd

# Función para agregar una tarea
def agregar_tarea(df, nombre, descripcion):
    nueva_fila = {'tarea': nombre, 'descripción': descripcion, 'estado': 'Incompleta'}
    df = df._append(nueva_fila, ignore_index=True)
    df.to_csv('datos.csv', index=False)
    return df

# Función que interactúa con el usuario para agregar una tarea
def agregar():
    # Leer las tareas desde el CSV
    df = pd.read_csv("datos.csv")
    
    if df.shape[0] <= 0:
        print("No tienes tareas guardadas")
    else:
        print(df)
    
    # Pedir al usuario el nombre y la descripción de la tarea
    while True:
        nombre = input("Introduce un nombre para la tarea que deseas agregar: ")
        print(f"Vas a agregar el nombre: {nombre}")
        while True:
            decision = input("¿Quieres continuar? si no quieres continuar, puedes reescribir el nombre (S/n): ")
            if decision.lower() == "s" or decision.lower() == "n" or decision == "":
                break
            else:
                print('Introduce "S" o "N"')
        if decision.lower() == "s" or decision == "":
            break
    
    while True:
        descripcion = input(f"Introduce una descripción para la tarea '{nombre}': ")
        print(f"Vas a agregar esta descripción: {descripcion} \nA la tarea: {nombre}")
        while True:
            decision = input("¿Quieres continuar? si no quieres continuar, puedes reescribir la descripción (S/n): ")
            if decision.lower() == "s" or decision.lower() == "n" or decision == "":
                break
            else:
                print('Introduce "S" o "N"')
        if decision.lower() == "s" or decision == "":
            break

    # Llamar a la función para agregar la tarea
    df = agregar_tarea(df, nombre, descripcion)
    print("Estas son todas tus tareas:")
    print(df)

    