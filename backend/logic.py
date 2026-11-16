"""Бекенд «Двадцятого Києва».

Сервер і фронтенд уже працюють: коли користувач ставить точку на мапі,
сюди приходить user_point = [latitude, longitude] (гарантовано всередині меж Києва).

Поки що реальної логіки немає: on_user_point завжди повертає одну й ту саму
тестову відповідь, щоб можна було перевірити, що фронтенд її показує.

Що повертати з on_user_point:
    dict з необов'язковими ключами  title, date, period, description
    або None, якщо для цієї точки нічого показувати.
"""

from store import add_point, clear_point, get_points

SEARCH_RADIUS_M = 250


def setup():
    """Викликається один раз під час запуску сервера.
    Поки що нічого не додаємо."""
    pass


def distance_m(a, b):
    """Заглушка: завжди повертає 0."""
    return 0


def nearest_point(user_point, max_distance_m=SEARCH_RADIUS_M):
    """Заглушка: завжди повертає None (нічого не знайдено)."""
    return None


def on_user_point(user_point):
    """user_point = [latitude, longitude] — точка, яку поставив користувач.
    Заглушка: повертає фіксовану тестову подію незалежно від місця на мапі."""
    return {
        "title": "Тестова подія",
        "date": "1991-08-24",
        "period": 8,
        "description": "Це заглушка: справжня подія буде знайдена за координатами "
                       f"{user_point[0]:.4f}, {user_point[1]:.4f}, коли бекенд буде готовий.",
    }

