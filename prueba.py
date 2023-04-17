import os
import sys

mensaje_de_bienvenida = """
***************************************
             BIENVENIDO
***************************************
"""

print(mensaje_de_bienvenida)

contra = int(float(input("Ingrese la contraseña: ")))

if contra == 2023:
    while True:
        print("\nElija una opción:")
        print("1. Crear nuevo archivo")
        print("2. Abrir archivo txt")
        print("3. Agregar información a un archivo")
        print("4. Eliminar archivo")
        print("5. Salir")
        user_choice = input("> ")

        if user_choice == "1":
            file_name = input("¿Qué nombre le dará al archivo?: ")
            with open(file_name, 'w') as f:
                pass
            print(f"{file_name} se ha creado exitosamente!")

        elif user_choice == "2":
            file_list = os.listdir()
            print("Archivos disponibles:")
            for file_name in file_list:
                if file_name.endswith(".txt"):
                    print(file_name)
            file_name = input("¿Cuál es el nombre del archivo que desea abrir?: ")
            if os.path.exists(file_name):
                with open(file_name, 'r') as f:
                    print(f.read())
            else:
                print(f"{file_name} no existe.")

        elif user_choice == "3":
            file_list = os.listdir()
            print("Archivos disponibles:")
            for file_name in file_list:
                if file_name.endswith(".txt"):
                    print(file_name)
            file_name = input("¿Qué archivo desea editar?: ")
            if os.path.exists(file_name):
                with open(file_name, 'a') as f:
                    new_text = input("Introduzca el nuevo texto: ")
                    f.write(new_text)
                print(f"{file_name} editado exitosamente!")
            else:
                print(f"{file_name} no existe.")

        elif user_choice == "4":
            file_list = os.listdir()
            print("Archivos disponibles:")
            for file_name in file_list:
                if file_name.endswith(".txt"):
                    print(file_name)
            file_name = input("¿Qué archivo desea eliminar?: ")
            if os.path.exists(file_name):
                os.remove(file_name)
                print(f"{file_name} ha sido eliminado exitosamente!")
            else:
                print(f"{file_name} no existe.")

        elif user_choice == "5":
            print("Saliendo del programa...")
            sys.exit()

        else:
            print("Inténtelo otra vez.")

else:
    print("Contraseña incorrecta")
    sys.exit()
