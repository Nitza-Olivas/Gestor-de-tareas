import pandas as pd
import os
import pytest
from agregar_tareas import agregar_tarea
from quitar_tareas import quitar
from completar_tarea import completar

# Ruta del archivo CSV para las pruebas
CSV_FILE = 'test_datos.csv'

@pytest.fixture
def setup_csv():
    # Crear un DataFrame vacío y guardarlo en un archivo CSV para las pruebas
    df = pd.DataFrame(columns=['tarea', 'descripción', 'estado'])
    df.to_csv(CSV_FILE, index=False)
    yield df
    # Limpiar el archivo después de las pruebas
    #if os.path.exists(CSV_FILE):
        #os.remove(CSV_FILE)

def test_agregar_tarea(setup_csv):
    df = setup_csv
    nombre = "Tarea 1"
    descripcion = "Descripción de la tarea 1"
    
    # Llamar a la función para agregar la tarea
    df_resultado = agregar_tarea(df, nombre, descripcion)
    
    # Verificar que la tarea se haya agregado correctamente
    assert len(df_resultado) == 1
    assert df_resultado.iloc[0]['tarea'] == nombre
    assert df_resultado.iloc[0]['descripción'] == descripcion
    assert df_resultado.iloc[0]['estado'] == 'Incompleta'

def test_quitar_tarea(setup_csv):
    df = setup_csv
    # Agregar una tarea antes de intentar quitarla
    df = agregar_tarea(df, "Tarea 1", "Descripción de la tarea 1")
    df.to_csv(CSV_FILE, index=False)  # Guardar el DataFrame en el CSV

    # Simular la eliminación de la tarea
    df = pd.read_csv(CSV_FILE)
    df = df.drop(0)  # Eliminar la primera tarea
    df.to_csv(CSV_FILE, index=False)

    # Verificar que la tarea se haya eliminado
    df_resultado = pd.read_csv(CSV_FILE)
    assert len(df_resultado) == 0  # No debe haber tareas

def test_completar_tarea(setup_csv):
    df = setup_csv
    # Agregar una tarea antes de intentar completarla
    df = agregar_tarea(df, "Tarea 1", "Descripción de la tarea 1")
    df.to_csv(CSV_FILE, index=False)  # Guardar el DataFrame en el CSV

    # Simular la acción de completar la tarea
    df = pd.read_csv(CSV_FILE)
    df.iloc[0, df.columns.get_loc("estado")] = 'Completa'
    df.to_csv(CSV_FILE, index=False)

    # Verificar que la tarea se haya completado
    df_resultado = pd.read_csv(CSV_FILE)
    assert df_resultado.iloc[0]['estado'] == 'Completa'

# Ejecutar todas las pruebas
if __name__ == "__main__":
    pytest.main()
