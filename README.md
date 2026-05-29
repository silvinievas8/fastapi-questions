# Proyecto API de Preguntas
Este proyecto consiste en una API REST desarrollada con **FastAPI** que gestiona un dataset de preguntas técnicas almacenadas en una base de datos **PostgreSQL**.

## Estructura del Proyecto
- **FastAPI**: Framework para la creación de la API.
- **SQLAlchemy**: ORM para la gestión de la base de datos.
- **Docker**: Contenedor para la base de datos PostgreSQL.
- **Poetry**: Gestión de dependencias y entorno virtual.
- **Pandas**: Procesamiento de datos desde Hugging Face.

## Cómo ejecutar el proyecto localmente
1. **Levantar la base de datos**: 
   `docker compose up -d`
2. **Instalar dependencias**: 
   `poetry install`
3. **Cargar los datos iniciales**: 
   `$env:PYTHONPATH = "."; poetry run python app/load_data.py`
4. **Iniciar el servidor**: 
   `$env:PYTHONPATH = "."; poetry run uvicorn app.main:app --reload`

## Endpoints principales
- `GET /questions`: Listado de todas las preguntas.
- `GET /questions/{id}`: Detalle de una pregunta específica.
- `GET /docs`: Documentación interactiva (Swagger UI).
