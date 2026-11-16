#заглушки


from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
OUTLINE_FILE = BASE_DIR / "kyiv_outline.txt"
POINTS_FILE = BASE_DIR / "points.json"

YEAR_MIN, YEAR_MAX = 1917, 1991
PERIODS = {
    1: "Українська революція",
    2: "Міжвоєнний період",
    3: "Друга світова війна",
    4: "Повоєнна відбудова",
    5: "Відлига",
    6: "Застій",
    7: "Перебудова",
}


def is_in_kyiv(latitude, longitude):
    """True, якщо точка всередині меж Києва (і не в «дірці» контуру)."""
    # TODO: завантажити контури з kyiv_outline.txt і перевірити входження точки
    return True


def _parse_period(value):
    # TODO: реалізувати парсинг номера або назви епохи
    return 1


def check_coordinates(value):
    """Перевіряє [latitude, longitude]: числа, діапазон, усередині Києва. Повертає [lat, lng]."""
    # TODO: додати перевірку типів, меж світу та is_in_kyiv()
    return list(value)



def add_point(name, date, period, description, coordinates):
    """Додає точку."""
    # TODO: додати валідацію всіх полів (включно з лімітом 2000 символів) та збереження у points.json
    return {
        "id": str(name),
        "date": str(date),
        "period": _parse_period(period),
        "description": description,
        "coordinates": check_coordinates(coordinates),
    }


def clear_point(id):
    """Видаляє точку за id. Повертає True, якщо точка існувала."""
    # TODO: реалізувати видалення зі сховища
    return False


def get_points():
    """Список усіх точок."""
    # TODO: зчитати дані з points.json
    return []

