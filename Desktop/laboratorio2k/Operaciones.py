# operaciones dadas en clase

# suma

def suma (a,b):
    '''suma dos numeros'''
    resultado= a + b 
    return resultado

# resta

def resta (a,b):
    '''resta dos numeros'''
    return a - b

# Multiplicacion 

def multiplicacion (a,b):
    '''multiplica dos numeros'''
    return a * b

# Division

def Division (a,b):
    '''Divide dos numeros'''
    return a / b

# Exponenciacion

def Exponenciacion (a,b):
    '''Eleva un numero '''
    return a ** b 

# raices

def raiz (a):
    '''raiz de un numeros'''
    import math
    return  math.sqrt(a)
 
# suma5

def suma5 ():
    '''suma 5 numeros'''
    suma=1
    for i in range (1,6):
        s= int (input(f"ingrese {i} numero: "))
        suma = suma + s
    print(suma)
      


suma5()


