#Biblioteca
Contraseña_Correcta="Insano"
intentos=-3
Libros=[]

def contraseña(Contraseña_Correcta, intentos):
    while intentos<0:
        contraseña=input(str("Ingrese la contraseña: "))
        if contraseña==Contraseña_Correcta:
            print("Bienvenido")
            return True
        else:
            intentos+=1
            print("Contraseña incorreta")
    else:
        print("Terminastes tus intentos, vuelve pronto")
        return False

contraseña(Contraseña_Correcta, intentos)

def agregar(Libros):
    titulo=input()
    autor=input()
    categoria=input()
    libro={"Titulo":titulo,"Autor":autor,"Categoria":categoria}
    Libros.append=(libro)
    print("El libro fue guardo con exito")

def buscar_titulo(Libros):
    fetch_titulo=input("Ingrese el titulo del libro: ")
    encontrados = [libro for libro in libros if libro["Titulo"].lower() == fetch_titulo.lower()]
    if encontrados:
        for libro in encontrados:
            print(libro)
        else:
            print("No se encontro el libro.")

def buscar_autor(Libros):
    fetch_autor=input("Ingrese el nombre del autor del libro: ")
    encontrados = [libro for libro in libros if libro["Autor"].lower() == fetch_autor.lower()]
    if encontrados:
        for libro in encontrados:
            print(libro)
        else:
            print("No se encontro el libro.")



def buscar_categoria(Libros):
    fetch_categoria=input("Ingrese la categoria de los libros a buscar: ")
    encontrados = [libro for libro in libro if libro[Categoria].lower()== fetch_categoria.lower()]
    if encontrados:
        for libro in encontrados:
            print(libro)
        else:
            print("No existen libros de esta categoria.")

def eliminar_libro(libros):
    eliminar=input("Ingrese el nombre del libro a eliminar: ")
    for libro in libros:
        if eliminar.lower() == libro["Titulo"].lower():
            opcion=input("Se encontro el libro que deseas eliminar, ¿Estas seguro de realizar esta acción?.")
            print("1: Si")
            print("2: No")
            if opcion==1:
                print("Se elimino el libro con exito")
                return
            else:
                return
        else:
            print("No se encontro el libro")


def mostrar_todos():
    if Libros:
        for libro in Libros:
          print(libro)
    else:
        print("No hay libros registrados en la biblioteca.")


def menu():
    print("\nBienvenido al Sistema de Gestión de Biblioteca")
    if contraseña():
        while True:
            print("\nMenú:")
            print("1. Agregar libro")
            print("2. Buscar libro por título")
            print("3. Buscar libro por autor")
            print("4. Buscar libro por categoría")
            print("5. Eliminar libro")
            print("6. Mostrar todos los libros")
            print("7. Salir")
            opcion = input("Seleccione una opción: ")
            if opcion == "1":
                agregar()
            elif opcion == "2":
                buscar_titulo()
            elif opcion == "3":
                buscar_autor()
            elif opcion == "4":
                buscar_categoria()
            elif opcion == "5":
                eliminar_libro()
            elif opcion == "6":
                mostrar_todos()
            elif opcion == "7":
                print("¡Hasta luego!")
                break
            else:
                print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu()