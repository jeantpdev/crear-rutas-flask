
# Creador de ruta, controlador y modelo en flask

El proyecto ayuda a crear de manera rapida y facil las rutas que usamos en nuestra API creada con Flask usando el patrón Modelo, Ruta Controlador (MVC)



## Authors

- [@jeantpdev](https://www.github.com/jeantpdev)


## Usos/Ejemplos

Se usa con argumentos mediante la terminal.

Con esta estructura de referencia:
```
└── proyecto-mvc/
    ├── controllers/
    │   └── usuarios_controlador.py
    ├── models/
    │   └── usuarios_modelo.py
    └── routes/
        └── usuarios_rutas.py
```

Argumentos:

- ruta_proyecto: Ruta donde se encuentra nuestro proyecto. **Ejemplo:C:\Users\proyectos\python\proyecto-mvc**

- archivo_modificar: Nombre del archivo de nuestro proyecto al que modificaremos. **Ejemplo: "usuarios"**

- http-tipo: Tipo de peticion HTTP. **Ejemplo: "delete"**

- nombre_ruta: Nombre de la ruta que se creara. **Ejemplo "eliminar-usuario"**

Uso:
```cmd
py app.py <ruta-proyecto> <archivo_modificar> <http-tipo> <nombre_ruta>
```

Ejemplo
```cmd
py app.py "C:\Users\proyectos\python\proyecto-mvc" "iniciar_sesion" "delete" "eliminar_usuarios_de_lideres"
```
![Diagrama de flujo](https://res.cloudinary.com/dkuw4zg2h/image/upload/v1717016715/Proyectos/api-sql-crm/igxqgva78ulvrci6cpoj.png)

#### **Por mejorar**
