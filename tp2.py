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
#1 
# Esta funcion crea un diccionario con claves y valores a partir de un archivo csv. 
# Entrada: Ruta hacia un archivo csv
# Salida: Diccionario con informacion del archivo 

def read_file (archivo):
    with open (archivo, 'r') as file: 
        dic = {}
        f = file.readline().strip().split(",")
        #dic = read_file("bolsa.csv") 
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

# 2
# Lo que buscamos hacer cn esta funcion fue, calcular el precio promedio mes a mes, devolviendo dos secuencias, una con la fecha del primer dia de cada mes, y la segunda con ls precios promedios.
# Entrada: Nombre de la accion y diccionario con la informacion del archivo creada en la funcion1 
# Salida: Dos secuencias con la misma longitud: una con la fecha del primer dia de cada mes y la segunda con los precios promedios de ese mes. 

def monthly_average (nombreaccion, diccionario1):

# FECHA 
    meses = []
    fechas = []
    fechas = diccionario1['Date']
    for fecha in fechas:
        mes = fecha.month
        if mes not in meses:
            meses.append(fecha)
            fechas.append(mes)

    promedio_total = []
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

# CALCULANDO PROMEDIO 

    for i, fecha in enumerate(diccionario1['Date']):
        mes = fecha.month
        if mes == 1:
            enero.append(diccionario1[nombreaccion][i])
        elif mes == 2:
            febrero.append(diccionario1[nombreaccion][i])
        elif mes == 3:
            marzo.append(diccionario1[nombreaccion][i])
        elif mes == 4:
            abril.append(diccionario1[nombreaccion][i])
        elif mes == 5:
            mayo.append(diccionario1[nombreaccion][i])
        elif mes == 6:
            junio.append(diccionario1[nombreaccion][i])
        elif mes == 7:
            julio.append(diccionario1[nombreaccion][i])
        elif mes == 8:
            agosto.append(diccionario1[nombreaccion][i])
        elif mes == 9:
            septiembre.append(diccionario1[nombreaccion][i])
        elif mes == 10:
            octubre.append(diccionario1[nombreaccion][i])
        elif mes == 11:
            noviembre.append(diccionario1[nombreaccion][i])
        elif mes == 12:
            diciembre.append(diccionario1[nombreaccion][i])


    promedio1 = sum(enero) / len(enero)
    promedio2 = sum(febrero) / len(febrero)
    promedio3 = sum(marzo) / len(marzo)
    promedio4 = sum(abril) / len(abril)
    promedio5 = sum(mayo) / len(mayo)
    promedio6 = sum(junio) / len(junio)
    promedio7 = sum(julio) / len(julio)
    promedio8 = sum(agosto) / len(agosto)
    promedio9 = sum(septiembre) / len(septiembre)
    promedio10 = sum(octubre)/ len(octubre)
    promedio11 = sum(noviembre) / len(noviembre)
    promedio12 = sum(diciembre) / len(diciembre)
    promedio_total.append(promedio1)
    promedio_total.append(promedio2)
    promedio_total.append(promedio3)
    promedio_total.append(promedio4)
    promedio_total.append(promedio5)
    promedio_total.append(promedio6)
    promedio_total.append(promedio7)
    promedio_total.append(promedio8)
    promedio_total.append(promedio9)
    promedio_total.append(promedio10)
    promedio_total.append(promedio11) 
    promedio_total.append(promedio12) 
    return fechas, promedio_total 

prom_accion = monthly_average("SATL", diccionario1)


#3
with open('TP 2/monthly_average_SATL.csv', 'w', encoding="utf-8") as file:
    file.write("Date,SATL")
    fechas, promedios = monthly_average("SATL", diccionario1)
    for i in range(len(fechas)):
        file.write(f"{fechas[i]},{promedios[i]}\n")


#4
# La funcion busca la fecha de cmpra en el diccionario, la cual genero la mayor ganancia. 
# Entrada: nombre de una acción, el diccionario de datos y una fecha de venta. 
# Salida:fecha de compra (en el pasado) que hubiera generado la mayor ganancia. Retorno de la inversión.
# ganancia = (precio de venta - precio de compra) / precio de compra

def max_gain(nombreaccion, diccinario1, fecha_venta):
    fecha_venta = str2datetime(fecha_venta)
    valores = diccinario1[nombreaccion]
    ind = diccinario1["Date"].index(fecha_venta)
    precio_venta = valores[ind]
    precio_compra = precio_venta
    fecha = diccinario1["Date"][ind]
    for x in range(ind):
        if valores[x] < precio_compra:
            precio_compra = valores[x]
            fecha = diccinario1["Date"][x]
    ganancia = (precio_venta - precio_compra) / precio_compra
    return fecha, ganancia

def max_gain( accion, diccionario , fecha_venta):

    fechas = diccionario1["fecha"]
    precios = diccionario1[accion]
    fecha_compra = 0
    precio_compra = 0
    precio_venta = 0

    for fecha, pre in zip(fechas, precios):
        if precio_compra == 0:
            precio_compra = pre
            fecha_compra = fecha
        elif pre < precio_compra:
            precio_compra = pre
            fecha_compra = fecha
        else:
            precio_venta = pre
            break
    ganancia = (precio_venta - precio_compra)/precio_compra
    return fecha_compra , ganancia     

#5
# Entrada:
# Salida:
def report_max_gains(dic, fecha_venta):

    with open ("resumen_mejor_compra.txt","w")as f:
        for accion in dic.keys():
            if accion == "Date":
                continue
            f_compra , g_accion = max_gain(accion , dic , fecha_venta)
            if g_accion >= 0:
                f.write(f"{accion} genera una ganancia de {g_accion*100}% habiendo comprando en {f_compra.date()} y vendiendose en {fecha_venta}\n")
            else:
                file.write(f"{accion} genera una ganancia de {g_accion*100}% habiendo comprando en {f_compra.date()} y vendiendose en {fecha_venta}. La acción {accion} solo genera péridas \n")
report_max_gains(diccionario1, "2021-11-26")


#6

def plot_price(accion_grafica , diccionario , start = "2021-10-04" , end = "2022-06-01"):
    e = datetime2str(diccionario1)
    principio = e.index(start)
    final = e.index(end)
    print(final)
    eje_x = []
    eje_y = []
    todo_fecha = e[principio:final+1]
    todo_accion_grafica = diccionario1[accion_grafica][principio:final+1]
    for x in todo_fecha:
        eje_x.append(x)
    for y in todo_accion_grafica:
        eje_y.append(int(y))
    
    plt.plot(str2datetime(eje_x), eje_y, color = "m")
    plt.title(f'Acciones de {accion_grafica}')
    plt.xticks(rotation=65)
    plt.gcf().subplots_adjust(bottom=0.20)
    plt.xlabel('Fechas')
    plt.ylabel('Acciones')
    plt.show()
    plt.savefig(f"price_{accion_grafica}.png")

grafico = plt.savefig(f"plot_price.png")

return grafico

#7

#a

def monthly_average_bar_plot(accion,diccionaro1):
    fechas, promedio = monthly_average(accion, diccionario1)

    plt.figure()
    plt.rc('xtick', labelsize = 9)
    plt.bar(fechas, promedio)
    plt.xticks(rotation = 30)
    plt.xlabel("Fecha", horizontalalignment = 'right')
    plt.ylabel("Precio accion")
    plt.gfc().subplots_adjust(bottom = 0.15)

    grafico = plt.savefig(f"monthly_average_bar_plot_{accion}.png")
    return grafico

#b

def plot_max_gain(fecha_venta, diccionario1):
        l_ganancias = []
        l_acciones = []

        for accion in diccionario1.keys():
            if accion == "date":
                continue
            fecha , ganancia = max_gain(accion , diccionario1 , fecha_venta)
            l_ganancias.append(ganancia)
            l_acciones.append(accion)

        plt.figure()
        plt.bar(l_acciones, l_ganancias)

        plt.xlabel("ACIONES")
        plt.ylabel("GANANCIA MEJOR INVERSION")
        plt.gfc().subplots_adjust(bottom = 0.15)
        grafico = plt.savefig("max_gains.png")
        return grafico

""" >>>> ESCRIBAN SU CÓDIGO A PARTIR DE AQUÍ >>>> """



