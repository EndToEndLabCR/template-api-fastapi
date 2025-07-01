# template-api-fastapi
A lightweight FastAPI starter kit with PostgreSQL integration, Flyway migrations, and containerization powered by Docker for streamlined and scalable backend development.

## 📑 Table of Contents

- [✨ Features](#-features)
- [🛠️ Technologies Used](#-technologies-used)
- [🚀 Getting Started](#-getting-started)
  - [⚙️ Prerequisites](#-prerequisites)
  - [💾 Installation](#-installation)
  - [🏃 Running the App](#-running-the-app)
- [👾 Usage](#-usage)
- [📝 Configuration](#-configuration)
- [🔗 Important Links to Have at Hand](#-important-links-to-have-at-hand)
- [📚 Additional Links](#-additional-links)
- [🤝 Contributing](#-contributing)

## ✨ Features

- Dockerized Backend
- RESTful API (FastAPI)
- Flyway for Schema Versioning

## 🛠️ Technologies Used

- [Python](https://www.python.org)
- [FastAPI](https://fastapi.tiangolo.com)
- [SQLAlchemy](https://www.sqlalchemy.org)
- [Pydantic](https://docs.pydantic.dev/latest/)
- [Docker](https://www.docker.com)
- [Gunicorn](https://gunicorn.org)
- [Flyway](https://brunomendola.github.io/flywaydb.org/documentation/)
- [PostgreSQL](https://www.postgresql.org)

## 🚀 Getting Started

### ⚙️ Prerequisites

All core services and dependencies are containerized, so you only need the following installed on your local machine to run the project:

- Docker – For building and running containers
- Flyway – Optional locally, but included in the container setup for database migrations
- Git – To clone the repository and manage version control

All other components—Python, FastAPI, SQLAlchemy, Pydantic, Gunicorn, and PostgreSQL—are pre-configured and run inside the container.
No need to install them globally.

### 💾 Installation

Create a fork of this repository.

Then:

```sh
# Clone the repository in your local machine
git clone https://github.com/your-username/template-api-fastapi.git
cd template-api-fastapi
```

### 🏃 Running the App

- Create the pip environment:

```sh
python -m venv venv
```

- Activate the pip environment:

```sh
source venv/bin/activate
```

- Update pip (optional-recommended):

```sh
pip install --upgrade pip
```

- Install the project's dependencies:

```sh
pip install -r requirements.txt
```

- Deactivate virtual environment:

```sh
deactivate
```

### Docker

Run locally using Docker:

- Delete any containers to avoid cache (no required if it is the first time running this project):

```sh
docker compose down
```

- Build the project:

```sh
docker compose up
```

## 👾 Usage

- If everything runs smoothly, you’ll see your containers up and running, ready to serve your backend.

<img width="1213" alt="Screenshot 2025-07-01 at 00 14 07" src="https://github.com/user-attachments/assets/1e8634de-179e-481d-b413-4bc83764ef7b" />

- Once the containers are running, navigate to <http://localhost:8080/docs> to access the auto-generated OpenAPI interface and interact with the API endpoints.

<img width="1443" alt="Screenshot 2025-07-01 at 00 23 24" src="https://github.com/user-attachments/assets/8465386f-d12b-40c9-b6cd-2b271272ea7b" />

## 📝 Configuration

Here’s what your .env file should look like with the required variables:
- Example:
```sh
  APP_ENV=local

  POSTGRES_DB_HOST=postgres
  POSTGRES_DB_PORT=5432
  POSTGRES_DB_NAME=template-api-fastapi
  POSTGRES_DB_USERNAME=admin
  POSTGRES_DB_PASSWORD=password
```

To connect to the database using PgAdmin 4, configure the connection with the following settings:

- General:

<img width="700" alt="Screenshot 2025-07-01 at 00 37 30" src="https://github.com/user-attachments/assets/dfbcb099-2564-4119-9718-0cd0cdb579e2" />

- Connection:
  
<img width="700" alt="Screenshot 2025-07-01 at 00 37 56" src="https://github.com/user-attachments/assets/5bd82d64-8e75-4fb4-923a-1db210d51823" />

## 🔗 Important Links to Have at Hand

- [Open Issues](https://github.com/EndToEndLabCR/template-api-fastapi/issues)
- [Open Pull Requests](https://github.com/EndToEndLabCR/template-api-fastapi/pulls)

## 📚 Additional Links

- [Commits Guide](https://github.com/EndToEndLabCR/documentation/blob/main/github/commits-guide.md)
- [Contributing Guide](https://github.com/EndToEndLabCR/documentation/blob/main/docs/contributions-guidelines.md)
- [Code of Conduct](https://github.com/EndToEndLabCR/template-api-fastapi?tab=coc-ov-file#readme)

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/YourFeature`
3. Commit your changes: `git commit -am 'Add feature'`
4. Push to the branch: `git push origin feature/YourFeature`
5. Open a pull request

---

_Built with ❤️ by [Derian Campos](https://github.com/DerianCampos)_
