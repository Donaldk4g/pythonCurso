import libreria as funci
import matplotlib.pyplot as plt

ruta="C:/Users/dogoc/Desktop/cursos/python_curso1/data.csv"

datos=funci.DataLoad(ruta)
selecion=input('ingrese el pais a graficar: ')
dato=funci.selePais(selecion,datos)

x = dato.keys()
y = dato.values()

fig, ax = plt.subplots()
ax.bar(x, y, width=1, edgecolor="white", linewidth=0.7)
plt.savefig(f"{selecion}")
plt.close()




