class Ruta:
    
    def sacar_blueprint(ruta_archivo):
        with open(ruta_archivo, 'r', encoding='utf-8') as archivo_entrada:
            contenido = archivo_entrada.readlines()

            for linea in contenido:
                if "= Blueprint" in linea:
                    nose = linea.split(" ")
                    blueprint = nose[0].strip()
        return blueprint

    def sacar_nombre_controlador(ruta_archivo):
        with open(ruta_archivo, 'r', encoding='utf-8') as archivo_entrada:
            contenido = archivo_entrada.readlines()

            for linea in contenido:
                if "()" in linea:
                    nose = linea.split("\n")
                    nose2 = nose[0]
                    nose3 = nose2.split(" ")
                    nombre_controlador = nose3[0]
                    break

            return nombre_controlador
        
    def crear_ruta_api(nombre):
        return nombre.replace("_", "-")

    def ruta_final(blueprint, ruta_api, tipo, nombre, nombre_controlador):
        ruta = f"""

@{blueprint}.route('/{ruta_api}/', methods=['{tipo.upper()}'])
@cross_origin()
def {tipo}_{nombre}():
    return {nombre_controlador}.{tipo}_{nombre}()
    """
        return ruta