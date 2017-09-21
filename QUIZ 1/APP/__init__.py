palabra = "BALBOA"
print(" ")

print("TENDRAS 3 TURNOS PARA ADIVINAR MI PALABRA ...SECRETA....")
print("")

for x in range(3):
     intentos= input("ingresa tus locuras :) : ")
     if intentos.upper() == palabra:
         print("QUE SUERTE TIENES...")
         break

     if intentos.upper() != palabra:
         print("te falta calle")
         print(" ")
