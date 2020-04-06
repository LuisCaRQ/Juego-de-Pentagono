
from matriz import *
from Boton import *

campo = None
turno = 0 
s = 0
salir = 0
B1 = None
B2 = None
B3 = None
B4 = None
B5 = None
B6 = None
B7 = None
B8 = None

#Se inicializa el programa
def setup():
    global campo
    #background(174,215,255)
    img = loadImage("goku.png")
    size(700,800)
    image(img,0,0)
    campo = matriz()
    

#condiciones al hacer click en la pantalla
def mousePressed():
    global turno,x,s
    if salir == 0:
        if s == 0:
            if campo.jugadaValida(mouseX,mouseY):
                if campo.ponerFicha(mouseX,mouseY,turno):
                    s = 1
                    if campo.victoria():
                        Vic()
                    if campo.empate():
                        Empate()
        else:            
            if B1.Activo(mouseX,mouseY):
                campo.Nmatriz(0,3,0,3,"d")
                s = 0
                if campo.victoria():
                    Vic()
                else:
                    turn()
            if B2.Activo(mouseX,mouseY):
                campo.Nmatriz(3,6,0,3,"d")
                s = 0
                if campo.victoria():
                    Vic()
                else:
                    turn()
            if B3.Activo(mouseX,mouseY):
                campo.Nmatriz(0,3,3,6,"i")
                s = 0
                if campo.victoria():
                    Vic()
                else:
                    turn()
            if B4.Activo(mouseX,mouseY):
                campo.Nmatriz(3,6,3,6,"i")
                s = 0
                if campo.victoria():
                    Vic()
                else:
                    turn()
            if B5.Activo(mouseX,mouseY):
                campo.Nmatriz(0,3,0,3,"i")
                s = 0
                if campo.victoria():
                    Vic()
                else:
                    turn()
            if B6.Activo(mouseX,mouseY):
                campo.Nmatriz(3,6,0,3,"i")
                s = 0
                if campo.victoria():
                    Vic()
                else:
                    turn()
            if B7.Activo(mouseX,mouseY):
                campo.Nmatriz(0,3,3,6,"d")
                s = 0
                if campo.victoria():
                    Vic()
                else:
                    turn()
            if B8.Activo(mouseX,mouseY):
                campo.Nmatriz(3,6,3,6,"d") 
                s = 0
                if campo.victoria():
                    Vic()
                else:
                    turn()
    else:
        if (545 + 120 >= mouseX and 545 <= mouseX) and (700 +55 >= mouseY and 700 <= mouseY):
            exit()
       
#funcion que crea los botones
def Botones():
    global B1,B2,B3,B4,B5,B6,B7,B8
    B1 = Boton("->",200,110,50,50) #Boton C1 Arriba
    B2 = Boton("->",200,540,50,50) #Boton C3 abajo 
    B3 = Boton("<-",420,110,50,50) #Boton C2 Arriba
    B4 = Boton("<-",420,540,50,50) #Boton C4 abajo
    B5 = Boton("<-",105,220,40,50) #Boton C1 Derecha
    B6 = Boton("<-",105,430,40,50) #Boton C3 Derecha
    B7 = Boton("->",540,220,40,50) #Boton C2 Izquierda
    B8 = Boton("->",540,430,40,50) #Boton C4 abajo
    
#Cambia el turno     
def turn():
    global turno
    if turno == 0:
        turno = 1    
    elif turno == 1:
        turno = 0

#Muestra el turno del jugador
def jugador():
    global turno
    if turno == 0:
        texto = "Turno del jugador 1 , Fichas Blancas"
    if turno == 1:
        texto = "Turno del jugador 2 , Fichas Negras"
    fill(12,134,224)
    noStroke()
    rect(170, 670, 380, 45)
    fill(0,0,0)
    textSize(20)
    text(texto, 170, 700)
    
#Muestra la victoria del jugador
def Empate():
    global salir
    fill(12,134,224)
    noStroke()
    rect(250, 730, 380, 45)
    fill(0,0,0)
    textSize(20)
    text("Empate", 250, 750)
    salir = 1 
    
#Muestra la victoria del jugador
def Vic():
    global turno,salir
    if turno == 0:
        texto = "Victoria del jugador 1"
    if turno == 1:
        texto = "Victoria del jugador 2"
    fill(12,134,224)
    noStroke()
    rect(250, 730, 380, 45)
    fill(0,0,0)
    textSize(20)
    text(texto, 250, 750)
    salir = 1 
        
#crea un boton para salir 
def sal():
    global salir
    if salir != 0:
        fill(12,134,224)
        #noStroke()
        rect(545, 700, 120, 55)
        fill(0,0,0)
        textSize(50)
        text("Salir", 550, 750)
    
    
#dibuja la interfaz del programa
def draw():
    global campo
    campo.display()
    Botones()
    B1.dibujar()
    B2.dibujar()
    B3.dibujar()
    B4.dibujar()
    B5.dibujar()
    B6.dibujar()
    B7.dibujar()
    B8.dibujar()
    jugador()
    sal()

    

    