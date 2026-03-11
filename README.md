# 🔗 URL Shortener — сервис коротких ссылок

<p align="center">
  <img src="https://img.shields.io/badge/python-3.14+-blue?style=for-the-badge&logo=python" alt="Python">
  <img src="https://img.shields.io/badge/FastAPI-0.115+-green?style=for-the-badge&logo=fastapi" alt="FastAPI">
  <img src="https://img.shields.io/badge/PostgreSQL-17+-blue?style=for-the-badge&logo=postgresql" alt="PostgreSQL">
  <img src="https://img.shields.io/badge/Docker-ready-blue?style=for-the-badge&logo=docker" alt="Docker">
  <img src="https://img.shields.io/badge/license-MIT-yellow?style=for-the-badge" alt="License">
</p>

<p align="center">
  Простой и эффективный микросервис для сокращения длинных ссылок.<br>
  Работает на <b>FastAPI</b> + <b>PostgreSQL</b>, умеет считать переходы и отдавать статистику.
</p>

---

## ✨ Возможности

- ✅ **Сокращение ссылок** — отправляйте длинный URL, получайте короткий идентификатор (6 символов).
- 🔀 **Редирект** — переход по короткой ссылке мгновенно перенаправляет на оригинал.
- 📊 **Статистика** — для каждой ссылки хранится количество переходов (эндпоинт `/stats/{id}`).
- 🔒 **Автоматическая нормализация** — если ссылка передана без `http://` или `https://`, сервис сам добавит `https://`.
- 🌐 **Веб-интерфейс** — удобная страница для создания ссылок и просмотра статистики.
- 🐳 **Готов к Docker** — запуск одной командой `docker-compose up`.
- 🧪 **Покрытие тестами** — модульные и интеграционные тесты на `pytest`.

---

## 🛠️ Технологический стек

| Компонент       | Технология                              |
|------------------|-----------------------------------------|
| **Язык**         | Python 3.14+                            |
| **Фреймворк**    | FastAPI                                 |
| **База данных**  | PostgreSQL 17+ / asyncpg                |
| **ORM**          | SQLAlchemy 2.0 (асинхронная)            |
| **Миграции**     | Alembic (опционально)                    |
| **Тестирование** | pytest, pytest-asyncio, httpx, aiosqlite |
| **Контейнеры**   | Docker, Docker Compose                   |
| **Фронтенд**     | HTML, CSS, JavaScript (без фреймворков)  |

---

## 🚀 Быстрый старт

### 📋 Предварительные требования

- **Git** – [скачать](https://git-scm.com/downloads)
- **Docker** + **Docker Compose** – [Docker Desktop](https://www.docker.com/products/docker-desktop/)
- **Python 3.14+** (только для локального запуска)

### 🐳 Запуск одной командой (Docker Compose)
**Если используете uv (рекомендуется):**
```bash
git clone https://github.com/Sergeywws13/tz-gradient-tech.git
cd tz-gradient-tech
cp .env.example .env
uv sync  # Установка зависимостей
docker-compose up -d
```

## Обычный pip:
```bash
git clone https://github.com/Sergeywws13/tz-gradient-tech.git
cd tz-gradient-tech
cp .env.example .env
pip install -r requirements.txt
docker-compose up -d
```

## 🛑 Остановка
```bash
docker-compose down
```



