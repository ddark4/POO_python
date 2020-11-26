from tkinter import*
#-----------------------------------------------------
'''lista=[1,2,3,4,"hola",2,2]
conjunto=set(lista)
print(conjunto)
#-----------------------------------------------------
lista=[1,2,3,4,"hola",2,2]
conjunto=set(lista)
lista= list(conjunto)
print(conjunto)
#-----------------------------------------------------
class Persona(object):
    nombres="Cristian"
    apellidos="Correa"
    genero="Masculino"
    def mostrar_nombres(self):
        print(self.nombres)
#-----------------------------------------------------
class vehiculo:
    largochasis=250
    anchochasis=120
    ruedas=4
    encamino=False
    def funcion(self):
        self.encamino=True
    def estado(self):
        if (self.encamino):
            return"El carro esta en marcha"
        else:
            return "El carro esta estático"
        pass
auto=vehiculo()
print("El largo de vehiculo es:",auto.largochasis)
print("El vehiculo tiene de ruedas:",auto.ruedas)
auto.funcion()
print(auto.estado())
print("----------------------------------------------------------------------------------")
auto2=auto
print("El largo de vehiculo es:",auto2.largochasis)
print("El vehiculo tiene de ruedas:",auto2.ruedas,"ruedas")
print(auto2.estado())
#-----------------------------------------------------------
class notas:
    evaluacion=5
    saber=5
    hacer=5
    recupera=False
    def funcion(self):
        self.recupera=False
    def final(self):
        if (self.recupera):
            return"Cristian debe recuperar con Rosalba TuT"
        else:
            return"Cristian pasó derechito wepajeeeeeee"
        pass
cris=notas()
print("La evaluación de Cristian quedó en: ", notas.evaluacion)
print("La nota del Saber le quedó en: ",notas.saber)
print("La nota del Hacer le quedó en: ",notas.hacer)
cris.funcion()
print(cris.final())
#-----------------------------------------------------------
millas_recorridas = input("Introduce las millas recorridas: ")
millas_recorridas = float(millas_recorridas)
galones_usados = input("Introduce los galones usados: ")
galones_usados = float(galones_usados)
mpg = millas_recorridas / galones_usados
print("Millas por galon:", mpg)
#------------------------------------------------------------
#Clases y objetos
class latinos():
    nombre= ""
    genero = ""
    edad= ""
    pass
persona=latinos()
persona.nombre=str (input("Digite su nombre"))
persona.genero=str(input("Digite su género"))
persona.edad=int(input("Digite su edad"))
print(f"Su nombre es: {persona.nombre}, su género es:{persona.genero}, su edad es:{persona.edad}")'''
#--------------------------------------------------------------
ventana=Tk()
ventana.geometry("600x500")
ventana.title("Aplicación")
Boton1=Button(ventana,text="Inicio")
Boton1.grid(row=8,column=8)
Boton2=Button(ventana,text="Archivos")
Boton2.grid(row=8,column=1)
ventana.mainloop()