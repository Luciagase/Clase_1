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
  nivel=input('Nivel: ')
  

def definir_limites():
  if elige_nivel == 1:
    maximo = 100
  elif elige_nivel == 2:
    maximo = 1000
  elif elige_nivel == 3:
    maximo = 1000000
  elif elige_nivel == 4:
    maximo = 1000000000000
  else:
    print('Tiene que ser uno de los cuatro niveles anteriores')
    elige_nivel()


def numero_random():
  import random
  numeroRan= random.randint(0,maximo)


from entrada import (pedir_entrada_numero, pedir_entrada_numero_delimitado)


def jugar_una_vez(numeroRan, maximo):
    intento = pedir_entrada_numero_delimitado("Adivine el numero", maximo)

    # Se comprueba si el intento es correcto o no
    if intento < numeroRan:
        print("Demasiado pequeño")
        victoria = False
    elif intento > numeroRan:
        print("Demasiado grande")
        maximo = intento - 1
        victoria = False
    else:
        print("¡Ha ganado!")
        victoria = True
        maximo = intento
    return victoria, maximo


def pedir_entrada_del_numero_incognita(maximo):
    return pedir_entrada_numero_delimitado("Introduzca el número a adivinar", maximo)


def jugar_una_partida(numeroRan, maximo):
    while True:
        # Se entra en un bucle infinito
        # que permite jugar varias veces

        victoria, maximo = jugar_una_vez(numeroRan, maximo)

        if (victoria):
            return




def jugar():
    maximo = decifinir_limites()
    while True:
        numero = pedir_entrada_del_numero_incognita(minimo, maximo)
        jugar_una_partida(numero, maximo)




