import re
from typing import Callable, Generator

def generator_numbers(text: str) -> Generator[float, None, None]:
    """
    Аналізує текст і повертає генератор, що ітерує по всіх дійсних числах у тексті.

    Аргументи:
    text (str): Вхідний текст для аналізу.

    Повертає:
    Generator[float, None, None]: Генератор, що ітерує по всіх дійсних числах у тексті.
    """
    pattern = r'\b\d+\.\d+\b'
    for match in re.finditer(pattern, text):
        yield float(match.group())

def sum_profit(text: str, func: Callable[[str], Generator[float, None, None]]) -> float:
    """
    Використовує генератор для обчислення загальної суми чисел у тексті.

    Аргументи:
    text (str): Вхідний текст для аналізу.
    func (Callable): Функція, що повертає генератор чисел з тексту.

    Повертає:
    float: Загальна сума чисел у тексті.
    """
    return sum(func(text))


text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")  