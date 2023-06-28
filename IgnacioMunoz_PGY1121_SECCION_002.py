import os
os.system ("cls")

Menu = """
1) Registrar un Producto.
2) Buscar un Producto.
3) Listar un Producto.
4) Salir.
"""
ListaCodigos = [11111111, 22222222, 77777777]
ListaNombres = ['Pan', 'Milo', 'Jugo']
ListaPrecios = [200, 300, 400]
ListaCantidadDispo = [20, 100, 10]
ListaCategorias = [12345678, 87654321, 33333333]

def funcion_registrar():
    print("Registrando el Producto")
    while True:  
            Codigo = int(input("Ingrese el Codigo: "))
            if len(Codigo) != 8:
                print("El Codigo debe ser igual a 8 numeros")
            else:
                ListaCodigos.append(Codigo)
                print("Codigo Ingresado. ")
                print(ListaCodigos)
                break
    while True:
         Nombres = input("Ingrese un nombre: ")
         if len(Nombres) >= 2 and len(Nombres) < 50:
              ListaNombres.append(Nombres)
              print("Nombre agregado! ")
              print(ListaNombres)
              break
         else:
              print("El nombre tiene que tener entre 2 a 50 caracteres.")
    while True:
         Categorias = input("Ingrese una Categoria: ")
         if len(Categorias) >= 1:
              ListaCategorias.append(Categorias)
              print("La Categoria ha sido asignada")
              print(ListaCategorias)
              break
         else:
              print("Categoria invalida")
    while True:
         Precio = input("Ingrese el Precio: ")
         if Precio > 0:
              ListaPrecios.append(Precio)
              print("Precio Añadido!")
              print(ListaPrecios)
              break
         else:
              print("Precio Invalido!")
    while True:
         CantidadDispo = input("Ingrese la cantidad disponible: ")
         if CantidadDispo > 0:
              ListaCantidadDispo.append(CantidadDispo)
              print("Cantidad disponible añadida!")
              print(ListaCantidadDispo)
              break
         else:
              print("Cantidad invalida!")

def funcion_buscar():
     print("Buscando el Producto")
     Buscar = input("Ingresa la categoria que quieres buscar")
     print(f"Listado categoria {Buscar} \n")
     print("N | CODIGO | NOMBRE | CATEGORIA | PRECIO | CANTIDAD DISPONIBLE")
     print("--------------------------------------------------------------")
     for i in range(len(ListaNombres)):
          if Buscar == ListaCategorias[i]:
               print(f"{ListaNombres[i]:20s} {ListaCodigos[i]:6d} {ListaCategorias[i]:10d} {ListaCantidadDispo[i]:60d} {ListaPrecios[i]:4d}")


def funcion_listar():
		print("Opcion 3")
		print(" Producots disponibles en venta \n")
		print("N| CODIGO | CATEGORIA | PRECIO | CANTIDAD DISPONIBLE | STOCK BAJO")
		print("-----------------------------------------------------------------")
StockBajo = 0 
for i in range(len(ListaCodigos)):
            if ListaCantidadDispo [i] < 5:
                 Stock = "Si"
                 StockBajo += 1
            else:
              Stock = "No"
            print(f"{i+1} | {ListaCodigos[i]:6d} | {ListaNombres[i]:20s} | {ListaCategorias[i]:10d} | {ListaPrecios[i]:4d} | {ListaCantidadDispo[i]:60d}")
                    
                    
                                      

              









opc = 0
NombreApellido = input("Hola, Ingresa tu nombre y apellido por favor: ")
while True:
     opc = int(input(Menu))
     if opc == 1:
           funcion_registrar()
     elif opc == 2:
           funcion_buscar()
     elif opc == 3:
           funcion_listar()
     elif opc == 4:
           print(f"Hasta luego {NombreApellido}, Vuelve pronto!")
           break
     else: print("Opcion invalida!")
    

     
           
     

    



