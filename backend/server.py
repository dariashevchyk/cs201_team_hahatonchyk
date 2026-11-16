"""Дані та допоміжні функції (заглушка). Тут буде завантаження/збереження даних."""
PERIODS = {
    1: "Українська революція",
    2: "Міжвоєнний період",
    3: "Друга світова",
    4: "Повоєнна відбудова",
    5: "Відлига",
    6: "Застій",
    7: "Відбудова"
}


def check_coordinates(value):
    """Перевіряє, що value — [latitude, longitude]; повертає [float, float].

    Кидає ValueError, якщо формат або діапазон некоректні.
    """
    if not isinstance(value, (list, tuple)) or len(value) != 2:
        raise ValueError("user_point має бути [latitude, longitude]")
    try:
        lat, lon = float(value[0]), float(value[1])
    except (TypeError, ValueError):
        raise ValueError("координати мають бути числами")
    if not (-90 <= lat <= 90 and -180 <= lon <= 180):
        raise ValueError("координати поза допустимим діапазоном")
    return [lat, lon]


def parse_period(value):
    """Приводить період (число або рядок на кшталт "3") до номера з PERIODS."""
    try:
        number = int(value)
    except (TypeError, ValueError):
        raise ValueError(f"некоректний період: {value!r}")
    if number not in PERIODS:
        raise ValueError(f"невідомий період: {number}")
    return number
