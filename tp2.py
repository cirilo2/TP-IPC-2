""" >>>> NO TOCAR ESTE CÓDIGO >>>> """

import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime


def str2datetime(date, fmt="%Y-%m-%d"):
    """Convierte una cadena (o secuencia de cadenas) a tipo datetime (o secuencia de datetimes).

    ENTRADAS:
        date (str ó secuencia de str): fechas a convertir.
        fmt (str, opcional): formato de fecha (ver documentación de biblioteca datetime).
    SALIDAS:
        output (datetime ó secuencia de datetime): fechas convertidas a datetime.
    EJEMPLOS:
    >>>> date = str2datetime('2022-10-24')
    >>>> print(date.year, date.month, date.day)

    >>>> date = str2datetime(['2022-10-24', '2022-10-23', '2022-10-22'])
    >>>> print(len(date))"""
    if isinstance(date, str):
        return datetime.strptime(date, fmt)
    elif isinstance(date, (list, np.ndarray)):
        output = []
        for d in date:
            output.append(datetime.strptime(d, fmt))
        if isinstance(date, np.ndarray):
            output = np.array(output)
        return output


def datetime2str(date, fmt="%Y-%m-%d"):
    """Convierte un datetime (o secuencia de datetimes) a tipo str (o secuencia de str).

    ENTRADAS:
        date (datetime ó secuencia de datetime): fechas a convertir.
        fmt (str, opcional): formato de fecha (ver documentación de biblioteca datetime).
    SALIDAS:
        output (str ó secuencia de str): fechas convertidas a cadenas.
    EJEMPLOS:
    >>>> date_str = '2022-10-24'
    >>>> date = str2datetime(date_str)
    >>>> print(datetime2str(date) == date_str)"""
    if isinstance(date, datetime):
        return date.strftime(fmt)
    elif isinstance(date, (list, np.ndarray)):
        output = []
        for d in date:
            output.append(d.strftime(fmt))
        if isinstance(date, np.ndarray):
            output = np.array(output)
        return output


""" >>>> DEFINAN SUS FUNCIONES A PARTIR DE AQUÍ >>>> """
#Funcion 1 
# Entrada: Ruta hacia un archivo 
# Salida: Diccionario con informacion del archivo 
def read_file (archivo):
    dic = {}
    with open (archivo, 'r') as file: 
        f = file.readline().sptrip().split(",")
        dic = read_file("bolsa.csv") 
        for valor in f:
            dic[valor] = []    
        for line in file:
            line = line.strip().split(',')
            for index, value in enumerate(line):
                if index == 0:
                    dic[f[index]].append(str2datetime(value))
                else:
                    dic[f[index]].append(float(value))
    return dic

diccionario1 = read_file("bolsa.csv")
date = diccionario1["Date"]

#Funcion 2
# Lo que buscamos hacer cn esta funcion fue, calcular el precio promedio mes a mes, devolviendo dos secuencias, una con la fecha del primer dia de cada mes, y la segunda con ls precios promedios.
# Entrada: Accion y diccionario con la informacion del archivo creada en la funcion1 
# Salida: Dos secuencias con la misma longitud: una con la fecha del primer dia de cada mes y la segunda con los precios promedios de ese mes. 
def monthly_average ():
    enero = []
    febrero = []
    marzo = []
    abril = []
    mayo = []
    junio = []
    julio = []
    agosto = []
    septiembre = []
    octubre = []
    noviembre = []
    diciembre = []
    meses = []
    fechas =[]

    for fecha in dic['Date']:
        mes = fecha.month
        if mes not in meses :
            fechas = append(mes)
            meses = append(fecha)








#Funcion 3
with open('monthly_average_SATL.csv', 'w') as file:
    '''
    Genera un archivo llamado monthly_average_SATL.csv, el cual tiene la primer fecha de cada mes, y el promedio de la accion SATL, en formato csv
    '''
    file.write("Date,SATL")
    fechas, promedios = monthly_average("SATL", diccionario1)
    for i in range(len(fechas)):
        file.write(f"{fechas[i]},{promedios[i]}\n")



#Funcion 4
# Entrada:
# Salida:
def max_gain(accion, dicionario, fecha_venta):

#Funcion 5
#Funcion 6
#Funcion 7

""" >>>> ESCRIBAN SU CÓDIGO A PARTIR DE AQUÍ >>>> """



