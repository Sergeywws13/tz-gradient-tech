# 🔗 URL Shortener — сервис коротких ссылок

<p align="center">
  <img src="https://img.shields.io/badge/python-3.14+-blue?style=for-the-badge&logo=python" alt="Python">
  <img src="https://img.shields.io/badge/FastAPI-0.115+-green?style=for-the-badge&logo=fastapi" alt="FastAPI">
  <img src="https://img.shields.io/badge/PostgreSQL-15+-blue?style=for-the-badge&logo=postgresql" alt="PostgreSQL">
  <img src="https://img.shields.io/badge/Docker-ready-blue?style=for-the-badge&logo=docker" alt="Docker">
  <img src="https://img.shields.io/badge/license-MIT-yellow?style=for-the-badge" alt="License">
</p>

<p align="center">
  Простой и эффективный микросервис для сокращения длинных ссылок.<br>
  Работает на <b>FastAPI</b> + <b>PostgreSQL</b>, умеет считать переходы и отдавать статистику.
</p>

---

## ✨ Возможности

- ✅ **Сокращение ссылок** — отправляй длинный URL, получай короткий ID (6 символов).
- 🔀 **Редирект** — переход по короткой ссылке мгновенно перенаправляет на оригинал.
- 📊 **Статистика** — для каждой ссылки хранится количество переходов (`/stats/{id}`).
- 🔒 **Автоматическая нормализация** — если ссылка без `http://` или `https://`, сервис сам добавит `https://`.
- 🌐 **Веб-интерфейс** — удобная страница для создания ссылок и просмотра статистики.
- 🐳 **Готов к Docker** — запуск одной командой `docker-compose up`.
- 🧪 **Покрытие тестами** — модульные и интеграционные тесты на `pytest`.

---

## 🛠️ Технологический стек

| Компонент       | Технология                              |
|------------------|-----------------------------------------|
| **Язык**         | Python 3.11+                            |
| **Фреймворк**    | FastAPI                                 |
| **База данных**  | PostgreSQL + asyncpg                    |
| **ORM**          | SQLAlchemy 2.0 (асинхронная)             |
| **Миграции**     | Alembic (опционально)                    |
| **Тестирование** | pytest, pytest-asyncio, httpx, aiosqlite |
| **Контейнеры**   | Docker, Docker Compose                   |
| **Фронтенд**     | HTML, CSS, JavaScript (без фреймворков)  |

---

## 🚀 Быстрый старт

### 🔧 Локальный запуск

1. **Клонируй репозиторий**
   ```bash
   git clone https://github.com/username/url-shortener.git
   cd url-shortener

