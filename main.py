
class Calculadora():
    def __init__(self):
        pass
    
    print("Calculadora iniciada")
    a = float(input("Ingrese el primer numero: "))
    b = float(input("Ingrese el segundo numero: "))
    opcion = input("Ingrese la operacion deseada (suma, resta, multiplicacion, division): ").strip().lower()
    if opcion == "resta":
        from resta import restar
        resultado = restar(a,b)
        print(resultado)
    elif opcion == "division":
        from division import dividir
        resultado = dividir(a,b)
        print(resultado)
    else:
        print("Operacion no soportada")