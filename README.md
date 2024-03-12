# Módulo Administrativo

Este repositorio contiene un módulo administrativo desarrollado con Django para el backend y React para el frontend. El módulo permite gestionar el personal, incluyendo la capacidad de modificar, crear, cesar y eliminar colaboradores.

## Características principales

- **Gestión de Personal**: El módulo permite llevar a cabo las siguientes operaciones relacionadas con el personal:
  - Crear nuevos colaboradores con sus datos principales.
  - Modificar la información existente de los colaboradores.
  - Cesar a colaboradores, lo que puede implicar actualizar su estado de activo a inactivo o eliminar su registro.
  - Eliminar colaboradores de forma permanente de la base de datos.

- **Datos de Colaboradores**: Cada colaborador puede tener los siguientes datos principales:
  - Nombre completo.
  - Cargo o posición dentro de la organización.
  - Información de contacto secundaria, como números de teléfono y direcciones de correo electrónico.

## Tecnologías utilizadas

- **Backend**: Desarrollado con Django, un framework de desarrollo web de Python que proporciona una arquitectura robusta y segura para el backend.
- **Frontend**: Implementado con React, una biblioteca de JavaScript para construir interfaces de usuario interactivas y de una sola página (SPA).
- **Base de Datos**: Se utiliza una base de datos relacional, preferiblemente MySQL o PostgreSQL, para almacenar los datos de los colaboradores.

## Configuración del Entorno de Desarrollo

1. **Clonar el Repositorio**: Clona el repositorio del proyecto desde GitHub:

```bash
git clone https://github.com/tu-usuario/modulo-administrativo.git
