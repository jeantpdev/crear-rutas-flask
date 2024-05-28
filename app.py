# Description: Este archivo sirve para poder crear ruta, controlador y modelo de un proyecto Flask.
# start_date: 27/05/2024 6:44pm
# author: Jean Trujillo
import os
import sys
from utils.ruta import *
from utils.archivo import *

def crear_ruta(ruta_archivo, tipo, nombre):
    print("Sacando nombre del blueprint...")
    blueprint = Ruta.sacar_blueprint(ruta_archivo)
    print("Nombre del blueprint", blueprint)

    print("Sacando nombre del controlador...")
    nombre_controlador = Ruta.sacar_nombre_controlador(ruta_archivo)
    print("Nombre del controlador", nombre_controlador)

    print("Creando ruta de la API...")
    ruta_api = Ruta.crear_ruta_api(nombre)
    print("Ruta API", ruta_api)

    print("Creando ruta final...")
    texto = Ruta.ruta_final(blueprint, ruta_api, tipo, nombre, nombre_controlador)
    print(texto)

    Archivo.modificar_archivo(ruta_archivo, texto)

    # Abrir el archivo en modo append (agregar al final) y escribir la nueva ruta
    #with open(ruta_archivo, 'a', encoding='utf-8') as archivo_salida:
    #    archivo_salida.write(ruta)


    
# Se lee la ruta de las carpetas que contienen "modelo" y el entorno a modificar
def leer_archivo(ruta_proyecto, nombre_archivo, tipo, nombre):
    for dirpath, dirnames, filenames in os.walk(ruta_proyecto):

        if 'routes' in dirpath and 'pycache' not in dirpath:
            for filename in filenames:
                if nombre_archivo in filename:
                    ruta_archivo = os.path.join(dirpath, filename)
                    crear_ruta(ruta_archivo, tipo, nombre)

        if 'controllers' in dirpath and 'pycache' not in dirpath:
            for filename in filenames:
                if nombre_archivo in filename:
                    ruta_archivo = os.path.join(dirpath, filename)
        
        if 'models' in dirpath and 'pycache' not in dirpath:
            for filename in filenames:
                if nombre_archivo in filename:
                    ruta_archivo = os.path.join(dirpath, filename)


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Uso: py app.py <ruta_proyecto> <nombre_archivo> <type> <nombre>")
        sys.exit(1)

        
#print("Uso: py entorno.py <ruta_proyecto> <nombre> <tipo>")

    ruta_proyecto = sys.argv[1]
    nombre_archivo = sys.argv[2]
    tipo = sys.argv[3]
    nombre = sys.argv[4]
    leer_archivo(ruta_proyecto, nombre_archivo, tipo, nombre)