#Si el email de una persona son sus nombres, en minúscula separados por un punto. Seguido de @ y el nombre de la empresa
#En minuscula, .dominio . Como podría automatizarse?
nombre=input("Ingrese su nombre \n")
empresa=input("Ingrese el nombre de su empresa \n")
dominio=input("Ingrese el dominio de su correo \n")
nombre=nombre.strip().lower().split() #Puedo utilizar varios metodos a la ves!!
empresa=empresa.strip().lower().split()
dominio=dominio.strip().lower().split()
correo=".".join(nombre)+"@"+"".join(empresa)+"".join(dominio)
print(correo)
