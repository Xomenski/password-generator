"""
Простой генератор паролей
"""

import random
import string
import sys

def generate_password(length=12, use_special=True):
    """
    Генерирует случайный пароль
    
    length: длина пароля (по умолчанию 12)
    use_special: использовать спецсимволы (по умолчанию True)
    """
    # Базовые наборы символов
    letters = string.ascii_letters  # A-Z a-z
    digits = string.digits          # 0-9
    special = "!@#$%&*+-="         # Специальные символы
    
    # Формируем набор символов для генерации
    characters = letters + digits
    if use_special:
        characters += special
    
    # Генерируем пароль
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    """Основная функция программы"""
    print("🔐 Генератор паролей")
    print("-" * 30)
    
    try:
        # Запрашиваем длину пароля
        length_input = input("Длина пароля (по умолчанию 12): ").strip()
        length = int(length_input) if length_input else 12
        
        if length < 4:
            print("Длина должна быть не менее 4 символов!")
            sys.exit(1)
        
        # Запрашиваем использование спецсимволов
        special_input = input("Использовать спецсимволы (!@#$%&*) (y/n, по умолчанию y): ").strip().lower()
        use_special = special_input != 'n'
        
        # Запрашиваем количество паролей
        count_input = input("Сколько паролей сгенерировать (по умолчанию 1): ").strip()
        count = int(count_input) if count_input else 1
        
        # Генерируем и выводим пароли
        print("\n" + "=" * 40)
        print("Сгенерированные пароли:")
        print("=" * 40)
        
        for i in range(count):
            password = generate_password(length, use_special)
            print(f"{i+1}. {password}")
        
        print("=" * 40)
        print("✅ Готово! Сохраните пароли в надежном месте.")
        
    except ValueError:
        print("❌ Ошибка! Введите число.")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\n👋 Программа завершена.")
        sys.exit(0)

if __name__ == "__main__":
    main()
