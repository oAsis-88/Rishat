### Выполните следующие пункты для локального тестирования
1) `git clone  https://github.com/oAsis-88/Rishat.git` - Клонирование репозитория
2) `python -m venv venv` - Создать виртуальное окружение
3) `venv\Scripts\activate` для Windows `source venv/bin/activate` для Linux и MacOS- Активировать виртуальное окружение
4) `python -m pip install -r req.txt` - Установить зависимости
5) `python manage.py collectstatic --noinput` - Загрузить все static файлы
6) `python manage.py makemigrations`
8) `python manage.py migrate`
9) `python manage.py loaddatautf8 db.json` - Загружаем данные ()
10) `python manage.py runserver`

##### Admin panel
* login: admin
* password: admin
