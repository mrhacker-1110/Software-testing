import random

def check_guess(guess, secret_number):
    """
    Чистая логика: сравнивает догадку с загаданным числом.
    Возвращает: 'correct', 'too_low' или 'too_high'.
    """
    if guess == secret_number:
        return 'correct'
    elif guess < secret_number:
        return 'too_low'
    else:
        return 'too_high'

def play_game(secret_number=None, max_turns=10):
    """Основной игровой цикл."""
    if secret_number is None:
        secret_number = random.randint(1, 100)
    
    print("=== ИГРА: УГАДАЙ ЧИСЛО ===")
    print(f"Я загадал число от 1 до 100. У вас есть {max_turns} ходов!\n")

    turns_left = max_turns
    
    while turns_left > 0:
        current_turn = max_turns - turns_left + 1
        print(f"--- Ход {current_turn} из {max_turns} (Осталось: {turns_left}) ---")
        
        user_input = input("Введите число: ")
        
        # Проверка некорректного ввода
        if not user_input.isdigit():
            print("Ошибка! Введите целое положительное число.\n")
            continue

        guess = int(user_input)
        result = check_guess(guess, secret_number)

        if result == 'correct':
            print(f"\nПоздравляем! Вы угадали число {secret_number} за {current_turn} ходов!")
            return True
        elif result == 'too_low':
            print("Загаданное число БОЛЬШЕ.")
        elif result == 'too_high':
            print("Загаданное число МЕНЬШЕ.")
        
        turns_left -= 1
        print()

    print(f"Вы исчерпали все {max_turns} ходов. Игра окончена! Число было: {secret_number}")
    return False

if __name__ == "__main__":
    play_game()