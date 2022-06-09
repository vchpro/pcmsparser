# PCMS Parser

Скрипт поможет отсортировать нерешенные вами задачи по сложности, где сложность определяется, как количество людей, решивших задачу.


## Настройка

В файле config.py находятся все необходимые настройки
```python
url = "http://pcms.fml31.ru:5000/leaderboard/sirius2022j1" # ссылка на таблицу с результатами
delay = 120 # задержка перед обновлением страницы в секундах
```

## Использование

Запустите start.bat. Он установит необходимые библиотеки и запустит скрипт.

Запуск вручную:
```python
pip install -r requirements.txt
python main.py
```



## Участие в разработке
Вы можете внести свой вклад в проект, создав полезный Issue или Pull Request.

## Скриншот скрипта
[Скриншот скрипта](https://github.com/vchpro/pcmsparser/raw/main/github_demo.jpg)

## Лицензия
[MIT](https://choosealicense.com/licenses/mit/)



