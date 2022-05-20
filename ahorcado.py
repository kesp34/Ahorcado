import time
nombre = input("¿Cómo te llamas?")
print("Muy buenas! "+nombre, "ahora te toca jugar al ahorcado")
print("")
time.sleep(2)
print("Puedes adivinar la palabra")
time.sleep(1)
print("Tienes 6 vidas para completar la palabra")
palabra='informatica'
palabra2=''
vidas=6

while vidas > 0:
    errors=0
    for lletra in palabra:
        if lletra in palabra2:
            print(lletra,end="")
        else:
            print("*",end="")
            errors+=1
    if errors==0:
        print("")
        print("Has ganado!")
        break

    letra2=input("Pon una letra: ")
    palabra2+=letra2

    if letra2 not in palabra:
        vidas-=1
        print("Has fallado")
        print("Te quedan ",+vidas, " vidas")
    if vidas == 0:
        print("Has perdido")
else:
    print("Gracias por jugar")
