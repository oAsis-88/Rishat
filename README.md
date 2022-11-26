Выполните следующие пункты
1) `git clone  https://github.com/oAsis-88/Rishat.git` - Клонирование репозитория
2) `python -m venv venv` - Создать виртуальное окружение
3) `venv\Scripts\activate.bat` или `source env/Scripts/activate` - Активировать виртуальное окружение
4) `pip install -r req.txt` - Установить зависимости
5) `python manage.py makemigrations`
6) `python manage.py migrate`
7) `python manage.py loaddata db.json` - Загружаем данные
8) `python manage.py createsuperuser` (Если нужна админка)
9) `python manage.py runserver`
