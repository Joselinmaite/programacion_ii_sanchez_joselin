Programación II - Repositorio de Proyectos

Bienvenido al repositorio principal de la materia Programación II. Este espacio está destinado al almacenamiento, organización y seguimiento de los proyectos y subproyectos desarrollados a lo largo del curso.

🛠️ Tecnologías Principales

En esta asignatura trabajaremos con el ecosistema de Python, abarcando desde el desarrollo de scripts fundamentales hasta la creación de aplicaciones web estructuradas y sistemas ERP empresariales.

🐍 Python

Python es un lenguaje de programación multiparadigma, de alto nivel e interpretado, conocido por su sintaxis clara, legible y eficiente. En este curso se utiliza como lenguaje base para aplicar conceptos de Programación Orientada a Objetos (POO), manejo de estructuras de datos y lógica de desarrollo.

🎸 Django

Django es un framework web de alto nivel escrito en Python que fomenta un desarrollo rápido y un diseño limpio y pragmático. Sigue el patrón de arquitectura MVT (Modelo-Vista-Template) e incluye un ORM (Object-Relational Mapping), sistema de autenticación y panel de administración listo para usar.

📦 Odoo

Odoo es una suite completa de aplicaciones empresariales de código abierto basada en Python y PostgreSQL. Permite construir y personalizar módulos ERP (Enterprise Resource Planning) para la gestión de ventas, inventario, contabilidad y procesos de negocio a través de una arquitectura modular y extensible.

📂 Estructura del Repositorio

El repositorio está organizado por carpetas y subcarpetas para facilitar el control de versiones de cada unidad temática o proyecto individual:

.
├── 01_python_avanzado/      # Ejercicios y proyectos base en Python
├── 02_django_proyectos/     # Aplicaciones y proyectos web con Django
├── 03_odoo_modulos/         # Módulos y desarrollos personalizados para Odoo
├── .gitignore               # Exclusión de archivos temporales, entornos virtuales y BD
└── README.md                # Documentación general del repositorio


🚀 Requisitos Previos

Para ejecutar los proyectos de este repositorio de manera local, asegúrate de contar con:

Python 3.10+

PostgreSQL (necesario para la ejecución de proyectos de Odoo)

Git para el control de versiones

⚙️ Configuración del Entorno de Trabajo

Clonar el repositorio:

git clone <URL_DEL_REPOSITORIO>
cd <NOMBRE_DEL_REPOSITORIO>


Crear y activar un entorno virtual:

python -m venv venv
# En Linux/macOS:
source venv/bin/activate
# En Windows:
.\venv\Scripts\activate


Instalar dependencias:
Ingresa a la subcarpeta del proyecto correspondiente e instala los requerimientos especificados en su propio directorio.