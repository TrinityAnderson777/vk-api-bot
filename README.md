English version (README-en.md)

Title: VK Automation CLI (bot.py)

Overview
- A Python-based command-line tool that automates several VK actions using the VK API.
- Features include:
- Delete outgoing friend requests
- Add suggested friends
- Unsubscribe from all groups
- Delete all music
- Like posts in a group feed
- Like posts on a user’s wall
- Remove likes from posts in a group
- Remove likes from a user’s posts
- Interactive, with colored status boxes and confirmation prompts.
- Language of prompts: Russian, but code comments and structure are in English/Russian mix.

Prerequisites
- Python 3.8+ (tested with 3.8–3.11)
- pip (comes with Python)
- A VK user access token with the necessary permissions (offline scope is helpful for long-running sessions)

Installation
- Install required libraries:
- pip install vk_api colorama
- Optional: clone the repo and run the script directly
- python bot.py
- The script will prompt you to enter your VK access token at startup.

Usage
- When you run python bot.py:
- A welcome colored box is printed.
- You are asked to enter your VK access token.
- The script establishes a VK session via vk_api.VkApi(token=token).
- You are presented with a menu of actions (1–8) and 0 to exit.
- For each operation:
- A confirmation prompt appears (e.g., “Do you want to ...? 1 for Yes / 0 for No”).
- If you confirm (enter 1), the script performs the action and logs progress.
- If you cancel (enter 0), the operation is skipped with a notice.
- Operations (as numbered in the UI):
1) Delete outgoing friend requests
2) View suggested friends and add them
3) Unsubscribe from all groups
4) Delete all music
5) Put likes on posts in a group’s wall
6) Like posts on a user’s wall
7) Remove likes from posts in a group
8) Remove likes from posts on a user’s wall
0) Exit

Notes
- The script relies on VK API methods like friends.getRequests, friends.delete, groups.leave, audio.delete, wall.get, likes.add, likes.delete, etc.
- Some operations may fail due to API limitations, permissions, or rate limits. Errors are reported in the console.
- Output is enhanced with colored boxes via colorama and ANSI color codes.

Security and Safety
- The script requires your VK access token. Do not share it.
- Treat this tool as a risky automation utility: confirm destructive actions (like deleting music or leaving groups) before running.
- Consider using a dedicated account or token with limited permissions for automated tasks.

Configuration
- There is no separate config file; the token is entered at runtime.
- The script prints status messages and uses a random color for the banner box on startup.

Troubleshooting
- If the script cannot create a VK session, verify that the token is valid and has required permissions.
- If an API error occurs for a specific operation, check the error message in the console and retry later (rate limits or permission issues are common).


Russian version (README-ru.md)

Название: VK Автоматизация CLI (bot.py)

Описание
- Python-скрипт с интерфейсом командной строки, который автоматизирует ряд действий во VK через VK API.
- Возможности:
- Удаление исходящих заявок в друзья
- Добавление предложенных друзей
- Отписка от всех групп
- Удаление всей музыки
- Поставить лайки запостам в ленте группы
- Поставить лайки на посты пользователя
- Удалить лайки с постов группы
- Удалить лайки с постов пользователя
- Интерактивный режим с выводом в цвете и подтверждениями перед выполнением операций.
- Приветственное оформление на русском языке в интерфейсе.

Требования
- Python 3.8+ (проверено на актуальных версиях)
- Установленные библиотеки vk_api и colorama
- Токен доступа VK пользователя с нужными правами (рекомендуется offline-право для стабильной работы)

Установка
- Установить зависимости:
- pip install vk_api colorama
- Запустить скрипт:
- python bot.py
- При первом запуске скрипт запросит ваш токен доступа VK.

Использование
- При запуске бот выводит приветствие в цветной рамке.
- Затем запрашивает токен доступа.
- Скрипт устанавливает сессию VK через vk_api.VkApi(token=token) и открывает меню.
- В меню можно выбрать действия плитками 1–8 и 0 для выхода.
- Перед выполнением любой операции появляется подтверждение (1 — да, 0 — отмена).
- Номер действий в меню:
1) Удалить исходящие заявки
2) Посмотреть имена предложенных друзей и добавить их
3) Отписаться от всех групп
4) Удалить всю музыку
5) Поставить лайки в ленте группы
6) Поставить лайки на странице пользователя
7) Убрать лайки с постов группы
8) Убрать лайки с постов пользователя
0) Выход

Замечания
- Скрипт напрямую взаимодействует с VK API и может нести риск нежелательных действий (удаление музыки, выход из сообществ и т. п.). Будьте внимательны и заранее протестируйте на тестовом аккаунте.
- Возможны ошибки API, ограничения по частоте запросов и отсутствие разрешений на конкретные операции. Ошибки выводятся в консоль.

Безопасность
- Не передавайте токен посторонним лицам.
- Для долгосрочной работы можно использовать токен с offline-права.

Настройка и использование
- Токен вводится вручную во время запуска.
- Текстовые сообщения интерфейса на русском языке; код содержит элементы на русском и английском.

Внесение изменений
- Вносите изменения через форк репозитория, создайте ветку, поменяйте код и создайте pull request.
