# MOC API

## Description
MOC API is a backend application developed using Python. The project provides  APIs for managing users, enrollments, documents, slots etc. It follows a modular architecture and uses Poetry for dependency management.

## Project Repository

Repository URL:
```bash
https://gitlab.com/akanksha.lokhande-coditas/moc_api.git
```

## Installation

### Prerequisites

* Python 3.12+
* Poetry
* PostgreSQL

### Clone the Repository

```bash
git clone https://gitlab.com/akanksha.lokhande-coditas/moc_api.git
cd moc_api
```

### Install Dependencies

```bash
poetry install
```

### Activate Virtual Environment

### Configure Environment Variables

Create a `.env` file in the project root and add the required configuration values.

Example:

```env
DB_DIALECT
DB_USERNAME
DB_PASSWORD
DB_NAME
DB_HOST
DB_PORT
SECRET_KEY
ALGORITHM=
ACCESS_TOKEN_EXPIRE_MINUITES
REFRESH_TOKEN_EXPIRE_DAYS
SUPERADMIN_SALUTATION
SUPERADMIN_FIRST_NAME
SUPERADMIN_LAST_NAME
SUPERADMIN_EMAIL
SUPERADMIN_PASSWORD

```
### Run the Application

```bash
poetry run uvicorn main:app --reload
```

The application will start on:

```bash
http://127.0.0.1:8000
```

## API Documentation

Swagger UI:

```bash
http://127.0.0.1:8000/docs
```

## Usage

After starting the server, you can access the API using:

* Swagger UI
* Postman

## Contributing

Contributions are welcome.

## Maintainer

Akanksha Lokhande

## License
This project is intended for educational and organizational purposes.