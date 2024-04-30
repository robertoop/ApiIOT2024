# -*- coding: utf-8 -*-
from flask import Flask

app=Flask(__name__)

@app.route("/")
def Presentacion():
  Mensaje="Esta es una api que te convierte Dias en Horas, Minutos o Segundos"
  return Mensaje

@app.route("/Horas/<Dias>")
def Conversor_Dias_Horas(Dias):
  Resultado=int(Dias)*24
  return f" {Dias} dias son {Resultado} horas"

if __name__=="__main__":
  app.run()
