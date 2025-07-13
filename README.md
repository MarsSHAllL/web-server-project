# 🧪 Тестовая HTML-форма с серверной обработкой и автотестами

## 📋 Описание

Проект представляет собой простую веб-форму на HTML с обработкой данных на стороне Python-сервера и двумя видами тестов:

- Юнит-тесты для проверки логики сервера (`test_server.py`)
- Selenium UI-тесты для проверки взаимодействия пользователя с веб-страницей (`test_selenium.py`)

## 📁 Структура проекта
.
├── index.html # HTML-страница с формой
├── server.py # Сервер на базе http.server
├── test_server.py # Юнит-тесты логики обработки формы
├── test_selenium.py # Selenium-тест взаимодействия через браузер
└── README.md # Описание проекта

---

## 🚀 Запуск проекта

### 1. Установите зависимости

Создайте и активируйте виртуальное окружение (опционально):

bash
python -m venv .venv
.\.venv\Scripts\activate  # Windows
source .venv/bin/activate # Linux/macOS

Установите зависимости:
pip install selenium webdriver-manager

### 2. Запуск сервера
python server.py

🧪 Тестирование
Юнит-тест сервера
bash
python test_server.py
UI-тест через Selenium
Перед запуском убедитесь, что сервер (server.py) уже запущен!

bash
python test_selenium.py
⚠️ Убедитесь, что установлен браузер Chrome и соответствующий драйвер (используется webdriver-manager).⚠️

💡 Что делает сервер?
Отдаёт страницу "index.html" при переходе на "/"

При POST-запросе на "/submit" читает поля name и email

Возвращает HTML с подставленными данными:
Привет, [имя]! Твой email: [email]

🧰 Используемые технологии
Python 3.x
HTML5
http.server (встроенный модуль Python)
unittest (встроенный фреймворк тестирования)
Selenium (UI-тестирование)
webdriver-manager (автоматическое управление ChromeDriver)
