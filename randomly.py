# adivine el numero

# crea un numero random entre 1 y 100
# pide al usuario que adivine el numero
# si el usuario pone un numero mayor al generado
# debe decir "te pasaste" en caso contrario 
# "el numero a adivinar es mayor"
# solo hay 5 posibilidades de adivinar.

import random

num=random.randint(1,100)
pos=1
guess=int(input("Adivina el numero entre 1 y 100: "))
while pos<5 and guess!=num:
    print(f"turno {pos}")
    if guess>num:
        print("Te pasaste")
    else:
        print("El numero adivinar es mayor")
    guess=int(input("Adivina el numero: "))
    while guess <1 or guess >100:
        print("Numero fuera de rango, intente nuevamente")
        guess=int(input("Adivina el numero: "))
    pos+=1
if guess==num:    
    print("Has adivinado")
else:
    print("Se te acabaron las oportunidades")    

    
