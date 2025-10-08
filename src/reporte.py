import pandas as pd
from datetime import datetime

def val_anormales(totDATA):
    """
    Función para identificar y mostrar días con valores anormales en las horas trabajadas.
    
    """
    #Identificar valores anormales
    for i in range(len(totDATA["Minutos extra 50%"])):
        if totDATA.loc[i, "Minutos extra 50%"] < int(0):
            print("No se cumplió la con la jornada completa en el siguiente día: ")
            display(totDATA.loc[i])

def generar_reporte(totDATA, file_name = "reporte_horas_extras.csv"):
    listado = totDATA["Nombre"].unique()
    tot50 = [0 for k in range(len(listado))]
    tot100 = [0 for k in range(len(listado))]
    dias = [0 for k in range(len(listado))]
    for i in range(len(totDATA["Nombre"])):
        for j in range(len(listado)):
            if totDATA.loc[i, "Nombre"] == listado[j]
                tot50[j] += totDATA.loc[i, "Minutos extra 50%"]
                tot100[j] += totDATA.loc[i, "Minutos extra 100%"]
                dias[j] +=1
    reporte = pd.DataFrame({"Nombre": listado, "Total minutos extra 50%": tot50, "Total minutos extra 100%": tot100})
