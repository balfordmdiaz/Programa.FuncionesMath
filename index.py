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



print("Operaciones: Sumar    |   Restar   |   Multiplicar  |   Dividir")

while True:
    try:
        op = (str(input("Ingresa la operacion a utilizar: ")))
        op_=op.lower()

        if op_ == "sumar":
            print("Resultado = " + str(suma(val1, val2)))
            break

        elif op_ == "restar":
            print("Resultado = " + str(resta(val1, val2)))
            break

        elif op_ == "multiplicar":
            print("Resultado = " + str(multiplicar(val1, val2)))
            break

        elif op_ == "dividir":
            print("Resultado = " + str(dividir(val1, val2)))
            break

    except ValueError:
        print("Has escrito mal la operacion. Intentelo Nuevamente")


print("Operacion Ejecutada. Siga la ejecucion del Programa")

#https://github.com/balfordmdiaz/Programa.FuncionesMath.git
