class Archivo:

    def modificar_archivo(ruta_archivo: str, texto: str):
        with open(ruta_archivo, 'a', encoding='utf-8') as archivo_salida:
            archivo_salida.write(texto)

    def leer_archivo(ruta_archivo: str):
        with open(ruta_archivo, 'r', encoding='utf-8') as archivo_entrada:
            contenido = archivo_entrada.read()
            print(contenido)

    def leer_lineas_archivo(ruta_archivo: str):
        with open(ruta_archivo, 'r', encoding='utf-8') as archivo_entrada:
            contenido = archivo_entrada.readlines()
            return contenido