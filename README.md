# 🧪 <h2>Тестовая HTML-форма с серверной обработкой и автотестами</h2>

## 📋 <h2>Описание</h2>

Проект представляет собой простую веб-форму на HTML с обработкой данных на стороне Python-сервера и двумя видами тестов:

- Юнит-тесты для проверки логики сервера (`test_server.py`)
- Selenium UI-тесты для проверки взаимодействия пользователя с веб-страницей (`test_selenium.py`)

## 📁 <h2>Структура проекта</h2>
├── index.html # HTML-страница с формой<br>
├── server.py # Сервер на базе http.server<br>
├── test_server.py # Юнит-тесты логики обработки формы<br>
├── test_selenium.py # Selenium-тест взаимодействия через браузер<br>
└── README.md # Описание проекта

---

## 🚀 <h2>Запуск проекта</h2>

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

🧪 <h2>Тестирование</h2><br>
Юнит-тест сервера
bash
python test_server.py
UI-тест через Selenium
Перед запуском убедитесь, что сервер (server.py) уже запущен!

bash
python test_selenium.py
⚠️ Убедитесь, что установлен браузер Chrome и соответствующий драйвер (используется webdriver-manager).⚠️

💡 <h2>Что делает сервер?</h2><br>
Отдаёт страницу "index.html" при переходе на "/"

При POST-запросе на "/submit" читает поля name и email

Возвращает HTML с подставленными данными:
Привет, [имя]! Твой email: [email]

🧰 <h2>Используемые технологии</h2>
Python 3.x
HTML5
http.server (встроенный модуль Python)
unittest (встроенный фреймворк тестирования)
Selenium (UI-тестирование)
webdriver-manager (автоматическое управление ChromeDriver)
