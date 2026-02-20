# 📘 Learning Log

![Статус](https://img.shields.io/badge/status-learning-brightgreen)
![Python](https://img.shields.io/badge/python-3.10+-blue)

Журнал обучения по книге Эрика Мэтиза «Изучаем Python». Проект демонстрирует освоение ключевых концепций языка через практическое веб‑приложение.

## 🧠 О проекте

**Learning Log** — веб‑приложение для ведения личного журнала изучения Python. Позволяет:
- 📁 создавать темы (разделы обучения);
- 📝 добавлять записи по каждой теме;
- 📅 просматривать хронологию изучения;
- 🔐 управлять учётными записями пользователей.

Проект реализован на Django согласно главам книги Эрика Мэтиза.


## ✨ Особенности

- 🔑 аутентификация пользователей;
- ✏️ CRUD‑операции для тем и записей;
- 📱 адаптивный интерфейс (HTML/CSS);
- 🗃️ база данных SQLite;
- 🛡️ защита от CSRF и XSS;
- 📄 пагинация записей.


## ⚙️ Установка

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/dshebeko20/learning_log.git

2. Создайте виртуальное окружение:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate     # Windows

3. Установите зависимости:
   ```bash
   pip install -r requirements.txt

4. Настройте базу данных:
   ```bash
   python manage.py migrate

5. Создайте суперпользователя:
   ```bash
   python manage.py createsuperuser

6. Запустите сервер:
   ```bash
   python manage.py runserver
7. Откройте браузер: http://127.0.0.1:8000


## 🎯 Использование

1. Вход в систему:
- 🔽 перейдите на http://127.0.0.1:8000/admin для входа как администратор;
- 🚪 или используйте форму Register на главной странице.

2. Создание темы
- ➕ перейдите в раздел «Topics» нажмите «Add a new topic»;
- ✍️ введите название (например, «Циклы»);
- ✅ сохраните.

3. Добавление записи
- 📂 выберите тему из списка «Topics»;
- ➕ нажмите «Add new entry»;
- 🖋️ заполните поле (дата подставится автоматически);
- ✅ сохраните кнопкой «Add Entry».

4. Редактирование записи
- 📂 выберите тему из списка «Topics»;
- ➕ нажмите «edit entry»;
- 🖋️ отредактируйте запись;
- ✅ сохраните кнопкой «Save changes».

5. Просмотр журнала
- 📋 в разделе «Topics» отображается список тем;
- 🔍 кликните на тему для просмотра записей.

## 📸 Скриншоты

![Главная страница](https://github.com/dshebeko20/learning_log/blob/main/screenshots/main_page.png)  
![Регистрациия](https://github.com/dshebeko20/learning_log/blob/main/screenshots/form_register.png)  
![Страница тем](https://github.com/dshebeko20/learning_log/blob/main/screenshots/topics.png)  
![Страница описаний](https://github.com/dshebeko20/learning_log/blob/main/screenshots/entries.png)

## 📚 Пройденные концепции (по главам книги)

- Главы 1–11: 🐍 основы Python, 📁 работа с файлами, 🧪 тесты;
- Главы 12–15: ⚙️ настройка Django, 🗃️ модели, 🖼️ шаблоны;
- Главы 16–18: 📋 формы, 🔑 аутентификация, 📦 развёртывание;
- Главы 19–20: 🎨 улучшение интерфейса, ⛓️ API (в планах).


## 📜 Лицензия

Проект носит учебный характер. Код доступен под лицензией MIT.


## 👤 Контакты

- Автор: Шебеко Дмитрий
- Email: dshebeko20@gmail.com
- GitHub: https://github.com/dshebeko20


## 🙏 Благодарности

- Эрик Мэтиз — за книгу «Изучаем Python» 📚;
- сообщество Django — за документацию и примеры 🧑‍💻.
   

