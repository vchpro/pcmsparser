# PCMS Parser

Скрипт поможет отсортировать нерешенные вами задачи по сложности, где сложность определяется, как количество людей, решивших задачу.


## Настройка

В файле src/settings.json находятся все необходимые настройки
```python
url = "http://pcms.fml31.ru:5000/leaderboard/sirius2022j1" # ссылка на таблицу с результатами
delay = 120 # задержка перед обновлением страницы в секундах
```

## Установка

Установите требуемые библиотеки:
```python
cd src
pip install -r requirements.txt
```

## Использование

Запустите скрипт с помощью python:
```python
cd src
python main.py
```



## Участие в разработке
Вы можете внести свой вклад в проект, создав Issue или Pull Request.

## Скриншот скрипта
[Скриншот скрипта](https://github.com/vchpro/pcmsparser/raw/main/github_demo.jpg)

## Лицензия
[MIT](https://choosealicense.com/licenses/mit/)



