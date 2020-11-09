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

#Se seleccionan los datos que sean del año 2000 al 2019,  tengan frontera US-Mexico Border y Port Name sea Brownsville  
print('FRONTERAS - US-Mexico Border - Brownsville - Año: 2000 al 2019')
border = fronteras["Border"] == "US-Mexico Border"
fecha = fronteras["Date"].dt.strftime("%Y").isin(["2000","2001","2002","2003","2004","2005","2006","2007","2008","2009","2010","2011","2012","2013","2014","2015","2016","2017","2018","2019"])
brow = fronteras["Port Name"] == "Brownsville"
ejer1 = fronteras[border & fecha & brow]
print(ejer1)

desejer1 = ejer1.describe()
print(desejer1)

#eje x, detalle del paso del tiempo 
x=ejer1['Date']
#eje y, valores
y=ejer1['Value']
#Función para graficar en línea
plt.plot(x,y)
#plt.show()

#Se guarda la grafica como imagen con formato png, pero si se desa guardar
#se debe comentar plot.show()
plt.savefig('MexBrownsville2000-2019.png')
