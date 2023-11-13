<h2 align="center">👋Здравствуйте, представляю Вам документацию на проект Passes_drf </h3>

<h2 align="center">В данном проекте реализован API, в котором хранятся сведения о горных перевалах.</h3>

<h2 align="center">**Модели:**</h2>

<h4 align="center">**_- Users_**</h4>
<h4 align="center">(содержит информацию о пользователе: email, телефон, имя, отчество, фамилию).</h4>

<h4 align="center">**_- Coords_** </h4>
<h4 align="center">содержит информацию о координатах перевала: ширину, долготу, высоту</h4>

<h4 align="center">**_- Photo_** </h4>
<h4 align="center">содержит информацию о фото</h4>

<h4 align="center">**_- Pereval_added_** </h4>
<h4 align="center">содержит информацию о перевале: название, описание, время добавления, уровень сложности; ссылку на 
пользователя, добавившего этот перевал; координаты; фото</h4>
****
<h2 align="center">**Методы:** </h2>

* `Pereval_addedAPICreate`

* POST /`submitData`/ - добавление перевала 

* GET`/submitData/?user__email=<email>` - получение списка перевалов с фильтром по email’у
`PerevalOne`

* GET `/submitData/<id>` -  информация о перевале по id

* PATCH `/submitData/<id>` - изменение информации о перевале (менять данные пользователя нельзя)

****
<h2 align="center">**Принимает JSON-документ следующего формата:**</h2>
```
{
    "photos": [
        {
        "data": "http://vsegda-pomnim.com/uploads/posts/2022-04/1650930638_66-vsegda-pomnim-com-p-pereval-katu-yarik-gornii-foto-70.jpg",
        "title": "спуск"
    },
        {
        "data": "https://live.staticflickr.com/65535/48597231856_8b056b10b7_b.jpg",
        "title": "подьем"
    }
    ],
    "user": {
        "email": "useremail@gmail.com",
        "phone": 89116317211,
        "name": "Иван",
        "patronimic": "Иванович",
        "last_name": "Иванов"
    },
    "coords": {
        "latitude": 11.11,
        "longitude": 21.21,
        "height": 1231
    },
    "beauty_title": "перевал",
    "title": "Альпы",
    "other_titles": "Горы",
    "connect": "Огромная гора",
    "winter_level": "3a",
    "autumn_level": "3a",
    "spring_level": "3a",
    "summer_level": "2a",
    "status": "new"
}
```
---
<h2 align="center">**Установка:**</h2>
1) скачать проект https://github.com/Dmitriy-Vilisov/Passes_drf.git
2) создать и активировать виртуальное окружение
`python -m venv venv`
`source venv/bin/activate`
3) установить следующие библиотеки:

`pip install django`

`pip install djangorestframework`

`pip install psycopg2-binary`

`pip install drf-writable-nested`

`pip install django-filter`

`pip install python-dotenv`
_(при отсутствии опыта работы с переменным окружением, заменить в файле settings параметры, используемые значения из 
python-dotenv)_
4) создать и применить миграции

`python manage.py makemigrations`

`python manage.py migrate`

5) запустить проект

`python manage.py runserver`
