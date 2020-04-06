#Clase ficha
#Recibe la posicion vertical, horizontal de la ficha y el tamano de la ficha
class fichas:
    def __init__(self,vertical,horizontal,Vtama,Htama):
        self.colorF = 2
        self.vertical= vertical
        self.horizontal= horizontal
        self.Vtama = Vtama
        self.Htama = Htama
        
    #Funcion ColorF
    #Retorna el color de la ficha
    def ColorF(self):
        return  self.colorF  
    
    #Funcion display
    #Displiega la ficha con el color que tenga 
    def display(self):
        self.Fcolor()
        ellipse(self.vertical,self.horizontal ,self.Vtama,self.Htama)
   
   #Funcion valido
   #Recibe las posisiones "x" y "y" de la matriz y el turno 
   #Coloca el color a la ficha dependiendo del turno de jugador
   #retorna true si encontro la ficha
    def valido(self,x,y,turno):
        if (self.vertical+self.Vtama/2 >= x and self.vertical-self.Vtama/2 <= x) and (self.horizontal+self.Htama/2 >= y and self.horizontal-self.Htama/2 <= y):
            if turno == 0:
                self.colorF = 0
            else:
                self.colorF = 1
            return True
    
    #Funcion JugadaValida
    #entradas: posicion "x" y "y" de la ficha
    #retorna false si el color es diferente 2(Que ya tenga una ficha) y que retorne True si el color de la ficha es 2(Que no tiene una ficha)
    def JugadaValida(self,x,y):
        if (self.vertical+self.Vtama/2 >= x and self.vertical-self.Vtama/2 <= x) and (self.horizontal+self.Htama/2 >= y and self.horizontal-self.Htama/2 <= y):
            if self.colorF != 2:
                return False
            else:
                return True
        return False
    
    #Funcion Fcolor
    #selecciona que color va a pintar la siguente ficha
    def Fcolor(self):
        if self.colorF == 0:
            noStroke()
            fill(255,255,255)
        if self.colorF == 1:
            noStroke()
            fill(0,0,0)
        
        if self.colorF == 2:
            stroke(0,70,150)
            fill(0,105,210)
        
            
        
        
        