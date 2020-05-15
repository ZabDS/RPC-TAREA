import xmlrpc.client
import datetime
s = xmlrpc.client.ServerProxy('http://localhost:8000')

while True:
    opc = input("Ingrese una de las siguientes opciones\n"
                "1.-Suma\n"
                "2.-Resta\n"
                "3.-Multiplicacion\n"
                "4.-División\n"
                "5.-Salir\n")
    if int(opc) == 1:
        x = input("Ingrese sumando 1 ")
        y = input("Ingrese sumando 2 ")
        print("El resultado es: ",s.suma(x,y))
    if int(opc) == 2:
        x = input("Ingrese restando 1 ")
        y = input("Ingrese restando 2 ")
        print("El resultado es: ",s.resta(x,y))
    if int(opc) == 3:
        x = input("Ingrese multiplicando 1 ")
        y = input("Ingrese multiplicando 2 ")
        print("El resultado es: ",s.mult(x,y))
    if int(opc) == 4:
        x = input("Ingrese numerador ")
        y = input("Ingrese denominador ")
        print("El resultado es: ",s.div(x,y))        
    if int(opc) == 5:
        break
    
    
        
        