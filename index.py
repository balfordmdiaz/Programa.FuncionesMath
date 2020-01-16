from module_math import suma, resta, multiplicar, dividir


while True:
    try:
        val1 = (int(input("Introduce el primer valor: " )))
        break
        
    except ValueError:
        print("El primer valor es incorrecto. Intentalo Nuevamente")

while True:
    try:
        val2 = (int(input("Introduce el segundo valor: " )))
        break
        
    except ValueError:
        print("El segundo valor es incorrecto. Intentalo Nuevamente")


####CODIGO A MEJORAR
"""print("Operaciones; Sumar    |   Restar   |   Multiplicar  |   Dividir")

while True:
    try:
        op = str(input("Ingresa la operacion a utilizar: "))
        break

    except ValueError:
        print("Has escrito mal la operacion. Intentelo Nuevamente")

op_=op.lower()#######funcion que permite que no importa como se escribe el dato lo haga pasar"""

print("Operaciones; Sumar    |   Restar   |   Multiplicar  |   Dividir")
op = input("Ingresa la operacion a utilizar: ")
op_=op.lower()#######funcion que permite que no importa como se escribe el dato lo haga pasar

if op_ == "sumar":
    print(suma(val1, val2))

elif op_ == "restar":
    print(resta(val1, val2))

elif op_ == "multiplicar":
    print(multiplicar(val1, val2))

elif op_ == "dividir":
    print(dividir(val1, val2))

else:
    print("No existe la operacion")

print("Operacion Ejecutada. Siga la ejecucion del Programa")

