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
