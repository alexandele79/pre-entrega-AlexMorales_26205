lista_productos =[("mesa","prueba","1"),("silla","prueba","1"),("operador","prueba","1")] #[[nombre],[categoria],[precio]]
#lista de productos con 3 productos de prueba.
pregunta = "SI"
while True:
    print(" .^_^. "*15)
    print("\n \t \t \t Tu inventario de compras_baratas.com\n")
    print(" .^_^. "*15)
    print("\n1. Agregar productos\n2. Mostrar productos\n3. Buscar productos\n4. Eliminar productos\n5. Salir")

    opcion = input("Seleccione una opción (1-5): ").strip()

    if opcion == "1":
        print("###### ... Agregar productos ... #####")

        nombre = input("Nombre del producto: ").strip() #""
        while nombre == "":
            print("Error: debe usar un nombre que no sea vacio.")
            nombre = input("Nombre del producto: ").strip()

        categoria = input("Seleccione la categoria del producto: ").strip()
        while categoria == "":
            print("Error: debe usar una categoria que no sea vacia.")
            categoria = input("Seleccione la categoria del producto: ").strip()

        precio_str = input("Precio (sin centavos): ").strip()
        while not precio_str.isdigit():
            print("Error: ingresar solo números positivos")
            precio_str = input("Precio (sin centavos): ").strip()
        precio = int(precio_str)

        datos = [nombre,categoria,precio]
        lista_productos.append(datos)

    elif opcion == "2":
        print("##### ... Ver lista de productos ... #####")

        if len(lista_productos) == 0:
            print("No has agregado todavia productos - lista vacia")
        else:
            for i in range(len(lista_productos)):
                print(f"{i+1}: Nombre: {lista_productos[i][0]}\t Categoria: {lista_productos[i][1]}\t Precio: AR${lista_productos[i][2]}")
            
    elif opcion == "3":
        print("###### Buscar en lista de producto .... ######")
        
        if len(lista_productos) == 0:
            print("No has agregado todavia productos - no hay para buscar")
            
        else:
            print("Lista de productos cargados: ")
            for i in range(len(lista_productos)):
                print(f"{i+1}: {lista_productos[i][0]}")
            busqueda = input("Nombre del producto a buscar: ").strip().lower()
            while busqueda == "":
                print("Error: escribir un producto válido para buscar")
                busqueda = input("Nombre del producto a buscar: ").strip().lower()

            encontrado = 0
            for i in range(len(lista_productos)):
                if busqueda in lista_productos[i][0].lower():
                    print(f"Es el item {i+1}: {lista_productos[i][0]}, {lista_productos[i][1]}, AR$ {lista_productos[i][2]}")
                    encontrado += 1

            if encontrado == 0:
                print("No se encontró ningun resultado.")
            else:
                print(f"Productos encontrados {encontrado}")

    elif opcion == "4":
        print("##### Eliminar productos ##### ")
        print("Selecciones de la lista de productos cargados para eliminar: ")
        for i in range(len(lista_productos)):
            print(f"{i+1}: {lista_productos[i][0]}")
        elimina = input("Escriba el Nombre del producto a eliminar: ").strip().lower()
        while elimina == "":
            print("Error: escribir un producto válido para buscar")
            elimina = input("Escriba el Nombre del producto a eliminar: ").strip().lower()

        encontrado = 0
        for i in range(len(lista_productos)):
            if elimina in lista_productos[i][0].lower():
                lista_productos.pop(i)
                encontrado += 1
                print("Producto eliminado correctamente.")
                
            if encontrado == 0:
                print("Producto no encontrado.")

    elif opcion == "5":
        print("\nGracias por utilizarme, espero haber funcionado correctamente, son 5.000.000 AR$, alias = mi.cuenta")
        break

    else:
        print("Debes seleccionar una opción de la 1 a la 5: ")
