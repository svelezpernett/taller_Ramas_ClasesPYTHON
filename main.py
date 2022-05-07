from clases.Ciclista import Ciclista
from operator import attrgetter

arregloCiclistas=[]

def ingresarCiclista():
    e=input("Presione cualquier tecla para ingresar los datos del ciclista y * al terminar")

    while(e!="*"):
        ciclista=Ciclista("egan Bernal", "22", "Colombia", "Eneos", 122)
        
        nombre=input("ingrese el nombre ")
        edad=input("ingrese la edad ")
        pais=input("ingrese el pais ")
        equipo=input("ingrese el equipo ")
        tiempo=int(input("ingrese el tiempo"))

        ciclista.nombre=nombre
        ciclista.edad=edad
        ciclista.pais=pais
        ciclista.equipo=equipo
        ciclista.tiempo=tiempo

        arregloCiclistas.append(ciclista)

        e=input("Ingrese * para finalizar o cualquier tecla para añadir otro ciclista")

    
    for objeto in arregloCiclistas:
        print(objeto.nombre)
        print(objeto.edad)
        print(objeto.pais)
        print(objeto.equipo)
        print(objeto.tiempo)

    mejorTiempo=(min(arregloCiclistas, key=attrgetter('tiempo')))
    print(f"{mejorTiempo.nombre} fue el ciclista con mejor tiempo ({mejorTiempo.tiempo})")

ingresarCiclista()