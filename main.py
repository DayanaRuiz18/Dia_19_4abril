#Importar libreria

import datetime
from datetime import (date,time)

a = datetime.date.today()
print("La fecha hoy es:",a,"\n")

#Leer el contenido de los dos archivos

h = open('Archivo1.txt','r')
g = h.read()
print("El contenido del archivo 1 es:\n",g,"\n")
h.close()

k = open('Archivo2.txt','r')
f = k.read()
print("El contenido del archivo 2 es:\n",f,"\n")
k.close()

#Crear dos nuevos archivos donde guardaremos la inforación de los archivo 1 y 2 además de la información que obtengamos como respuesta  

##Archivo 3
i = open('Archivo3.txt','w+')
i.write("El contenido del archivo 1 es:\n")
i.write(g)

##Archivo 4
o = open('Archivo4.txt','w+')
o.write("El contenido del archivo 2 es:\n")
o.write(f)

#Pasar la información en formato de fechas para poder trabajar con estas

##Para el archivo 1

b = datetime.date(year= 2021, month=11,day=10)
#print(b)
c = datetime.date(year= 2021, month=2,day=3)
#print(c)

i.write("\nEl contenido del archivo 1 en formato de fechas es:\n")
i.write("\nFecha 1:\n")
i.write(str(b))
i.write("\nFecha 2:\n")
i.write(str(c))

##Para el archivo 2

v = datetime.date(year= 2020, month=8,day=5)
#print(b)
x = datetime.date(year= 2020, month=6,day=17)
#print(c)

o.write("\nEl contenido del archivo 2 en formato de fechas es:\n")
o.write("\nFecha 1:\n")
o.write(str(v))
o.write("\nFecha 2:\n")
o.write(str(x))

#Realizar operaciones con las fechas del archivo 1

##Sumar 100 días a la primera fecha y 50 a la segunda

n = b + datetime.timedelta(days=100)
print(n)
m= x + datetime.timedelta(days=50)
print(m)

##Agregar la información anterior al archivo 3

i.write("\n\nSi sumamos 100 días a la fecha 1 obtenemos la fecha:\n")
i.write(str(n))
i.write("\n\nSi sumamos 50 días a la fecha 2 obtenemos la fecha:\n")
i.write(str(m))

#Realizar operaciones con las fechas del archivo 2

##Mirar cuanto tiempo ha transcurrido a partir de esa fecha hasta hoy

z = a - v
print(z)
q= a - x
print(q)

##Agregar la información anterior al archivo 4

o.write("\n\nSi restamos la fecha 1 a la fecha actual obtenemos que han trancurrido\n")
o.write(str(z))
o.write("\n\nSi restamos la fecha 2 a la fecha actual obtenemos que han trancurrido\n")
o.write(str(q))

#Cerrar y guardar la información de los archivos 3 y 4

i.close()
o.close()



