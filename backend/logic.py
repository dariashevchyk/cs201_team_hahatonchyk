"""Ваш код бекенду. Уся логіка живе тут, у Python.

Фронтенд лише дозволяє поставити точку на мапі й показує те, що ви повернете.
Коли користувач ставить точку, сюди приходить список
    user_point = [latitude, longitude]
(гарантовано всередині меж Києва). Точка зникає з мапи, щойно користувач
закриє праву панель або поставить іншу.

Що повертати з on_user_point:
    dict з необов'язковими ключами  title, date, period, description
    або None, якщо для цієї точки нічого показувати.
"""

import math

from store import add_point, clear_point, get_points   # clear_point, get_points — для ваших потреб

SEARCH_RADIUS_M = 250   # як близько до точки користувача шукати записи


def setup():
    """Викликається один раз під час запуску сервера. Наповнюйте дані тут.
    add_point оновлює запис, якщо такий id уже є, тож повторний запуск безпечний.
    Нижче лише приклади — замініть їх власними."""
    add_point("maidan-1941", "1941-09-19", 4, "19 вересня 1941 року до Києва увійшли німецькі війська. Окупація міста тривала до листопада 1943 року.", [50.4501, 30.5234])
    add_point(
        "rada-1991", "1991-08-24", 8,
        "24 серпня 1991 року Верховна Рада УРСР ухвалила Акт проголошення незалежності України.",
        [50.4478, 30.5325]
    )

setup()

def distance_m(a, b):
    """Відстань між двома [lat, lng] у метрах (формула гаверсинуса)."""
    lat1, lng1, lat2, lng2 = map(math.radians, (a[0], a[1], b[0], b[1]))
    h = math.sin((lat2 - lat1) / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin((lng2 - lng1) / 2) ** 2
    return 2 * 6371000 * math.asin(math.sqrt(h))


def nearest_point(user_point, max_distance_m=SEARCH_RADIUS_M):
    """Найближча збережена точка в межах max_distance_m або None."""
    best, best_distance = None, max_distance_m
    for point in get_points():
        d = distance_m(user_point, point["coordinates"])
        if d <= best_distance:
            best, best_distance = point, d
    return best


def on_user_point(user_point):
    """user_point = [latitude, longitude] — точка, яку поставив користувач.
    Приклад: показуємо найближчий запис у радіусі SEARCH_RADIUS_M."""
    return nearest_point(user_point)


