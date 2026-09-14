especialidades=[]
cupos=[]

while True:
    print('''============================
MENU
1. INGRESAR lISTA DE ESPECIALIDADES
2. INGRESAR LISTA DE CUPOS DISPONIBLES POR ESPECIALIDAD 
3. MOSTRAR AGENDA 
4. CONSULTAR CUPOS DE UNA ESPECIALIDAD 
5. LISTAR ESPECIALIDADES SIN CUPO 
6. AGREGAR ESPECIALIDAD
7. ACTUALIZAR CUPOS (RESERVAR/CANCELAR) 
8. SALIR''')
    
    opcion=input("Ingrese una opcion (1-8): ")

    while not opcion.isdigit():
        opcion=input("Ingrese una opcion valida: ")
    opcion=int(opcion)
    match opcion:
        case 1:
            cant_espe=input("Cantidad de especialidades a ingresar: ")
            while not cant_espe.isdigit():
                cant_espe=input("Ingrese una opcion valida: ")
            cant_espe=int(cant_espe)

            for i in range(cant_espe):
                espe_ingresadas=input(f"Especialidad N°{i + 1}: ").capitalize().strip()
                while not espe_ingresadas.isalpha():
                    espe_ingresadas=input("Ingrese unicamente letras: ").capitalize().strip()
                if espe_ingresadas not in especialidades:
                    print("Especialidad guardada.")
                    especialidades.append(espe_ingresadas)
                else:
                    print("Especialidad existente")
        case 2:
            for especialidad in especialidades:
                cupos_disp=input(f"Cupos disponibles para {especialidad}: ")
                while not cupos_disp.isdigit():
                    cupos_disp=input(f"Coloque solo la cantidad de cupos: ")
                cupos_disp=int(cupos_disp)
                cupos.append(cupos_disp)

        case 3:
            if (len(especialidades)) == 0:
                print("No hay especialidades cargadas")
            elif (len(cupos)) == 0:
                print("No hay cupos cargados")
            else:
                for i in range(len(especialidades)):
                        print(f'''AGENDA DE TURNOS
{especialidades[i]} - Cupos disponibles: {cupos[i]}''')
        case 4: 
            especialidad_consul=input("Ingrese la especialidad para ver sus turnos: ")
            while not especialidad_consul.isalpha():
                especialidad_consul=input("Ingrese la especialidad para ver sus turnos: ")
            if especialidad_consul in especialidades:
                indice=especialidades.index(especialidad_consul)
                print(f"Turnos dispónibles para {especialidad_consul}:{cupos[indice]}")
            else:
                print("Especialidad no encontrada")
        case 5:
            encontrado=False
            for i in range(len(especialidades)):
                if cupos[i] ==0:
                    print(f"{especialidades[i]} no tiene turnos disponibles.")      


        
    
