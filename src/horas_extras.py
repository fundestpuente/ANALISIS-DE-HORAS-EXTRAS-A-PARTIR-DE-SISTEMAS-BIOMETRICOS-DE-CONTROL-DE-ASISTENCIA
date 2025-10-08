import pandas as pd
from datetime import datetime

def horas_extras(totDATA, mes=None, feriados_csv=None):

    #Leer feriados desde CSV si se proporciona
    if feriados_csv:
        try:
            df_feriados = pd.read_csv(feriados_csv)
            if 'Fecha' in df_feriados.columns:
                raise ValueError("El archivo de feriados debe contener una columna 'Fecha'")
            holydays = df_feriados['Fecha'].astype(str).tolist()
            print(f"{len(holydays)} feriados cargados desde {feriados_csv}")
        except Exception as e:
            print(f"Error al leer el archivo de feriados: {e}")
            holydays = []
    else:
        # Si no se proprociona CSV, preguntar manualmente
        holydays = []
        is_holiday = input(f"¿Hay feriados en el mes {mes}? (S/N): ").strip().upper()
        if is_holiday == 'S':
            how_many = int(input("Ingrese el número de feriados en el mes: "))
            for i in range(how_many):
                holyi = input(f"Ingrese la fecha del feriado {i+1} (formato DD/MM/AAAA): ").strip()
                holydays.append(holyi)
        else:
            print("No se registraron feriados manuales.")

    #Identificar domingos y feriados (Horas extras 100%)
    sunday_holy = []
    for i in range(len(totDATA["Fecha"])):
        date_string = str(totDATA.loc[i, "Fecha"])
        try:
            date_object = datetime.strptime(date_string, "%d/%m/%Y")
        except ValueError:
            raise ValueError(f"Formato de fecha incorrecto: {date_string}. Debe ser DD/MM/AAAA")
        
        if date_object.weekday() == 6 or date_string in holydays:
            sunday_holy.append(1)
        else:
            sunday_holy.append(0)
        
    #Identificar sábados (Horas extras 50%)
    saturdays = []
    for i in range(len(totDATA["Fecha"])):
        date_string = str(totDATA.loc[i, "Fecha"])
        date_object = datetime.strptime(date_string, "%d/%m/%Y")
        saturdays.append(i if date_object.weekday() == 5 else 0)

    #Añadir columnas al dataframe
    totDATA["Sabado"] = saturdays
    totDATA["Domingo/Feriado"] = sunday_holy

    #Calculo de horas extras totales por empleado
    min50 = []
    min100 = []
    for i in range(len(totDATA["Fecha"])):

        #Dia normal de lunes a viernes
        if (totDATA.loc[i, "Sabado"]== 0 and (totDATA.loc[i, "Domingo/Feriado"])==0):
            extra = totDATA.loc[i, "Minutos totales por dia"]
            min50.append(extra)
            min100.append(int(0))
        
        #Sábado
        elif totDATA.loc[i, "Sabado"]==1:
            extra = totDATA.loc[i, "Minutos totales por dia"]
            min50.append(extra)
            min100.append(int(0))

        #Dia especial (Domingo o Feriado)
        elif totDATA.loc[i, "Domingo/Feriado"]:
            extra = totDATA.loc[i, "Minutos totales por dia"]
            min50.append(extra)
            min100.append(int(0))

    totDATA["Minutos extra 50%"] = min50
    totDATA["Minutos extra 100%"] = min100