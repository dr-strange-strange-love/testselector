Данный сервис (testselector) предназначен для сборки параметров автотестов из файлового хранилища (job_warehouse) и предоставления их в формате JSON по RESTful API. Базовые параметры хранятся в __init__ файлах, специфичные - в остальных файлах данной директории (по принципу переопределения).

<br />

Сервис состоит из 3х частей:
- веб-сервис jobconstructor_service (python-flask-gunicorn)
```
cd jobconstructor_service && gunicorn jobconstructor_service:application
```
- вспомогательная библиотека jobconstructor
```
$ pip install git+https://github.com/dr-strange-strange-love/testselector
```
- файловое хранилище job_warehouse

<br />

Примеры:
- Hello World - https://sleepy-island-97222.herokuapp.com/
- список тестов - https://sleepy-island-97222.herokuapp.com/api/v1.0/job
- пример теста - https://sleepy-island-97222.herokuapp.com/api/v1.0/job/vzt-pgov-win10x32-el_capitan-up
