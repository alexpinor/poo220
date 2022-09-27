from sqlite3 import TimestampFromTicks


Estado = False
ruedas = input("cuantas ruedas tiene el vehiculo?")
lat=input("ingrese la latitud del vehiculo")
long=input("ingrese la longitud del vehiculo")
velocidad=input("ingrese la velocidad del vehiculo")
ubicacion=[lat,long]
tiempo=0
def encender():
    global Estado
    Estado=not(Estado)
    print("----------------------------")
    print("***vehiculo encendido***" if Estado else "***vehiculo apagado***")
    print("----------------------------")
def salida():
    print("-------------------------------------------------")
    print("el vehiculo tiene: "+str(ruedas)+ " ruedas")
    print("el vehiculo esta en la pos: "+str(ubicacion)+" gps")
    print(f"la velocidad actual es: " +str(velocidad)+ "km/h")
    print("-------------------------------------------------")
def acelerar():
    global velocidad
    global Estado
    if (Estado):
        velocidad=int(velocidad)+10
        print("el vehiculo ha acelerado a "+str(velocidad)+ " km/h \n")
        salida()
    else:
        print("----------------------------")
        print("encienda el vehiculo primero")
        print("----------------------------")
def frenar():
    global velocidad
    if velocidad>0:
        velocidad=int(velocidad)*0
        print("----------------------------")
        print("el vehiculo ha frenado "+str(velocidad)+ " km/h")
        print("----------------------------")
    else:
        print("----------------------------")
        print("el vehiculo esta detenido")
        print("----------------------------")
def viajar():
    global velocidad
    global tiempo
    global ubicacion
opc=0
print("elija que desea realizar?")
while((opc)!=9):
    opc=int(input("1.- encender \n2.- Acelerar \n3.- frenar  \n4.- mostrar vehiculo \n9.- salir \n"))
    if(opc==1):
        encender()
    elif(opc==2):
        acelerar()
    elif(opc==3):
        frenar()
    elif(opc==4):
        salida()

print("--------BUEN VIAJE :)---------")