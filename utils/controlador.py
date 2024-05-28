from utils.archivo import *

class Controlador:

    def sacar_modelo(ruta_archivo):
        contenido = Archivo.leer_lineas_archivo(ruta_archivo)

        for linea in contenido:
            if "()" in linea:
                nose = linea.split("\n")
                nose2 = nose[0]
                nose3 = nose2.split(" ")
                nombre_modelo = nose3[0]
                break

        return nombre_modelo

    def ruta_final(tipo, modelo, nombre):
        ruta = f"""

    def {tipo}_{nombre}(self):
            query = {modelo}.{nombre}()
            return query
    """
        return ruta