print('¿SERÁS CAPAZ DE ADIVINAR EL NÚMERO?')

def elige_nivel():
  print('Elige un nivel: ')
  print('1 = simple')
  simple = 1
  print('2 = intermedio')
  intermedio = 2
  print('3 = avanzado')
  avanzado = 3
  print('4 = experto')
  experto = 4
  print('')

def Introduce_nivel():
  nivel=input('Nivel: ')


  
def definir_limites():
  if Introduce_nivel == 1:
    maximo = 100
  elif Introduce_nivel == 2:
    maximo = 1000
  elif Introduce_nivel == 3:
    maximo = 1000000
  elif Introduce_nivel == 4:
    maximo = 1000000000000
  else:
    print('No existe tal nivel')
    Introduce_nivel(nivel)



def numero_random():
  maximo=definir_limites()
  import random
  numeroRan= random.randint(0,maximo)




def jugar_una_vez():
    intento = int(input('Introduce un numero: '))
    numeroRan=numero_random()

    # Se comprueba si el intento es correcto o no
    if intento < numeroRan:
        print("Demasiado pequeño")
        jugar_una_vez()
    elif intento > numeroRan:
        print("Demasiado grande")
        jugar_una_vez()
    else:
        print("¡Ha ganado!")



def jugar():
  elige_nivel()
  Introduce_nivel()
  definir_limites()
  jugar_una_vez()


jugar()