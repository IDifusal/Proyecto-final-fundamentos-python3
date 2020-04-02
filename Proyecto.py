import os
os.system('cls')
print("Hola bienvenido")

#**********************
#* varialbes globales *
#**********************
runnin = True
database = list()
# FUNCIONES
def show_menu():
    print("1- Cargar pacientes")
    print("2- Buscar pacientes")
    print("3- Listar pacientes")
    print("4- Salir")
    res = input("INGRESE UNA OPCION ■")
    os.system('cls')
    return res
# LOOP PRINCIPAL
def response(r):
    validated = False 
    num_res =  0

    if respuesta.isdigit():
        num_res = int(respuesta)
        if num_res >= 1 and num_res <=4 :
            msg = "Esta en rango"
            validated = True
        else:
           msg ="Fuera de rango"
    else:
        msg ="Entrada incorrecta"

    return validated, num_res,msg


while runnin:
    respuesta = show_menu()
    validated,num_res,msg = response(respuesta)
    if validated:
        if num_res ==1:
            name = input("Ingrese nombre del paciente -> ")
            clinica = input ("Ingrese el nombre de la clinica -> ")
            paciente = {"Nombre":name,"Clinica":clinica}
            database.append(paciente)
            print(database)

        elif num_res ==2:
            name = input ("Ingrese el nombre del paciente -> ")
            encontrado = True
            for x in range(len(database)):
                 if database[x]["Nombre"].lower() == name.lower():
                    print ("")
                    print ("PACIENTE ENCONTRADO | CLINICA -> ",database[x]["Clinica"])
                    print("")
                 else:
                    encontrado = False
            if not encontrado:
                 print("PACIENTE NO ENCONTRADO")       

        elif num_res ==3:
            for x in range(len(database)):
                print("")
                print ("Lista de pacientes")
                print("Nombre -> ".rjust(10),database[x]["Nombre"],"CLINICA -> ".rjust(10),database[x]["Clinica"])
                print("FIN DE LISTA")
                print("")
        
        else:
            runnin = False
    else: 
        print(msg)
print("")
print("APLICACION FINALIZADA")
print("")