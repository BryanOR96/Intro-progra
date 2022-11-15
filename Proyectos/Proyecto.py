#Estudiantes
#Bryan Orozco Rojas 
#Valeria Vega Madrigal


from turtle import delay
import time
#import numpy as np

ListaEmpleados=['Bryan','Valeria','Jafet','Anderson']
ListaCedula=[304920966,128376533,4653912873,652730165]
Salario=[2000,1500,1000,850]
Puesto=['Presidente','Vicepresidenta','tesorero','Recepcionista']

i=0
while i<3:
      usuario=input("ingrese su nombre de usuario :\n")
      i=i +1
      if str(usuario)=="a":
            print("USUARIO CORRECTO\n")
            clave=input("ingrese su clave\n")
            if str(clave)=="a":
                  print("Bienvenido Bryan\n")
                  break
            else:
                  print("Password incorrecto\n")
                  if    i==3:
                        print("Se agotaron sus intentos")
                        break
      else:
            print("USUARIO INCORRECTO\n")
            if    i==3:
                  print("INTENTOS AGOTADOS")



def menu():
    print("Elige una opción:\n",
          "1-Empleados.\n",
          "2-Clientes.\n",
          "3-Provedores.\n",
          "4-Productos.\n",
          "5-Ventas.\n",
          "6-Salir.\n")

    opcion = input("Escribe un número y pulsa enter: ")
        
    if opcion == "1":
        
        def menu1():
            
            print("Elige una opción:\n\n",
                "1-Ver empleados actuales.\n",
                "2-Modificar datos de empleados.\n",
                "3-Ingresar nuevo empleado.\n",
                "4-Salir al menu principal.\n")
                
            op1= input("Escribe un número y pulsa enter: ")
            
            if op1=="1":
                
                print("Los colaboradores actuales son los siguientes\n")
                for x in ListaEmpleados:
                    print (x)
                print()
                time.sleep(2)
                return menu1()


            elif op1=="2":
                
                NomEmpleado=input(" Digite el nombre del empleado al que desea modificar los datos: ")
                if NomEmpleado in ListaEmpleados:
                    print("Los datos del empleado",NomEmpleado,"Son los siguientes:")

                else:
                    print("El nombre digitado no se encuentra en la base de datos ")
                
                return menu1()

            elif op1=="3":
                
                AgregarEmpleado=input(print(" Digite el nombre del colaborador que desea Agregar a la lista"))
                
                
                Cedula=input(print("Digite el numero de cedula"))
                
                hora=input(print("Digite el salario por hora que ganara",AgregarEmpleado))
                
                trabajo=input(print("Ingrese el puesto que tendra ",AgregarEmpleado))
                
                ListaEmpleados.append(AgregarEmpleado)
                ListaCedula.append(Cedula)
                Salario.append(hora)
                Puesto.append(trabajo)
                print("El Colaborador",AgregarEmpleado,"con la cedula",Cedula," ganara un salario de ",hora, "por hora, en el puesto de ",Puesto, " ha sido agregado con exito")
                
                for valor_a, valor_b, valor_c, valor_d in zip(ListaEmpleados, ListaCedula, Salario, Puesto): 
	                print("Empleado: ",valor_a, "Cedula de identidad :",valor_b, "con salario de ",valor_c, " colones por hora en el puesto de: ,",valor_d, "ha sido agregado con exito ")
                return menu1()
                
            
            elif op1=="4":
                print("Volviendo al menu principal")
                return menu()
                

        menu1()


    elif opcion == "2":
        print()

    elif opcion == "3":
        print()

    elif opcion == "4":
        print()

    elif opcion == "5":
        print()
    
    elif opcion == "6":
        print("Finalizando programa")
        exit

    else:
        print("No has introducido una opción válida.\n Cerrando programa")
menu()

