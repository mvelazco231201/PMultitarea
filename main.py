# realice la simulación de un sistema operativo multitarea
#recibira procesos de forma aleatoria, estos procesos tendrán un valor de tiempo de ejecución
#también aleatorio y serán atendidos descontando un tiempo (ciclo) a la vez (de solo un proceso
#en cada ciclo de ejecución), de forma que en el siguiente ciclo se atenderá un tiempo del siguiente
#proceso y así sucesivamente hasta que los procesos vayan terminando y sean eliminados de la estructura.
#Simular 300 ciclos
#Solo se descuenta una unidad de tiempo de un proceso en cada ciclo.
#Probabilidad de llegada de un proceso nuevo es del 25% y la llegada de un proceso
#nuevo es independiente de la atención que se da a un proceso
#Tiempo o ciclos para cada proceso nuevo (aleatorio entre 4 y 9)
#Mostrar cuantos procesos se crearon
#Mostrar cuantos procesos se atendieron en su totalidad
#Indicar en cual ciclo se crea el primer proceso
from ListaCircular import ListaCircular
from Proceso import Proceso
from random import randint

multitarea = ListaCircular() #ceramos nuestra lista circular
ProcesoActual = None
procesosCreados = 0
primerProceso = 0
procesosAtendidos = 0
for i in range(0,300):#simulacion de 300 ciclos
    if (randint(1,100)<=25): #Probabilidad de llegada de un nuevo proceso del 25%
        newProceso = Proceso()
        multitarea.Agregar(newProceso) #el nuevo proceso se agrega a la lista
        procesosCreados += 1  # contamos cuantos procesos se han creado
        if(primerProceso == 0):
            primerProceso = i

    if not multitarea.ProcesoActual() is None: #porceso diferente de null?
        multitarea.ProcesoActual().restarTiempo()
        if multitarea.ProcesoActual().getTiempo() == 0:  # Si el proceso tiene una duracion de 0
            procesosAtendidos += 1  # contamos como atendido, finalizo su ciclo de vida
            multitarea.EliminarInicio()  # eliminamos ese proceso de la lista circular
        else:
            multitarea.Recorrer() #de lo contrario seguimos recorriendo la lista

print('Se crearon ' , procesosCreados , ' procesos')
print('Se atendieron ' , procesosAtendidos , 'procesos')
print('El primer proceso se creó en el ciclo ', primerProceso)