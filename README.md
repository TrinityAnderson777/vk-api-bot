# VK Automation Bot

This script is designed to automate interactions with VK (VKontakte). It allows you to:

- Retrieve the list of suggested friends and display only their first and last names.
- Automatically send friend requests to selected users.
- Delete outgoing and incoming friend requests.

Additionally, it features a colorful frame with a random color on startup, making the interface look neat and vibrant.

---

## How the script works

### 1. Enter your access token
When you run the program, it prompts you to input your VK access token — which you should obtain in advance from the [VK developer section](https://vk.com/dev/access_token).

Your token needs permissions to manage friends and requests.

### 2. Visual design
Before starting, a decorative frame with a greeting appears, with a randomly chosen color, to enhance the visual appeal.

### 3. Main menu
You can select one of two options:
- **1** — delete all outgoing friend requests.
- **2** — get the list of suggested friends, display only their names, and send friend requests automatically.

---

## Detailed function descriptions

### `print_box(title, content_lines)`
This function draws a beautiful box with a header and content. The box's color is randomly selected each run, making the interface more engaging.

---

### `delete_outgoing_requests()`
This function finds all friend requests you've sent (outgoing) and deletes them.
How it works:
- Retrieves the list of outgoing requests.
- Calls the `friends.delete` API method for each.
- Displays the status of each deletion.

---

### `add_friends()`
This function:
- Fetches suggested friends (`friends.getSuggestions()`).
- Displays only their first and last names.
- Then, optionally, sends friend requests to each of them automatically, with delays.

---

## How to run

1. Install the required libraries:
BASH
pip install vk_api colorama
Скопировать
Запустить
Скачать


2. Launch the script — it will ask for your access token.

3. Choose an action — delete requests or add friends.

---

## Important notes

- For proper operation, it's recommended to run in Windows Terminal or another modern terminal that supports Unicode.
- On Windows, in cmd, run `chcp 65001` for UTF-8 support.
- For obtaining your token, see the [official VK documentation](https://vk.com/dev/access_token).

---

## Summary

This script is a convenient tool for managing VK friend requests and suggested friends with a friendly interface and automation features. It’s suitable for personal use or small communities needing quick list management.


# VK Automation Bot

Этот скрипт предназначен для автоматизации работы с VK (ВКонтакте). Он позволяет:

- Получить список предложенных друзей и вывести только их имена и фамилии.
- Автоматически отправить заявки в друзья выбранным пользователям.
- Удалять исходящие и входящие заявки.

Также в нем реализована красочная рамка с рандомным цветом при запуске, чтобы интерфейс выглядел аккуратно и ярко.

---

## Как работает скрипт

### 1. Ввод токена доступа
При запуске программа запрашивает у вас токен доступа VK — его нужно получить заранее через [раздел разработчика VK](https://vk.com/dev/access_token).

Токен должен иметь разрешения для работы с друзьями и заявками.

### 2. Визуальное оформление
Перед началом работы отображается рамка с приветствием, которая выбирается в случайном цвете. Это делается для красоты интерфейса.

### 3. Основное меню
Вы можете выбрать одну из двух опций:
- **1** — удалить все исходящие заявки.
- **2** — получить список предложенных друзей и автоматически отправить заявки в друзья.

---

## Подробное описание функций

### `print_box(title, content_lines)`
Функция рисует красивую рамку с заголовком и содержимым. Цвет рамки выбирается случайным при каждом запуске. Это делает интерфейс более приятным.

---

### `удалить_исходящие_заявки()`
Эта функция ищет все заявки, отправленные вами (исходящие), и удаляет их.
Работает так:
- Получает список исходящих заявок.
- Для каждой заявки вызывает API-метод `friends.delete`.
- Выводит статус удаления.

---

### `добавить_друзей()`
Эта функция:
- Получает список предложенных друзей (`friends.getSuggestions()`).
- Выводит только их имена и фамилии.
- Затем по желанию отправляет заявки в друзья каждому из них (автоматически, с задержкой).

---

## Как запустить

1. Установите необходимые библиотеки:
BASH
pip install vk_api colorama
Скопировать
Запустить
Скачать


2. Запустите скрипт, он попросит ввести ваш токен.

3. Выберите действие — удалить заявки или добавить друзей.

---

## Важные заметки

- Для корректной работы рекомендуется запускать в Windows Terminal или другом современном терминале, поддерживающем Unicode.
- В Windows в cmd рекомендуется выполнить команду `chcp 65001` для поддержки UTF-8.
- Для получения токена смотрите [официальную документацию VK](https://vk.com/dev/access_token).

---

## Итог

Этот скрипт — удобный инструмент для управления заявками и друзьями VK с приятным интерфейсом и автоматизацией. Он подойдет как для личного использования, так и для небольших сообществ, которым нужно быстро управлять списками.
