Este es un proyecto web desarrollado en Django que implementa el patrón MVT (Model-View-Template) y cumple con los requisitos de la consigna: Herencia de plantillas, 3 modelos con sus formularios de inserción, y un formulario de búsqueda.

## ⚙️ Estructura del Proyecto

| Archivo | Rol |
| :--- | :--- |
| `blog/models.py` | Modelos: Autor, Categoria, Post |
| `blog/forms.py` | Formularios: AutorFormulario, CategoriaFormulario, PostFormulario, BusquedaFormulario |
| `blog/views.py` | Lógica: Maneja la inserción de datos y la búsqueda. |
| `blog/templates/blog/base.html` | Plantilla Padre (Herencia de HTML) |

## 🚀 Cómo Probar las Funcionalidades

Para probar la web, usa los siguientes comandos en la terminal de la carpeta raíz:

1. **Prepara las Tablas:** ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```
2. **Inicia el Servidor:** ```bash
    python manage.py runserver
    ```

### URLs de Prueba:

* **Inicio:** `http://127.0.0.1:8000/`
* **Crear Autor:** Ingresar datos del primer Modelo.
* **Crear Categoría:** Ingresar datos del segundo Modelo.
* **Crear Post:** Ingresar datos del tercer Modelo.
* **Buscar Post:** Permite buscar Posts por título.
