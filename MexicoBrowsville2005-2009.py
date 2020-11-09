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

#EJERCICIO - 2 -

#------------------------------------------------------------------------------------------------------------

#                                              2005 - 2009

#------------------------------------------------------------------------------------------------------------

#Se seleccionan los datos que sean del año 2005 al 2009,  tengan frontera US-Mexico Border y Port Name sea Brownsville

#mes x

#Se seleccionan los datos que correspondan con Border = US-Mexico Border
border1 = fronteras["Border"] == "US-Mexico Border"
#Se seleccionan los datos que correspondan con los años 2005, 2006, 2007, 2008, 2009
fecha1 = fronteras["Date"].dt.strftime("%Y").isin(["2005","2006","2007","2008","2009"])
#Se seleccionan los datos que correspondan con Port Name = Brownsville
brow1 = fronteras["Port Name"] == "Brownsville"
#Se seleccionan los datos que correspondan con  Measure = Pedestrians 
ped1 = fronteras["Measure"] == "Pedestrians"
#Se seleccionan los datos que correspondan con el mes x, según sea el mes que se desean los datos
mes1 = fronteras["Date"].dt.strftime("%m") == "01"
#Se unen en la variable ejer21 todos los datos seleccionados anteriormente
ejer21 = fronteras[border1 & fecha1 & brow1 & ped1 & mes1]
print(ejer21)
#Mediante la función describe() podemos obtener la media
des1 = ejer21.describe()
print(des1)

#eje x, detalle del paso del tiempo 
x1=ejer21['Date']
#eje y, valores
y1=ejer21['Value']
#Función para graficar en línea
plt.plot(x1,y1)
#plt.show()

#Se guarda la grafica como imagen con formato png, pero si se desa guardar
#se debe comentar plot.show()
plt.savefig('2005-2009-01.png')















