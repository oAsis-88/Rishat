Выполните следующие пункты
1) `git clone  https://github.com/oAsis-88/Rishat.git` - Клонирование репозитория
2) `python -m venv venv` - Создать виртуальное окружение
3) `venv\Scripts\activate.bat` или `source venv/bin/activate` - Активировать виртуальное окружение
4) `python -m pip install -r req.txt` - Установить зависимости
5) `python manage.py makemigrations`
6) `python manage.py migrate`
7) `python manage.py loaddatautf8 db.json` - Загружаем данные
8) `python manage.py runserver`
