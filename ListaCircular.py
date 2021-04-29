from Proceso import Proceso
class ListaCircular:
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def Vacia(self):
        if(self.primero == None):
            return True #está vacía
        else:
            return False #no está vacía

    def Agregar(self, Proceso):  # ya funciona
        if (self.Vacia() == True):
            self.primero = Proceso  # El proceso va a ser el primero (25)
            temp = self.primero
            temp.siguiente = self.primero  # El siguiente del primero va a ser ese mismo 25->25
            self.ultimo = self.primero  # por lo que el ultimo es el primero (25)
        else:  # tenemos 25 queremos agregar 67
            self.ultimo.siguiente = Proceso  # el siguiente del ultimo va a ser el nuevo proceso 25->67
            Proceso.siguiente = self.primero  # el siguiente del nuevo será el primero (25) 67->25
            self.ultimo = Proceso  # por lo que el ultimo será el nuevo proceso (67)

    def EliminarInicio(self):
        if(self.Vacia() == True):
            print("Lista vacía")
        elif self.primero == self.ultimo: #si solo tenemos 25
            self.primero = self.ultimo = None #eso sería igual a none
        else: #en caso de que tengamos más elementos 25->67->89
            self.primero = self.primero.siguiente #el primero será el siguiente (67)
            self.ultimo.siguiente = self.primero #89 va a apuntar al 67

    def Recorrer(self):#ya funciona
        if(self.Vacia()==True):
            return print("lista vacía")
        else: #25->67->89->100
            actual=self.primero
            if(actual != None): #25!=Null? si
                while True:
                    print(actual.dato) #25
                    actual = actual.siguiente #actual sera igual al siguiente de 25 en este caso será (67)
                    if not (actual!=self.primero): #el ciclo continuara mientras no sea diferente del primero 67!=25? si, continua
                        break

    def EliminarProceso(self):
        if (self.Vacia() == True):
            print("Lista vacía") #imaginemos que ahora tenemos 4->5->4
        elif self.primero == self.ultimo:  # si solo tenemos 4
            while True:
                actual = self.primero = self.ultimo #actual tomará el valor de 4
                actual.restarTiempo() #se le restara un tiempo
                if not (actual is None):
                    break
                    actual is None
        else:  # en caso de que tengamos más elementos 4->5->4
            while True:
                actual = self.primero # actual tomará el valor de 4
                actual.restarTiempo()  # se le restara un tiempo
                actual = self.primero.siguiente #ahora actual será el siguiente (5)
                if not (actual is None): # 5 es null? no, continua ciclando
                    break
                    actual is None
                    return actual