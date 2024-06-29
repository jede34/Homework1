import random

def get_numbers_ticket(min_num, max_num, quantity):
    # Перевірка вхідних параметрів
    if not (1 <= min_num <= max_num <= 1000):
        print("Помилка: неправильні параметри min і max")
        return []

    if not (1 <= quantity <= max_num - min_num + 1):
        print("Помилка: неправильна кількість чисел")
        return []

    # Використовуємо множину для збереження унікальних чисел
    numbers_set = set()

    while len(numbers_set) < quantity:
        random_number = random.randint(min_num, max_num)
        numbers_set.add(random_number)

    # Перетворюємо множину в відсортований список
    sorted_numbers = sorted(numbers_set)
    
    return sorted_numbers

# Приклад використання:
lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)
