from utils.archivo import *

class Modelo:

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

    def ruta_final(nombre):
        ruta = f"""

    def {nombre}(self):
        try:
            print("Hola")
            return jsonify({{"saludo": "hola"}}), 200
        except Exception as e:
            print("Ocurrió un error:", e)
            return jsonify({{"mensaje": "Ocurrió un error al procesar la solicitud."}}), 500
    
    """
        return ruta