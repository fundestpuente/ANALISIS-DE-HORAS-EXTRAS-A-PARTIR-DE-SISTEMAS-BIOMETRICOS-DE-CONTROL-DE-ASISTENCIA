import pandas as pd
from datetime import datetime
import os
from IPython.display import display

def val_anormales(totDATA):
    """
    Función para identificar y mostrar días con valores anormales en las horas trabajadas.
    Input:
        totDATA (DataFrame): DataFrame con el tiempo total trabajado por empleado por día.
    Output:
        None: Muestra en pantalla los días con valores anormales.
    """
    #Identificar valores anormales
    for i in range(len(totDATA["Minutos extra 50%"])):
        if totDATA.loc[i, "Minutos extra 50%"] < int(0):
            print("No se cumplió la con la jornada completa en el siguiente día: ")
            display(totDATA.loc[i])

def generar_reporte(totDATA, file_name = "reporte_horas_extras.csv"):
    """
    Función para generar y guardar un reporte de horas extras por empleado.
    Input:
        totDATA (DataFrame): DataFrame con el tiempo total trabajado por empleado por día.
        file_name (str, optional): Nombre del archivo CSV donde se guardará el reporte. Por defecto es "reporte_horas_extras.csv".
    Output:
        None: Guarda el reporte en un archivo CSV.
    """
    #Sumar minutos 50% y 100% por separado
    #Contar dias asistidos por trabajador
    listado = totDATA["Nombre"].unique()
    tot50 = [0 for k in range(len(listado))]
    tot100 = [0 for k in range(len(listado))]
    dias = [0 for k in range(len(listado))]
    for i in range(len(totDATA["Nombre"])):
        for j in range(len(listado)):
            if totDATA.loc[i, "Nombre"] == listado[j]:
                tot50[j] += totDATA.loc[i, "Minutos extra 50%"]
                tot100[j] += totDATA.loc[i, "Minutos extra 100%"]
                dias[j] +=1
    reporte = pd.DataFrame({"Nombre": listado, "Total minutos extra 50%": tot50, "Total minutos extra 100%": tot100})
    #display(reporte)

    #Tranformar a horas (decimal format) y añadir días asistidos
    hor50 = []
    hor100 = []
    for i in range(len(reporte["Nombre"])):
        h5 = reporte.loc[i, "Total minutos extra 50%"] / int(60)
        hor50.append(h5)
        h1 = reporte.loc[i, "Total minutos extra 100%"] / int(60)
        hor100.append(h1)
    reporte_final = pd.DataFrame({"Nombre": listado, "Total horas extras 50%": hor50, "Total horas extras 100%": hor100, "Dias asistidos": dias})
    reporte_final.sort_values(by='Total horas extras 50%')

    # Create un directorio en donde se guardará el reporte
    dir_output = "output_data"
    if os.path.isdir(dir_output):
        print(f"Directorio '{dir_output}' ya existe.")
    else:
        print(f"Directorio '{dir_output}' ha sido creado.")
        os.mkdir(dir_output)
    # Gurdar el reporte
    try:
        reporte_final.to_csv(dir_output + "/" + file_name, index=False)
        print(f"Reporte guardado exitosamente en {dir_output + '/' + file_name}")
    except Exception as e:
        print(f"Error al guardar el reporte: {e}")

    return reporte_final