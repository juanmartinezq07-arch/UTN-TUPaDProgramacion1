print("INSTITUTO DE INGLES")

#defino y le doy valores a las variables: dia, DD/MM
print("Ingrese la fecha y día de la siguiente forma: día, DD/MM")
fecha = input("")
fecha = fecha.split(", ")
dia_semana = fecha[0].lower()
dd, mm = fecha[1].split("/")
dd = int(dd)
mm = int(mm)

#validacion de meses y dias
if mm <= 12 and mm >= 1 :
    if mm == 2 :
        if dd > 28 :
            print("X Fecha Incorrecta X")
    else:
        if mm == 1 or mm == 3 or mm == 5 or mm == 7 or mm == 8 or mm == 10 or mm == 12 :
            if dd > 31 :
                print("X Fecha Incorrecta X")
        else:
            if dd > 30 :
                print("X Fecha Incorrecta X")
else:
    print("X Fecha Incorrecta X")

#condicional de los dias (separados por nivel inical, nivel intermedio, nivel avanzado, práctica hablada, inglés para viajeros)
#lunes
if dia_semana == "lunes" :
    print("¿Hubo exámen en el Nivel Inicial? (responder con si o no)")
    respuesta = input(str("")).upper()
    if respuesta == "SI" :
        alumnos_aprobados = int(input("Ok. Ingrese la cantidad de alumnos aprobados: "))
        alumnos_desaprobados = int(input("Ok. Ingrese la cantidad de alumnos desaprobados: "))
        total_alumnos = alumnos_desaprobados + alumnos_aprobados
        porcentaje_alumnos = (alumnos_aprobados / total_alumnos) * 100
        porcentaje_alumnos = round(porcentaje_alumnos,1)
        print("El porcentaje de alumnos aprobados en el Nivel Inicial es de:",porcentaje_alumnos, "%")
    if respuesta == "no" :
        print("Ok. ¡Que tengas buen día!")

#martes
if dia_semana == "martes" :
    print("¿Hubo exámen en el Nivel Intermedio?")
    respuesta = input(str("")).upper()
    if respuesta == "SI" :
        alumnos_aprobados = int(input("Ok. Ingrese la cantidad de alumnos aprobados: "))
        alumnos_desaprobados = int(input("Ok. Ingrese la cantidad de alumnos desaprobados: "))
        total_alumnos = alumnos_desaprobados + alumnos_aprobados
        porcentaje_alumnos = (alumnos_aprobados / total_alumnos) * 100
        porcentaje_alumnos = round(porcentaje_alumnos,1)
        print("El porcentaje de alumnos aprobados en el Nivel Intermedio es de:",porcentaje_alumnos, "%")
    if respuesta == "no" :
        print("Ok. ¡Que tengas buen día!")

#miercoles
if dia_semana == "miercoles" :
    print("¿Hubo exámen en el Nivel Avanzado?")
    respuesta = input(str("")).upper()
    if respuesta == "SI" :
        alumnos_aprobados = int(input("Ok. Ingrese la cantidad de alumnos aprobados: "))
        alumnos_desaprobados = int(input("Ok. Ingrese la cantidad de alumnos desaprobados: "))
        total_alumnos = alumnos_desaprobados + alumnos_aprobados
        porcentaje_alumnos = (alumnos_aprobados / total_alumnos) * 100
        porcentaje_alumnos = round(porcentaje_alumnos,1)
        print("El porcentaje de alumnos aprobados en el Nivel Avanzado es de:",porcentaje_alumnos, "%")
    if respuesta == "no" :
        print("Ok. ¡Que tengas buen día!")

#jueves
if dia_semana == "jueves" :
    asistencia = int(input("Ingrese el porcentaje de los alumnos asistidos de hoy: "))
    if asistencia > 50 :
        print("Asistió la mayoría a la práctica hablada.")
    else:
        print("No asistió la mayoría a la práctica hablada.")

#viernes
if dia_semana == "viernes" :
    if dd == 1 and mm == 1 or mm == 7 :
        print("Comienzo de nuevo ciclo")
        cant_alumnos = int(input("Ingrese la cantidad de alumnos del nuevo ciclo: "))
        arancel = int(input("Ingrese el arancel en $ por cada alumno: "))
        arancel_total = cant_alumnos * arancel
        print("El total de los ingresos es de:",arancel_total)
