import pandas as pd
from IPython.display import display

def cargar_datos(path):
    """
    Función para cargar datos desde un archivo CSV o Excel.imp
    Input:
        path (str): Ruta del archivo a cargar.
    Output:
        data (DataFrame): Datos cargados en un DataFrame de pandas.
    """
    try:
        # Tomar el tipo de archivo
        tipo_archivo = path.split(".")[-1]
        print(f"Cargando archivo de tipo: .{tipo_archivo}")

        # Cargar el archivo según su tipo
        if tipo_archivo == "xls" or tipo_archivo == "xlsx":
            data = pd.read_excel(path, engine='openpyxl')
        else:
            data = pd.read_csv(path, delimiter=",")

        print("Archivo cargado exitosamente!")
        return data
    except:
        print("No se pudo acceder al archivo. Verificar que el archivo sea de tipo .csv, y que el archivo se encuetra en la dirección proporcionada.")
        return None

def procesamiento(df, col_name = None):
	"""
	Función para procesar los datos de tiempo trabajado.
	Input:
		df (DataFrame): DataFrame con los datos originales.
	Output:
		totDATA (DataFrame): DataFrame con el tiempo total trabajando por empleado y por día
	"""

	# Renombremos las columnas
	if col_name is None:
		col_name = {"TiemInicio": "Inicio", "TiemFinal": "Final", "Fecha": "Diferencia", "????": "Date"}

	df.rename(columns=col_name, inplace=True)
	print("Columnas renombradas exitosamente")

	# Trnansformamos el tiempo en minutos

	Diff_min = []
	for i in df["Diferencia"]:
		(h,m) = i.split(":")
		min1 = int(h)*60
		min2 = int(m)
		min = min1 + min2
		Diff_min.append(min)
	df["Diferencia en minutos"] = Diff_min

	#Tabla de tiempo trabajado por empleado por día
	tiemposDia = []
	personas = []
	dias_trabajados = []

	i=0
	while i<len(df["Nombre"]):
		cont=0
		tiempo_dia = df.loc[i, "Diferencia en minutos"]
		personas.append(df.loc[i, "Nombre"])
		dias_trabajados.append(df.loc[i, "Date"])
		while ((i+cont+1)<len(df)) and (df.loc[i, "Date"] == df.loc[i+cont+1, "Date"]) and (df.loc[i, "Nombre"] == df.loc[i+cont+1, "Nombre"]):
			tiempo_dia += df.loc[i+cont+1, "Difetencia en minutos"]
			cont += 1
		tiemposDia.append(tiempo_dia)
		i += cont+1
	totData = pd.DataFrame({"Nombre": personas, "Minutos totales por dia": tiemposDia, "Fecha": dias_trabajados})

	return totData
