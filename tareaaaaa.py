import numpy as np
import pandas as pd
import pickle
import matplotlib.pyplot as plt

#Estabelcemos el data frame para la fecha
print("\nPrograma de perros con Pandas :D\n")
fronteras = pd.read_csv('frontera.csv')
fronteras["Date"] = pd.to_datetime(fronteras["Date"], format="%m/%d/%Y")
es_2019 = fronteras["Date"].dt.strftime("%Y") == "2019"
#-------------------------------------------------------------------

#Establecemos el data frame de que estamos en la frontera de Canada
es_Canada = fronteras["Border"] == "US-Canada Border"
frontCanada = fronteras[es_Canada & es_2019]
#------------------------------------------------------------------

#Creamos el data frame con ubicarnos en canada y sea el año 2019
DataFrameCanada = pd.DataFrame(frontCanada)
cols_to_subset = ["Port Name", "State", "Date", "Measure", "Value"]
filtroFinal = DataFrameCanada[cols_to_subset]
DataFrameFiltro = pd.DataFrame(filtroFinal)
#print(filtroFinal)
#--------------------------------------------------------------------

#Creamos las condiciones de PVP y PV
es_PerVehPas = fronteras["Measure"] == "Personal Vehicle Passengers"
es_PerVeh = fronteras["Measure"] == "Personal Vehicles"
#--------------------------------------------------------------------

#Creamos las condiciones de PD
es_PD = fronteras["Measure"] == "Pedestrians"


#---------------------------------------------------------------------


#Creación de la ubicación de los estados
es_AK = fronteras["State"] == "AK"



#--------------------------------------------------------------------

#Creamos el DataFrame de AKPVP, AKPV Para el ESTADO DE AK
frameDePerAKPV = fronteras[es_2019 & es_Canada & es_PerVeh & es_AK]
DataFrameAKPV = pd.DataFrame(frameDePerAKPV)
#print(frameDePerAKPV)
frameDePerAKPVP = fronteras[es_2019 & es_Canada & es_PerVehPas & es_AK]
DataFrameAKPVP = pd.DataFrame(frameDePerAKPVP)
#print(frameDePerAKPVP)






#-------------------------------------------------------------------------

#Cremos el data frame de Pedestrians
frameDeAKPD = fronteras[es_2019 & es_Canada & es_PD  & es_AK]
DataFrameAKPD = pd.DataFrame(frameDeAKPD)
#print(DataFrameAKPD)




#--------------------------------------------------------------------------


#Gráfica de lineas por estado sin detalles de puertas, que muestra el movimiento de Personal Vehicles
#xAKPD=DataFrameAKPD['Date']
#yAKPD=DataFrameAKPD['Value']
#plt.plot(xAKPD,yAKPD)
#plt.show()




#-------------------------------------------------------------------------------------------------------

#Hacer Gráfica de puntos que muestre el comportamiento de "Pedestrians". Que sea una gráfica
#por cada estado y con detalle de puertas en la horizontal
#xAKPV=frameDePerAKPV['Port Name']
#yAKPV=frameDePerAKPV['Value']
#plt.scatter(xAKPV,yAKPV)
#plt.show()



#--------------------------------------------------------------------------------------------------------


#Creamos  los data frames con la condición de PV y PVP Por estado
akPV= DataFrameAKPV[DataFrameAKPV['Measure']=='Personal Vehicles']
akPVP= DataFrameAKPVP[DataFrameAKPVP['Measure']=='Personal Vehicle Passengers']
dfakPV= pd.DataFrame(akPV)
dfakPVP= pd.DataFrame(akPVP)
sumaAKPV  = dfakPV.groupby('Port Name')['Value'].sum()
sumaAKPVP = dfakPVP.groupby('Port Name')['Value'].sum()
dfsumaAKPV= pd.DataFrame(sumaAKPV)
dfsumaAKPVP= pd.DataFrame(sumaAKPVP)






#print(dfsumaAKPV)
#print(dfsumaAKPVP)
#---------------------------------------------------------------------------------------


#Unimos PV y PVP POR CADA ESTADO dentro de un mismo data frame
JuntosAK= pd.merge(dfsumaAKPV,dfsumaAKPVP,on='Port Name')
dfJuntosAK=pd.DataFrame(JuntosAK)



#print(dfJuntosAK)
#-----------------------------------------------------------------------------------------


#Graficamos por estado las dos barras en una gráfica
#JuntosAKx = dfJuntosAK[['Value_x','Value_y']]
#JuntosAKx.plot.bar()
#plt.show()


#-----------------------------------------------------------------------------------------


#Histograma de Buss pasengers para todos los estados

es_BP = fronteras["Measure"] == "Bus Passengers"
frameDeBP = fronteras[es_2019 & es_Canada & es_BP ]
DataFrameBP = pd.DataFrame(frameDeBP)
#print(DataFrameBP)

#xBP=DataFrameBP['Value']
#yBP=DataFrameBP[]
#plt.hist(xBP)
#plt.show()

#DataFrameBP['Value'].plot.hist()
#plt.show()