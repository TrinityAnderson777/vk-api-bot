import vk_api
import time
import sys
import random

import colorama
colorama.init()

def print_box(title, content_lines):
    max_length = max(len(line) for line in content_lines + [title])
    border = '═' * (max_length + 4)
    colors = [
        '',             # без цвета
        '\033[91m',     # красный
        '\033[93m',     # желтый
        '\033[92m',     # зеленый
        '\033[94m',     # синий
        '\033[95m',     # фиолетовый
        '\033[96m',     # голубой
        '\033[97m',     # белый
    ]
    color = random.choice(colors)
    endc = '\033[0m' if color else ''

    print(f"{color}╔{border}╗{endc}")
    print(f"{color}║  {title.center(max_length)}  ║{endc}")
    print(f"{color}╠{border}╣{endc}")
    for line in content_lines:
        print(f"{color}║  {line.ljust(max_length)}  ║{endc}")
    print(f"{color}╚{border}╝{endc}\n")

# Вначале выводим рамку один раз
print_box("Добро пожаловать в VK автоматизатор", [])

# Ввод токена
token = input("Введите ваш токен доступа: ")

# Создаем сессию
try:
    vk_session = vk_api.VkApi(token=token)
    vk = vk_session.get_api()
except Exception as e:
    print(f"Ошибка при создании сессии: {e}")
    sys.exit(1)

def удалить_исходящие_заявки():
    print_box("Удаление исходящих заявок", [])
    try:
        requests = vk.friends.getRequests(out=1, need_viewed=0, suggested=0, count=1000)
        count_requests = requests['count']
        print(f"Найдено исходящих заявок: {count_requests}")
        for user_id in requests['items']:
            try:
                print(f"🔄 Удаляю заявку на user_id: {user_id}")
                vk.friends.delete(user_id=user_id)
                print(f"✔️ Заявка на {user_id} удалена")
                time.sleep(1)
            except vk_api.exceptions.ApiError as e:
                print(f"❌ Ошибка при удалении {user_id}: {e}")
            except Exception as e:
                print(f"❓ Неожиданная ошибка на {user_id}: {e}")
    except Exception as e:
        print(f"Ошибка при получении заявок: {e}")
    print()

def добавить_друзей():
    print_box("Добавление друзей из предложений", [])
    try:
        suggestions = vk.friends.getSuggestions()
        print(f"Получено предложений: {suggestions['count']}")
        print("Имена предложенных друзей:")
        # Вывод только имен и фамилий
        if 'items' in suggestions:
            items = suggestions['items']
        else:
            items = suggestions
        if isinstance(items, list) and items and isinstance(items[0], dict):
            for user in items:
                print(f"{user['first_name']} {user['last_name']}")
        else:
            # В случае, если suggestions['items'] — просто список строк
            for name in items:
                print(name)
        # Далее можно добавить друзей по желанию
        for user in items:
            if isinstance(user, dict):
                user_id = user['id']
                try:
                    print(f"⏳ Готовлюсь добавить {user['first_name']} {user['last_name']} (ID: {user_id})")
                    time.sleep(3)
                    vk.friends.add(user_id=user_id)
                    print(f"✔️ {user['first_name']} {user['last_name']} добавлен")
                except vk_api.exceptions.ApiError as e:
                    print(f"❌ Ошибка при добавлении {user['first_name']} {user['last_name']}: {e}")
                except Exception as e:
                    print(f"❓ Неожиданная ошибка при добавлении {user['first_name']} {user['last_name']}: {e}")
    except Exception as e:
        print(f"Ошибка при получении предложений: {e}")
    print()

# Главное меню
print("Что вы хотите сделать?")
print("1 - Удалить исходящие заявки")
print("2 - Посмотреть имена предложенных друзей и добавить их")
choice = input("Введите число (1 или 2): ")
print()

if choice == '1':
    удалить_исходящие_заявки()
elif choice == '2':
    добавить_друзей()
else:
    print("Неверный выбор. Завершение.")