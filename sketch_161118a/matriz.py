from fichas import *
from Victoria import *

#Clase matriz
#crea los componentes basicos del campo 
class matriz:
    def __init__(self):
        self.tamano = 50
        self.Phorizontal = height/ 6
        self.Pvertical = width/4
        self.Campo = []
        horizontal = self.Phorizontal
        for Filas in range(6):
            vertical = self.Pvertical
            horizontal += self.tamano +5
            self.Campo.append([])
            for Columnas in range(6):
                if Columnas == 3:
                    vertical += self.tamano        
                self.Campo[Filas].append(fichas(vertical,horizontal ,self.tamano,self.tamano))
                vertical += self.tamano + 5
            if Filas == 2:
                horizontal += self.tamano
                
   #funcion display 
   #muestra en pantalla los objetos que se encuentran dentro de la matriz
    def display(self):
        stroke(100,100,100)
        fill(197,197,197)
        for Filas in range(6):
            for Columnas in range(6):
                self.Campo[Filas][Columnas].display()
    
    #Funcion ponerFicha
    #Coloca una ficha en la posicion de la matriz indicada
    #entradas: "x" y "y" posiciones de la matriz, y turno del jugador
    #salida: true si la jugada es posible y false si no puede ser realizada
    def ponerFicha(self,x,y,turno):
        for Filas in range(6):
            for Columnas in range(6):
                if self.Campo[Filas][Columnas].valido(x,y,turno):
                    return True
        return False
    
    #Funcion Nmatriz
    #Entradas: Posicion de Inicial y final de las filas y columnas y donde se va a mover
    #Salidas: Modifica la matriz original usando los datos que recibe
    def Nmatriz(self,FilaI,FilaF,ColuI,ColuF,Mover):
        nMatriz = []
        FilaN = 0
        for Fila in range(FilaI,FilaF):
            nMatriz.append([])
            for Columna in range(ColuI,ColuF):
                nMatriz[FilaN].append(self.Campo[Fila][Columna].colorF)
            FilaN += 1
        if Mover == "d":
            nMatriz = self.RotarD(nMatriz)
        else:
            nMatriz = self.RotarI(nMatriz)
        self.CambiarMatriz(nMatriz,FilaI,FilaF,ColuI,ColuF)
    
    #Funcion RotaD
    #entrada: Matriz de 3x3
    #salida: Matriz girada a la derecha 
    def RotarD(self,Matriz):
        Matriz = Matriz[::-1]
        nMatriz  = []
        for Fila in range(3):
            nMatriz.append([])
            for Columnas in range(3):
                nMatriz[Fila].append(Matriz[Columnas][Fila])
        return nMatriz
    
    #Funcion RotaI
    #entrada: Matriz de 3x3
    #salida: Matriz girada a la izquierda
    def RotarI(self,Matriz):
        con = 0
        nMatriz  = []
        for i in Matriz:
            Matriz[con] = i[::-1]
            con+=1
        for Fila in range(3):
            nMatriz.append([])
            for Columnas in range(3):
                nMatriz[Fila].append(Matriz[Columnas][Fila])
        return nMatriz
    
   
    #Funcion CambiarMatriz
    #entrada: Matriz de 3x3,posiciones de inicio y final de las filas y columnas        
    def CambiarMatriz(self,Matriz,FilaI,FilaF,ColuI,ColuF):
        FilaN = 0
        for Fila in range(FilaI,FilaF):
            ColumnaN = 0
            for Columna in range(ColuI,ColuF):
                self.Campo[Fila][Columna].colorF = Matriz[FilaN][ColumnaN]
                ColumnaN += 1
            FilaN += 1 
    
    #funcion victoria 
    #salida: Retorna True si un jugador gano o False si aun no se gana la partida    
    def victoria(self):
        if ganeV(self.Campo):
            return True
        if ganeH(self.Campo):
            return True
        if ganeDiagI(self.Campo):
            return True
        if ganeDiagD(self.Campo):
            return True
        if ganeDiagDsub2(self.Campo):
            return True
        if ganeDiagDsub3(self.Campo):
            return True
        if ganeDiagIsub3(self.Campo):
            return True
        if ganeDiagIsub2(self.Campo): 
            return True
        return False
    
    #funcion empate
    #salida: Retorna True si todas los campos estan ocupados  
    def empate(self):
        for c in range(6):
            for p in range(6):
                if self.Campo[c][p].colorF == 2:
                    return False
        return True 
    
    #Funcion jugada valida
    #entradas: "x" y "y" posiciones de la matriz 
    #salida: retorna True si la jugada se puede realizar y false si no es posible
    def jugadaValida(self,x,y):
        for Filas in range(6):
            for Columnas in range(6):
                if self.Campo[Filas][Columnas].JugadaValida(x,y):
                    return True
        return False

        
            