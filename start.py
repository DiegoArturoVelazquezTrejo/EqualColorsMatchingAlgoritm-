from CuerpoAlgoritmo import AnalisisCentroide
from CuerpoAlgoritmo import convertir_dataNoNumerico
import pandas as pd
import numpy as np
from recursos import generarCadena

print "************************** CHROMA TWINS **************************\n"

df = pd.read_csv('Data.csv')

print "\n*****************Data Frame*****************\n"
print df

correos = df['Correo']
df.drop(['Correo'],1,inplace = True)
df.drop(['Marca temporal'],1,inplace = True)
df = convertir_dataNoNumerico(df)


X = np.array(df)


colores = ["Red","Blue","Green","Yellow","Black","Orange", "Pink","Purple", "Coral","Aqua","VerdeLima", "White", "Gold"]
kmeans = AnalisisCentroide(13, colores)
kmeans.entrenar(X)
print "************************************Entrenamiento Completado***********************************"


#Este arreglo contiene las predicciones para cada dato del dataframe
print "\n*****************Asignacion de grupos*****************\n"
predicciones = []
for i in range(0,len(X)):
    predicciones.append(kmeans.predecir(X[i]))

print "\n*****************Numero de elementos por grupo*****************\n"
#Este ciclo nos dira cuantos elementos hay en cada grupo de colores
for i in range(0,len(kmeans.matrizElementos)):
    print "\n" +colores[i] + " tiene elementos: " + str(len(kmeans.matrizElementos[i]))

#Imprimiendo los resultados para cada elemento
for i in range(0, len(predicciones)):
    print str(correos[i]) + " Pertenece al grupo: " + (predicciones[i])


#Guardando coordenadas de los grupos
coordenadas = []
for i in range(0, len(kmeans.arrayConClusters)):
    coordenadas.append(kmeans.arrayConClusters[i].coordenadas)
clusters = []
for i in range(0, len(kmeans.arrayConClusters)):
    clusters.append(kmeans.arrayConClusters[i].color)


#Guardar los datos finales en un excel
decision = raw_input('Teclea y para generar archivo csv')
if(decision == 'y' or decision =='Y'):
    dataFrameFinal = pd.DataFrame({'Nombres': correos, 'Prediccion': predicciones})
    dataFrameCoordenadas = pd.DataFrame({ 'Centroides': coordenadas, 'Colores': clusters})
    dataFrameFinal.to_csv('Respuestas.csv', header=False, index=False)
    dataFrameCoordenadas.to_csv('Centroides.csv', header = False, index = False)
