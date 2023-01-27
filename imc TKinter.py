#Calculadora para medir el indice de masa corporal con interfaz gráfica realizada con TKinter. 

import tkinter as tk

window = tk.Tk()
window.title("Indice de masa corporal")
window.geometry("750x400")

def calculo():
  try:
    peso1=float(peso.get())
    altura1=float(altura.get())
    result=(peso1/altura1**2)
    result=round(result,2)
    resultado["text"]="\nSu IMC es de\n"+str(result)
    info["text"]="\nINFORMACION SOBRE IMC\n\nPeso inferior al normal: Menos de 18.5\n\nNormal: 18.5 – 24.9\n\nPeso superior al normal: 25.0 – 29.9\n\nObesidad: Más de 30.0"
  except:
    resultado["text"]="Solo es posible ingresar datos numericos"

peso_etiqueta = tk.Label(text="Ingrese su peso en Kilogramos")
peso_etiqueta.pack()

peso = tk.Entry()
peso.pack()

altura_etiqueta = tk.Label(text="Ingrese su altura en Metros")
altura_etiqueta.pack()

altura = tk.Entry()
altura.pack()

boton = tk.Button(text="Calcular IMC", command=calculo)
boton.pack()

resultado=tk.Label(text="",fg="red")
resultado.pack()

info=tk.Label(text="")
info.pack()

tk.mainloop()