import requests
from bs4 import BeautifulSoup
import sys
import os
import time
from tabulate import tabulate
from config import url, delay


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


r = None

cls()
try:
    print("Загружаем страницу...")
    r = requests.get(url)

    if str(r.status_code) != "200":
        raise Exception(f"Ошибка сервера/клиента. Код - {r.status_code}")

except Exception as e:
    print(f"Невозможно получить страницу {url}")
    print(f"{e}")
    time.sleep(30)
    sys.exit(0)

soup = BeautifulSoup(r.text, features="html.parser")
users = [""]

users_page = soup.select(".name")
for user_p in users_page:
    users.append(user_p.get_text())

this_user = ""
while this_user == "":
    cls()
    for x in range(1, len(users)):
        print(f"{x} {users[x]}")

    try:
        user_id = input(f"Введите ваш номер в списке (1-{len(users) - 1}): ")
        if user_id == "0":
            raise ValueError("Невалидное число (0)")

        this_user = users[int(user_id)]
    except Exception as e:
        print("Ошибка. Попробуйте еще раз")
        print(f"{e}")

cls()


def build_view(tasks):
    tasks.sort(key=lambda x: [-x[0], x[1], x[2]])
    lenn = 129


    e = []
    keys = ['Решено у', 'Контест', 'Задача', 'Ссылка']

    for task in tasks:
        e.append([str(task[0]).center(10) if len(str(task[0])) == 2 else str(task[0]).center(11), task[1], task[2], task[3]])

    print(tabulate(e, headers=keys, tablefmt='fancy_grid', stralign='center'))



while True:
    contests = []

    contests_page = soup.select(".contest")

    for contest_p in contests_page:
        link = contest_p.select_one("a").get("href")
        link = link[0:link.rfind("/")]
        contests.append([contest_p.get_text(), int(contest_p.get("colspan")), link])

    tasks = []

    tasks_page = soup.select(".problem")

    nowId = 0
    nowO = contests[0][1]

    for tasks_p in tasks_page:
        if nowO == 0:
            nowId += 1
            nowO = contests[nowId][1]

        tasks.append([0, contests[nowId][0], tasks_p.get("title"), f"{contests[nowId][2]}/problem/{tasks_p.get_text()}"])
        nowO -= 1

    nowId = 0
    nowName = 0
    verdicts = soup.select(".verdict, .name")

    for v in verdicts:
        if v.get("class")[0] == "name":
            nowName = v.get_text()
        else:
            if "OK" in v.get("class") or "UPS" in v.get("class"):
                if nowName == this_user:
                    tasks[nowId][0] = -100000000000
                else:
                    tasks[nowId][0] += 1

            nowId += 1
            nowId %= len(tasks)

    unsolved_tasks = []
    for t in tasks:
        if t[0] >= 0:
            unsolved_tasks.append(t)

    unsolved_tasks.sort()

    cls()
    build_view(unsolved_tasks)

    time.sleep(delay)
    try:
        r = requests.get(url)

        if str(r.status_code) != "200":
            raise Exception(f"Ошибка сервера/клиента. Код - {r.status_code}")

    except Exception as e:
        print(f"Невозможно получить страницу {url}")
        print(f"{e}")
        time.sleep(30)
        sys.exit(0)

    soup = BeautifulSoup(r.text, features="html.parser")
