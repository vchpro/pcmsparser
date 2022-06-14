# PCMS Parser

Скрипт поможет отсортировать нерешенные вами задачи по сложности, где сложность определяется, как количество людей, решивших задачу.


## Настройка

В файле pcmsparser/config.py находятся все необходимые настройки
```python
url = "http://pcms.fml31.ru:5000/leaderboard/sirius2022j1" # ссылка на таблицу с результатами
delay = 120 # задержка перед обновлением страницы в секундах
```

## Установка

Запустите INSTALL_LIBS.bat. Он установит необходимые библиотеки.

Установка библиотек вручную:
```python
cd pcmsparser
pip install -r requirements.txt
```

## Использование

Запустите start.bat. Он запустит скрипт.

Запуск вручную:
```python
cd pcmsparser
python main.py
```



## Участие в разработке
Вы можете внести свой вклад в проект, создав Issue или Pull Request.

## Скриншот скрипта
[Скриншот скрипта](https://github.com/vchpro/pcmsparser/raw/main/pcmsparser/github_demo.jpg)

## Лицензия
[MIT](https://choosealicense.com/licenses/mit/)



