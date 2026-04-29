# import random
# op=0
# cantpersonas=0
# total=0
# while op!=4:
#     print('''
#           1.- Niño (1-17) 1000
#           2.- Adulto(18-64) 3000
#           3.- Adulto Mayor (64 o mas) 1500
#           4.- Salir ''')
#     op=int(input("Seleccione una opcion "))
#     match op: 
#             case 1:
#                 cant=int(input("Ingrese la cantidad de niños "))
#                 while cant <1 or cant>10:
#                      cant=int(input("Ingrese la cantidad correctamente "))
#                 cantpersonas+=cant
#                 total+=1000*cant
#                 cant+=cantpersonas


#             case 2:
#                 cant=int(input("Ingrese la cantidad de adultos "))
#                 while cant <1 or cant>10:
#                      cant=int(input("Ingrese la cantidad correctamente "))    
#                 cantpersonas+=cant
#                 total+=3000*cant
#                 cant+=cantpersonas
#             case 3:
#                 cant=int(input("Ingrese la cantidad de adultos mayores "))
#                 while cant <1 or cant>10:
#                      cant=int(input("Ingrese la cantidad correctamente "))
#                 cantpersonas+=cant
#                 total+=1500*cant
#                 cant+=cantpersonas
#             case 4:
#                 print("Saliendo del programa")
#                 print(f"El total a pagar es {total}")
#                 print(f"La cantidad de personas es {cantpersonas}")
#             case _:
#                 print("Opcion invalida")


# preguntar el folio de una entrada a un concierto
# validar que los folios esten entre 7.000 y 21.000
# Preguntar si esa en cancha vip, cancga general , o tribuna
# Cada entrada vale 40.000 pero los impuestos son 
# vip 1.8 general 1.4 y tribuna 1.2
# mostar el valor a pagar al final

folio=int(input("Ingrese su folio: "))
while folio<7000 or folio>21000:
    print("Folio fuera de rango")
    folio=int(input("Ingrese su folio: "))
cancha=int(input(''' ¿Cual cancha es?
                 1.- Vip
                 2.- General
                 3.- Tribuna '''))    
                     
