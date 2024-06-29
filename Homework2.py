import random

def get_numbers_ticket(min, max, quantity):
    
    if not (1 <= min <= max <= 1000 and 1 <= quantity <= (max - min + 1)):
        return []  

  
    numbers = random.sample(range(min, max + 1), quantity)
    numbers.sort()  

    return numbers
   
  # Приклад використання:
min_number = 1
max_number = 49
quantity = 6

lottery_numbers = get_numbers_ticket(min_number, max_number, quantity)
print("Your lottery tickets:", lottery_numbers)
