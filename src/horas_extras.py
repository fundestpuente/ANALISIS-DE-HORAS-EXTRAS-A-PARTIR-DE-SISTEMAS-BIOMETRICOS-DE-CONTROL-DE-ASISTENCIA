import pandas as pd
from datetime import datetime

def horas_extras(totDATA, mes=None, feriados_csv=None):
    """
    Función para calcular horas extras considerando sábados, domingos y feriados.
    Input:
        totDATA (DataFrame): DataFrame con el tiempo total trabajado por empleado por día.
        mes (str, optional): Nombre del mes para el cual se calculan las horas extras. Si no se proporciona, se solicitará al usuario.
        feriados_csv (str, optional): Ruta a un archivo CSV que contiene las fechas de los feriados. Si no se proporciona, se solicitará al usuario.
    Output:
        totDATA (DataFrame): DataFrame actualizado con columnas para horas extras al 50% y 100%.
    """

    # Leer feriados desde CSV si se proporciona
    if feriados_csv:
        try:
            df_feriados = pd.read_csv(feriados_csv)
            if "Fecha" not in df_feriados.columns:
                raise ValueError("El archivo CSV debe contener una columna llamada 'Fecha'.")
            holydays = df_feriados["Fecha"].astype(str).tolist()
            print(f"{len(holydays)} feriados cargados desde {feriados_csv}")
        except Exception as e:
            print(f"Error al leer {feriados_csv}: {e}")
            holydays = []
    else:
        # Si no se proporciona CSV, preguntar manualmente
        holydays = []
        is_holiday = input(f"¿Hay feriados en este el mes de {mes}? (S/N): ").strip().upper()
        if is_holiday == "S":
            how_many = int(input("Ingrese el número de feriados: "))
            for i in range(how_many):
                holyi = input(f"Ingrese la fecha del feriado {i+1} (DD/MM/YYYY): ").strip()
                holydays.append(holyi)
        else:
            print("No se registraron feriados manuales.")

    # Identificar domingos y feriados (Horas 100%)
    sunday_holy = []
    for i in range(len(totDATA["Fecha"])):
        date_string = str(totDATA.loc[i, "Fecha"])
        try:
            date_object = datetime.strptime(date_string, "%d/%m/%Y")
        except ValueError:
            raise ValueError(f"Formato de fecha inválido: {date_string}. Use DD/MM/YYYY.")

        if date_object.weekday() == 6 or date_string in holydays:
            sunday_holy.append(1)
        else:
            sunday_holy.append(0)

    # Identificar sábados (Horas 50%)
    saturdays = []
    for i in range(len(totDATA["Fecha"])):
        date_string = str(totDATA.loc[i, "Fecha"])
        date_object = datetime.strptime(date_string, "%d/%m/%Y")
        saturdays.append(1 if date_object.weekday() == 5 else 0)

    # Añadir columnas al DataFrame
    totDATA["Sábado"] = saturdays
    totDATA["Domingo/Feriado"] = sunday_holy

    print("Cálculo de horas extras completado.")

    #Minutos extra 50% Y 100% por dia y por trabajador
    min50 = []
    min100 = []
    for i in range(len(totDATA["Fecha"])):
        #Dia normal de lunes a viernes
        if (totDATA.loc[i, "Sábado"] == 0) and (totDATA.loc[i, "Domingo/Feriado"] == 0):
            extra = totDATA.loc[i, "Minutos totales por dia"] - 480
            min50.append(extra)
            min100.append(int(0))
        #Sábado
        elif totDATA.loc[i, "Sábado"] == 1:
            extra = totDATA.loc[i, "Minutos totales por dia"]
            min50.append(extra)
            min100.append(int(0))
        #Dia especial (Domingo o feriado)
        elif totDATA.loc[i, "Domingo/Feriado"]:
            extra = totDATA.loc[i, "Minutos totales por dia"]
            min100.append(int(extra))
            min50.append(int(0))

    totDATA["Minutos extra 50%"] = min50
    totDATA["Minutos extra 100%"] = min100