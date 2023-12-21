Corredor = {}
while True:
    Estado = bool(int(input("Escribe 1 si  sigue en la carrera o 0 si no:")))
    if Estado ==1:
        tiempo = str(input("Tiempo:"))
        km = str(input("Km:"))
        Corredor[tiempo] = km
    elif Estado ==0:
        print("El Corredor" + "a las" + corredor.keys() + "Estaba en el km" + km)
        break
 