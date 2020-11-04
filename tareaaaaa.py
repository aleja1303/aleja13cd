import numpy as np
import pandas as pd
import pickle
import matplotlib.pyplot as plt

fronteras = pd.read_csv('frontera.csv')
fecha = fronteras["Date"].isin(["1/1/2019 00:00", "2/1/2019 00:00", "3/1/2019 00:00", "4/1/2019 00:00","5/1/2019 00:00","6/1/2019 00:00","7/1/2019 00:00","8/1/2019 00:00","9/1/2019 00:00","10/1/2019 00:00","11/1/2019 00:00","12/1/2019 00:00"])

es_Canada = fronteras["Border"] == "US-Canada Border"
frontCanada = fronteras[es_Canada & fecha]

DataFrameCanada = pd.DataFrame(frontCanada)
cols_to_subset = ["Port Name", "State", "Date", "Measure", "Value"]
filtroFinal = DataFrameCanada[cols_to_subset]
DataFrameFiltro = pd.DataFrame(filtroFinal)



print(filtroFinal)

es_PerVehPas = fronteras["Measure"] == "Personal Vehicle Passengers"
es_PerVeh = fronteras["Measure"] == "Personal Vehicles"

es_PD = fronteras["Measure"] == "Pedestrians"

es_AK = fronteras["State"] == "AK"



frameDePerAKPV = fronteras[fecha & es_Canada & es_PerVeh & es_AK]
DataFrameAKPV = pd.DataFrame(frameDePerAKPV)

print(frameDePerAKPV)

frameDePerAKPVP = fronteras[fecha & es_Canada & es_PerVehPas & es_AK]
DataFrameAKPVP = pd.DataFrame(frameDePerAKPVP)

print(frameDePerAKPVP)


frameDeAKPD = fronteras[fecha & es_Canada & es_PD  & es_AK]
DataFrameAKPD = pd.DataFrame(frameDeAKPD)

print(DataFrameAKPD)

#Gráfica de lineas por estado sin detalles de puertas, que muestra el movimiento de Personal Vehicles
#xAKPD=DataFrameAKPD['Date']
#yAKPD=DataFrameAKPD['Value']
#plt.plot(xAKPD,yAKPD)
#plt.show()


#Hacer Gráfica de puntos que muestre el comportamiento de "Pedestrians". Que sea una gráfica
#por cada estado y con detalle de puertas en la horizontal
#xAKPV=frameDePerAKPV['Port Name']
#yAKPV=frameDePerAKPV['Value']
#plt.scatter(xAKPV,yAKPV)
#plt.show()


akPV= DataFrameAKPV[DataFrameAKPV['Measure']=='Personal Vehicles']
akPVP= DataFrameAKPVP[DataFrameAKPVP['Measure']=='Personal Vehicle Passengers']
dfakPV= pd.DataFrame(akPV)
dfakPVP= pd.DataFrame(akPVP)
sumaAKPV  = dfakPV.groupby('Port Name')['Value'].sum()
sumaAKPVP = dfakPVP.groupby('Port Name')['Value'].sum()
dfsumaAKPV= pd.DataFrame(sumaAKPV)
dfsumaAKPVP= pd.DataFrame(sumaAKPVP)

print(dfsumaAKPV)
print(dfsumaAKPVP)

JuntosAK= pd.merge(dfsumaAKPV,dfsumaAKPVP,on='Port Name')
dfJuntosAK=pd.DataFrame(JuntosAK)

print(dfJuntosAK)

#Graficamos por estado las dos barras en una gráfica
JuntosAKx = dfJuntosAK[['Value_x','Value_y']]
JuntosAKx.plot.bar()
plt.show()

es_BP = fronteras["Measure"] == "Bus Passengers"
frameDeBP = fronteras[fecha & es_Canada & es_BP ]
DataFrameBP = pd.DataFrame(frameDeBP)
print(DataFrameBP)


xBP=DataFrameBP['Value']
yBP=DataFrameBP
plt.hist(xBP)
plt.show()

DataFrameBP['Value'].plot.hist()
plt.show()




