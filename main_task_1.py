def caching_fibonacci():
    """
    Створює функцію для обчислення чисел Фібоначчі з використанням кешування.

    Повертає:
    function: Функція fibonacci(n), яка обчислює n-те число Фібоначчі.
        Якщо число вже знаходиться у кеші, функція повертає значення з кешу.
        Якщо число не знаходиться у кеші, функція обчислює його, зберігає у кеш та повертає результат.
    """
    cache = {}

    def fibonacci(n: int) -> int:
        """
        Обчислює n-те число Фібоначчі з використанням кешування.

        Аргументи:
        n (int): Порядковий номер числа Фібоначчі для обчислення.

        Повертає:
        int: n-те число Фібоначчі.
        """
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        if n in cache:
            return cache[n]

        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    return fibonacci


fib = caching_fibonacci()
print(fib(10)) 
print(fib(15))  
