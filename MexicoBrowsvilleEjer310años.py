import pandas as pd
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt

#Se le el csv de Fronteras, que contiene a US-Canada Border y a US-Mexico Border del año 1996 a febrero de 2020
#print('FRONTERAS')
fronteras = pd.read_csv('front2.csv')
#print(fronteras)
#print(fronteras.dtypes)


#Para convertir la fecha a formato de fecha (mm/dd/YYYY) mediante la función de pd.to_datetime
fronteras['Date'] = pd.to_datetime(fronteras['Date'],format='%m/%d/%Y')
#print(fronteras.dtypes)

#Se seleccionan los datos que sean del año 2010 al 2019,  tengan frontera US-Mexico Border y Port Name sea Brownsville  
print('FRONTERAS - US-Mexico Border - Brownsville - Año: 2000 al 2019')
border = fronteras["Border"] == "US-Mexico Border"
fecha = fronteras["Date"].dt.strftime("%Y").isin(["2010","2011","2012","2013","2014","2015","2016","2017","2018","2019"])
brow = fronteras["Port Name"] == "Brownsville"
ejer1 = fronteras[border & fecha & brow]
print(ejer1)

#Se muestran los detalles de los datos con la función de describ
desejer1 = ejer1.describe()
print(desejer1)

#Se calcula el centro de rango usando las funciones max() y min()
print("Centro del rango")
rango = ejer1["Value"].max() - ejer1["Value"].min()
centrorango = rango/2
print(centrorango)

#Se calcula la media recortada al 10% mediante la funcion stats.trim_mean
from scipy import stats
print("Media recortada al 10%")
merecord = stats.trim_mean(ejer1["Value"],0.10)
print(merecord)

dOrder=sorted(ejer1)

n=len(dOrder)
middle=n/2

#Función para calcular la mediana
mediana=ejer1["Value"].median()
print("Mediana: ", mediana)
print(" ")

#eje x, detalle del paso del tiempo
x=ejer1['Date']
#eje y, valores
y=ejer1['Value']
#Función para graficar en línea
plt.plot(x,y)
#plt.show()

#Se guarda la grafica como imagen con formato png, pero si se desa guardar
#se debe comentar plot.show()
#plt.savefig('MexBrownsville2010-2019.png')




