# Cuaderno Py + Django

Sitio web personal desarrollado con Django para organizar clases, cursos y contenidos técnicos. Funciona como una biblioteca digital, con navegación jerárquica por categorías, cursos y clases. Está orientado tanto a la práctica profesional como al aprendizaje.

---

## 🛠 Instalación y ejecución del proyecto

1. **Clonar el repositorio:**  
```bash
git clone https://github.com/MuruaSL/CuadernoPy-Django.git
cd CuadernoPy-Django
```

2. **Crear y activar entorno virtual:**

**Windows:**  
```bash
python -m venv .venv
.venv\Scripts\activate
```

**Linux/Mac:**  
```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. **Instalar dependencias:**  
```bash
pip install -r requirements.txt
```

4. **Ejecutar migraciones:**  
```bash
python manage.py migrate
```

5. **Crear superusuario (opcional):**  
```bash
python manage.py createsuperuser
```

6. **Iniciar servidor de desarrollo:**  
```bash
python manage.py runserver
```

Accedé desde tu navegador: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 🧭 ¿Cómo navegar el sitio?

- **Inicio:** `/`  
  Página de bienvenida con acceso a los cursos.

- **Cursos:** `/cursos/`  
  Lista de cursos organizados por categorías.

- **Detalle de curso:** `/curso/<id>/`  
  Muestra las clases relacionadas al curso.

- **Detalle de clase:** `/clase/<id>/`  
  Contenido completo estilo carpeta, con imagen y descripción.

- **Sobre mí:** `/sobremi/`  
  Perfil del autor con biografía, avatar y datos personales.

---

## 🔧 Funcionalidades administrativas

Accesibles desde la barra de navegación (con usuario autenticado):

- Crear Categoría: `/crear_categoria/`
- Crear Curso: `/crear_curso/`
- Crear Clase: `/crear_clase/`
- Panel Django: `/admin/`

Otras funciones:

- Editar perfil (nombre, bio, fecha de nacimiento)
- Subir avatar
- Cambiar contraseña
- Contenido enriquecido con CKEditor

---

## 📦 Modelos implementados

- **Categoría:** agrupa múltiples cursos.  
- **Curso:** título, descripción enriquecida y una imagen.  
- **Clase:** contenido enriquecido (rich text), imagen opcional, título y descripción.

---

## 🎨 Estilo y diseño

- Interfaz oscura, moderna y responsiva (Bootstrap 5.3).
- Banners personalizados por página.
- Tipografías legibles y sombras suaves.
- Favicon en: `core/static/core/img/favicon.ico`

---

## 🔐 Autenticación y seguridad

- Registro, login y logout.
- Cambio de contraseña (`PasswordChangeView`).
- Rutas protegidas con `@login_required`.
- Perfil personalizado con avatar, bio y fecha de nacimiento.
- Validación de formularios con mensajes.

---

## 📋 Dependencias principales

- Django >= 4.2  
- Pillow  
- django-ckeditor  

Instalación:  
```bash
pip install -r requirements.txt
```

---

## 👤 Autor

**Sergio Murua**  
Proyecto personal de práctica y documentación técnica.

---

## ✅ Checklist de funcionalidades

| Requisito                        | Estado |
|----------------------------------|--------|
| Herencia de templates            | ✅     |
| Navbar común                     | ✅     |
| Páginas públicas (Home, About)   | ✅     |
| CRUD con CBVs                    | ✅     |
| Uso de 2 CBVs mínimo             | ✅     |
| Decorador `@login_required`      | ✅     |
| Cambio de contraseña             | ✅     |
| Texto enriquecido (CKEditor)     | ✅     |
| Campo de fecha (birth_date)      | ✅     |
| Mensaje si no hay objetos        | ✅     |
| Perfil con avatar y bio          | ✅     |
| Registro, Login, Logout          | ✅     |
| Admin con modelos registrados    | ✅     |
| Git + README + requirements.txt  | ✅     |
