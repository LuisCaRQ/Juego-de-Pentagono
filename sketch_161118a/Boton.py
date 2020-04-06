#Clase boton
#Recibe el texto,las cordenadas del boton(x,y) y el ancho y alto de este
class Boton:
    def __init__(self, texto,x,y,ancho,alto):
        self.texto=texto
        self.x=x
        self.y=y
        self.ancho=ancho
        self.alto=alto
        self.tamano = ancho
    
    #Funcion dibujar
    #Esta funcion dibuja el boton 
    def dibujar(self):
        noStroke()
        #stroke(124,151,171)
        #fill(124,151,171)
        fill(0,105,210)
        rect(self.x, self.y, self.ancho, self.alto)
        fill(0,0,0)
        textSize(30)
        text(self.texto, self.x, self.y+35)
    
    #Funcion activo
    #entrada:  las posiciones del boton(x,y)
    #salida: Retorna true si se activo el boton    
    def Activo(self,x,y):
        if (self.x + self.tamano >= x and self.x <= x) and (self.y +self.tamano >= y and self.y <= y):
                return True
        return False