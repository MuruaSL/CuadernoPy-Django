Mis Cuadernos: Py + Django

Sitio web personal desarrollado en Django para organizar clases, cursos y contenidos técnicos. Funciona como una biblioteca digital con navegación por categorías, cursos y clases.

INSTALACIÓN Y EJECUCIÓN DEL PROYECTO

    Clonar el repositorio:
    git clone https://github.com/tu_usuario/tu_repo.git
    cd tu_repo

    Crear y activar entorno virtual:

Windows:
python .venv\Scripts\activate

Linux/Mac:
python3 -m venv .venv
source .venv/bin/activate

    Instalar dependencias:
    pip install -r requirements.txt

    Ejecutar migraciones:
    python manage.py migrate

    Crear superusuario (opcional):
    python manage.py createsuperuser

    Iniciar servidor:
    python manage.py runserver

Abrí el navegador en: http://127.0.0.1:8000

¿CÓMO NAVEGAR EL SITIO?

INICIO
URL: /
Bienvenida general y botón para ver cursos.

CURSOS
URL: /cursos/
Lista todos los cursos organizados por categorías.

CURSO (DETALLE)
URL: /curso/<id>/
Muestra las clases asociadas al curso seleccionado.

CLASE (DETALLE)
URL: /clase/<id>/
Contenido completo con estilo tipo carpeta, e imagen de cabecera del curso.

SOBRE MÍ
URL: /sobremi/

FUNCIONALIDADES ADMINISTRATIVAS

Acceso desde la barra de navegación → Administrativo:

    Crear Categoría: /crear_categoria/

    Crear Curso: /crear_curso/

    Crear Clase: /crear_clase/

    Admin de Django: /admin/

MODELOS

    Categoría: agrupa varios cursos.

    Curso: agrupa varias clases. Tiene título, descripción e imagen.

    Clase: contenido textual, imagen opcional, título y descripción.

ESTILO GENERAL

    Diseño sobrio con fondo oscuro y texto claro.

    Banner personalizado por página.

    Favicon ubicado en: core/static/core/img/favicon.ico

    Responsive con Bootstrap 5.3.

    Tipografías y sombras para una lectura cómoda.

DEPENDENCIAS

Las dependencias necesarias están en requirements.txt (ya actualizado), por ejemplo:

Django>=4.2
Pillow

Instalación:
pip install -r requirements.txt

AUTOR

Sergio Murua
Proyecto personal de práctica y documentación técnica.