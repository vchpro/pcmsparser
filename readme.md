# PCMS Parser

Скрипт поможет отсортировать нерешенные вами задачи по сложности, где сложность определяется, как количество людей, решивших задачу.

## Установка

Установите необходимые библиотеки с помощью pip

```bash
pip install -r requirements.txt
```

## Настройка

В файле config.py находятся все необходимые настройки
```python
url = "http://pcms.fml31.ru:5000/leaderboard/sirius2022j1" # ссылка на таблицу с результатами
delay = 120 # задержка перед обновлением страницы в секундах
```

## Использование

```python
python main.py
```



## Участие в разработке
Вы можете внести свой вклад в проект, создав полезный Issue или Pull Request.

## Скриншот скрипта
[Скриншот скрипта](https://github.com/vchpro/pcmsparser/raw/main/github_demo.jpg)

## Лицензия
[MIT](https://choosealicense.com/licenses/mit/)



