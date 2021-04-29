#para generar los numeros enteros aleatorios
from random import randint
#creamos la clase
class Proceso:
    NoProceso=1 #variable de clase o estatica para identificar al proceso
    def __init__(self):
        self.No=Proceso.NoProceso
        Proceso.NoProceso=+1 #cada proceso tendra un numero con respecto a su creacion en este caso de uno en uno
        #encapsulamos la var tiempo para que no se tenga acceso a ella desde fuera y no sea modificada
        self.__tiempo = randint(4, 9) #tiempo de proceso será aleatorio entre 4 y 9
        self.siguiente = None

    def getTiempo(self): #obtener el tiempo o estado del proceso
        return self.__tiempo

    def restarTiempo(self): #Restar un tiempo al proceso; este se aplicara por ciclo
        self.__tiempo-=1