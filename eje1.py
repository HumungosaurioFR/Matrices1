abc = [['-','-','-','-','-','-'],['-','-','-','-','-','-'],['-','-','-','-','-','-'],['-','-','-','-','-','-'],['-','-','-','-','-','-']]


    
def fnt_agregar(dato, x, y):

    if dato == 'a' and (x == 0 and y == 0):
        if abc[x][y] == '-':
            abc[x][y] = dato.upper()
    elif dato == 'b' and (x == 0 and y == 1):
        if abc[x][y] == '-':
            abc[x][y] = dato.upper()
    elif dato == 'c' and (x == 0 and y == 2):
        if abc[x][y] == '-':
            abc[x][y] = dato.upper()
    elif dato == 'd' and (x == 0 and y == 3):
        if abc[x][y] == '-':
            abc[x][y] = dato.upper()
    elif dato == 'e' and (x == 0 and y == 4):
        if abc[x][y] == '-':
            abc[x][y] = dato.upper()
    elif dato == 'f' and (x == 0 and y == 5):
        if abc[x][y] == '-':
            abc[x][y] = dato.upper()
    elif dato == 'g' and (x == 1 and y == 0):
        if abc[x][y] == '-':
            abc[x][y] = dato.upper()
    elif dato == 'h' and (x == 1 and y == 1):
        if abc[x][y] == '-':
            abc[x][y] = dato.upper()
    elif dato == 'i' and (x == 1 and y == 2):
        if abc[x][y] == '-':
            abc[x][y] = dato.upper()
    elif dato == 'j' and (x == 1 and y == 3):
        if abc[x][y] == '-':
            abc[x][y] = dato.upper()
    elif dato == 'k' and (x == 1 and y == 4):
        if abc[x][y] == '-':
            abc[x][y] = dato.upper()
    elif dato == 'l' and (x == 1 and y == 5):
        if abc[x][y] == '-':
            abc[x][y] = dato.upper()
    elif dato == 'm' and (x == 2 and y == 0):
        if abc[x][y] == '-':
            abc[x][y] = dato.upper()
    elif dato == 'n' and (x == 2 and y == 1):
        if abc[x][y] == '-':
            abc[x][y] = dato.upper()
    elif dato == 'ñ' and (x == 2 and y == 2):
        if abc[x][y] == '-':
            abc[x][y] = dato.upper()
    elif dato == 'o' and (x == 2 and y == 3):
        if abc[x][y] == '-':
            abc[x][y] = dato.upper()
    elif dato == 'p' and (x == 2 and y == 4):
        if abc[x][y] == '-':
            abc[x][y] = dato.upper()
    elif dato == 'q' and (x == 2 and y == 5):
        if abc[x][y] == '-':
            abc[x][y] = dato.upper()
    elif dato == 'r' and (x == 3 and y == 0):
        if abc[x][y] == '-':
            abc[x][y] = dato.upper()
    elif dato == 's' and (x == 3 and y == 1):
        if abc[x][y] == '-':
            abc[x][y] = dato.upper()
    elif dato == 't' and (x == 3 and y == 2):
        if abc[x][y] == '-':
            abc[x][y] = dato.upper()
    elif dato == 'u' and (x == 3 and y == 3):
        if abc[x][y] == '-':
            abc[x][y] = dato.upper()
    elif dato == 'v' and (x == 3 and y == 4):
        if abc[x][y] == '-':
            abc[x][y] = dato.upper()
    elif dato == 'w' and (x == 3 and y == 5):
        if abc[x][y] == '-':
            abc[x][y] = dato.upper()
    elif dato == 'x' and (x == 4 and y == 0):
        if abc[x][y] == '-':
            abc[x][y] = dato.upper()
    elif dato == 'y' and (x == 4 and y == 1):
        if abc[x][y] == '-':
            abc[x][y] = dato.upper()
    elif dato == 'z' and (x == 4 and y == 2):
        if abc[x][y] == '-':
            abc[x][y] = dato.upper()
    elif dato == 'ch' and (x == 4 and y == 3):
        if abc[x][y] == '-':
            abc[x][y] = dato.upper()  
    elif dato == 'll' and (x == 4 and y == 4):
        if abc[x][y] == '-':
            abc[x][y] = dato.upper()
    elif dato == 'rr' and (x == 4 and y == 5):
        if abc[x][y] == '-':
            abc[x][y] = dato.upper()
    else:
        input('\nEsta letra no va ahí <ENTER>')

def fnt_impresion_matriz():
    for i in range(len(abc)):
        for j in range(len(abc[i])):
            print(abc[i][j], end='  ')
        print()
        
sw = True
while sw == True:
    import os
    os.system('cls')
    fnt_impresion_matriz()
    fnt_agregar(input('Dato: '), int(input('Fila: ')), int(input('Columna: ')))