#Funcion ganeV
#entradas:  una matriz de 6x6
#salidas: True si se encuentra una sucesion de ceros o unos y False si no se encuentra
def ganeV(m):
    
    for f in range(6):
        nM = ""
        for c in range(6):
            nM = nM + str(m[c][f].colorF)
        print (nM)
        if "00000" in str(nM):
            return True
        elif "11111" in str(nM):
            return True  
    return False

#Funcion ganeH
#entradas:  una matriz de 6x6
#salidas: True si se encuentra una sucesion de ceros o unos y False si no se encuentra
def ganeH(m):
    for f in range(6):
        nM = ""
        for c in range(6):
            nM = nM + str(m[f][c].colorF)
        print (nM)
        if "00000" in str(nM):
            return True
        elif "11111" in str(nM):
            return True 
    return False

#Funcion ganeDiagI
#entradas:  una matriz de 6x6
#salidas: True si se encuentra una sucesion de ceros o unos y False si no se encuentra
def ganeDiagI(m):
    nM = ""
    m  = m[::-1]
    for c in range(6):
        nM = nM + str(m[c][c].colorF)
    print (nM)
    if "00000" in str(nM):
        return True
    elif "11111" in str(nM):
        return True
    return False

#Funcion ganeDiagD
#entradas:  una matriz de 6x6
#salidas: True si se encuentra una sucesion de ceros o unos y False si no se encuentra
def ganeDiagD(m):
    nM = ""
    for c in range(6):
        nM = nM + str(m[c][c].colorF)
    print (nM)
    if "00000" in str(nM):
        return True
    elif "11111" in str(nM):
        return True
    return False

#Funcion ganeDiagDsub2
#entradas:  una matriz de 6x6
#salidas: True si se encuentra una sucesion de ceros o unos y False si no se encuentra
def ganeDiagDsub2(m):
    nM = ""
    p = 0
    for c in range(1,6):
        nM = nM + str(m[p][c].colorF)
        p += 1 
    print (nM)
    if "00000" in str(nM):
        return True
    elif "11111" in str(nM):
        return True  
    return False

#Funcion ganeDiagDsub3
#entradas:  una matriz de 6x6
#salidas: True si se encuentra una sucesion de ceros o unos y False si no se encuentra
def ganeDiagDsub3(m):
    nM = ""
    p = 1
    for c in range(0,5):
        nM = nM + str(m[p][c].colorF)
        p += 1 
    print (nM)
    if "00000" in str(nM):
        return True
    elif "11111" in str(nM):
        return True 
    return False

#Funcion ganeDiagIsub3
#entradas:  una matriz de 6x6
#salidas: True si se encuentra una sucesion de ceros o unos y False si no se encuentra
def ganeDiagIsub3(m):
    nM = ""
    m = m[::-1]
    for i in m:
        print(i)
    p = 0
    for c in range(1,6):
        nM = nM + str(m[p][c].colorF)
        p += 1 
    print (nM)
    if "00000" in str(nM):
        return True
    elif "11111" in str(nM):
        return True
    return False

#Funcion ganeDiagIsub2
#entradas:  una matriz de 6x6
#salidas: True si se encuentra una sucesion de ceros o unos y False si no se encuentra
def ganeDiagIsub2(m):
    nM = ""
    m = m[::-1]
    for i in m:
        print(i)
    p = 1
    for c in range(0,5):
        nM = nM + str(m[p][c].colorF)
        p += 1 
    print (nM)
    if "00000" in str(nM):
        return True
    elif "11111" in str(nM):
        return True 
    return False