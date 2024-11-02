import sys
import re
from typing import List, Dict

#
# python main_task_3.py ./files/logfile.log
# 

def parse_log_line(line: str) -> Dict[str, str]:
    """
    Парсить рядок логу і повертає словник з компонентами: дата, час, рівень, повідомлення.

    Аргументи:
    line (str): Рядок логу.

    Повертає:
    dict: Словник з компонентами логу.
    """
    match = re.match(r'(\d{4}-\d{2}-\d{2}) (\d{2}:\d{2}:\d{2}) (\w+) (.+)', line)
    if match:
        return {
            'date': match.group(1),
            'time': match.group(2),
            'level': match.group(3),
            'message': match.group(4)
        }
    return {}

def load_logs(file_path: str) -> List[Dict[str, str]]:
    """
    Завантажує лог-файл і повертає список словників з компонентами логу.

    Аргументи:
    file_path (str): Шлях до файлу логів.

    Повертає:
    list: Список словників з компонентами логу.
    """
    logs = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                log = parse_log_line(line.strip())
                if log:
                    logs.append(log)
    except FileNotFoundError:
        print(f"Файл {file_path} не знайдено.")
    except Exception as e:
        print(f"Помилка при читанні файлу: {e}")
    return logs

def filter_logs_by_level(logs: List[Dict[str, str]], level: str) -> List[Dict[str, str]]:
    """
    Фільтрує логи за рівнем логування.

    Аргументи:
    logs (list): Список словників з компонентами логу.
    level (str): Рівень логування для фільтрації.

    Повертає:
    list: Відфільтрований список логів.
    """
    return [log for log in logs if log['level'].upper() == level.upper()]

def count_logs_by_level(logs: List[Dict[str, str]]) -> Dict[str, int]:
    """
    Підраховує кількість записів для кожного рівня логування.

    Аргументи:
    logs (list): Список словників з компонентами логу.

    Повертає:
    dict: Словник з кількістю записів для кожного рівня логування.
    """
    counts = {}
    for log in logs:
        level = log['level']
        if level in counts:
            counts[level] += 1
        else:
            counts[level] = 1
    return counts

def display_log_counts(counts: Dict[str, int]):
    """
    Форматує та виводить результати підрахунку в читабельній формі.

    Аргументи:
    counts (dict): Словник з кількістю записів для кожного рівня логування.
    """
    print("Рівень логування | Кількість")
    print("-----------------|----------")
    for level, count in counts.items():
        print(f"{level:<16} | {count}")

def main():
    print("Запуск скрипта...")
    if len(sys.argv) < 2:
        print("Використання: python main_task_3.py <шлях до файлу логів> [рівень логування]")
        return

    file_path = sys.argv[1]
    level = sys.argv[2] if len(sys.argv) > 2 else None

    print(f"Завантаження логів з файлу: {file_path}") 
    logs = load_logs(file_path)
    if not logs:
        print("Логи не завантажені або файл порожній.")
        return

    print("Підрахунок логів за рівнями...")  
    counts = count_logs_by_level(logs)
    display_log_counts(counts)

    if level:
        print(f"Фільтрація логів за рівнем: {level}")  
        filtered_logs = filter_logs_by_level(logs, level)
        print(f"\nДеталі логів для рівня '{level.upper()}':")
        for log in filtered_logs:
            print(f"{log['date']} {log['time']} - {log['message']}")

if __name__ == "__main__":
    main()

#
# python main_task_3.py ./files/logfile.log
# 