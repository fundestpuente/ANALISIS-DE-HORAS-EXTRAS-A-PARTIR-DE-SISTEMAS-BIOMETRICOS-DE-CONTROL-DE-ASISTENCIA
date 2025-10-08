import pandas as pd
from IPython.display import display

def cargar_datos(path):
  """
  Función para cargar datos desde un archivo CSV o Excel.imp
  Input:
    path (str): Ruta del archivo a cargar
  Output:
    data (DataFrame): Datos cargados en un DataFrame de pandas.
  """
  try:
    
