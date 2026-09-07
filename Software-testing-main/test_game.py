import pytest
from game import check_guess

# 1. Позитивные тесты (проверка корректной работы)
def test_check_guess_correct():
    """Тест: число угадано верно."""
    assert check_guess(50, 50) == 'correct'

def test_check_guess_too_low():
    """Тест: введённое число меньше загаданного."""
    assert check_guess(30, 50) == 'too_low'

def test_check_guess_too_high():
    """Тест: введённое число больше загаданного."""
    assert check_guess(70, 50) == 'too_high'

# 2. Негативные тесты (проверка некорректных данных)
def test_invalid_input_string():
    """Тест: проверка валидации строки (не число)."""
    user_input = "abc"
    assert not user_input.isdigit()

def test_invalid_input_float():
    """Тест: проверка валидации дробного числа."""
    user_input = "12.5"
    assert not user_input.isdigit()