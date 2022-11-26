Выполните следующие пункты
1) `git clone  https://github.com/oAsis-88/Rishat.git` - клонирование репозитория
2) `python -m venv env` - создать виртуальное окружение
3) `venv\Scripts\activate.bat` или `source env/Scripts/activate` - активировать виртуальное окружение
4) `python manage.py makemigrations`
5) `python manage.py migrate`
6) `python manage.py loaddata db.json` - загружаем данные
7) `python manage.py createsuperuser` (Если нужна админка)
8) `python manage.py runserver`
