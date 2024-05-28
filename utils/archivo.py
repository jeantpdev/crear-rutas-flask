class Archivo:

    def modificar_archivo(ruta_archivo: str, texto: str):
        with open(ruta_archivo, 'a', encoding='utf-8') as archivo_salida:
            archivo_salida.write(texto)