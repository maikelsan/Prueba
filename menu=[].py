menu=[]

Cats_Día_Viernes=150
Cats_Día_Sábado=180
vendido_viernes=0
vendido_sabado=0
dicionario={"nombre":[],"funcion":[]}

def comprar_entrada():
        entradas=False
        nombre=str(input("ingrese su nombre: "))
        if dicionario["nombre"]:
            print("error. ya hay un nombre igual registrado")
        else:
            dicionario["nombre"].append(nombre)
            selecionar_funcion()



def selecionar_funcion():
    
    funcion=input(f"seleccione una funcion: \n2 1. Cats Día Viernes {Cats_Día_Viernes} entradas \n3 2. Cats Día Sábado {Cats_Día_Sábado} entradas")
    if funcion == 1:
        Cats_Día_Viernes-=1
        vendido_viernes+=1
        print(f"Entrada registrada en función 1! Stock restantes:\n2   Función 1 (Viernes): {Cats_Día_Viernes} \n3 Función 2 (Sábado): {Cats_Día_Sábado}")
        dicionario["funcion"].append(funcion)
        entradas=True
    elif funcion ==2:
        Cats_Día_Sábado=-1
        vendido_sabado=+1
        print(f"Entrada registrada en función 2! Stock restantes:\n2   Función 1 (Viernes): {Cats_Día_Viernes} \n3 Función 2 (Sábado): {Cats_Día_Sábado}")
        dicionario["funcion"]="funcion 2"
        entradas=True
    else:
        print("ingrese un numrero entero")
            



def cambio_funcion():
    if print("ingrese el nombre a buscar:", dicionario["nombre"]):
        cambiar=int(print("Cambiar de función (si es 1/no es 2)"))
        if cambiar==1:
            if dicionario["funcion"]==1:
                dicionario["funcion"]=2
            elif dicionario["funcion"]==2:
                dicionario["funcion"]=1
    else:
        print("el nombre no9 esta registrado")






def mostrar_stock():
    print(f"Función 1 (Viernes): Disponibles: {Cats_Día_Viernes}, vendidas {vendido_viernes} ")
    print(f"Función 2 (Sábado): Disponible: {Cats_Día_Sábado}, vendidas: {vendido_sabado}")

while True:
    print("\n1 TOTEM AUTOATENCIÓN CAFECONLECHE\n2 1.- Comprar entrada a Cats.\n2 2.- Cambio de función.\n3 3.- Mostrar stock de funciones.\n4 4.- Salir.")
    try:
        opcion=int(input("ingrese una opcion: "))
        if opcion==1:
            comprar_entrada() 
                
        elif opcion==2:
            cambio_funcion()
        elif opcion==3:
            mostrar_stock()
        elif opcion==4:
            print("saliendo del programa")
            break
    except ValueError:
        print("debe ingresar un numero valido")