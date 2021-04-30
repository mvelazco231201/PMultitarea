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

    def Recorrer(self):
        if (self.Vacia() == True):
            return print("lista vacía")
        else:  # 4->5->6
            self.primero = self.primero.siguiente #inicialmente el primero es 4 por lo que ahora el primero será igual a 5
            self.ultimo = self.ultimo.siguiente #y el ultimo será 4, ya que anteriormente el 6 era el ultimo

    def ProcesoActual(self):
        return self.primero
