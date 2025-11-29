from random import randint

number  - randint(1, 100)
print("Угайдайте число от 1 до 100.")

while True:
    guess = input("Введите ваше предположение (или 'выход' для завершения): ")
    
    if guess.lower() == 'выход':
        print("Спасибо за игру! До свидания.")
        break
    
    try:
        guess = int(guess)
    except ValueError:
        print("Пожалуйста, введите корректное число.")
        continue
    
    if guess < 1 or guess > 100:
        print("Число должно быть в диапазоне от 1 до 100.")
        continue
    
    if guess < number:
        print("Слишком мало! Попробуйте снова.")
    elif guess > number:
        print("Слишком много! Попробуйте снова.")
    else:
        print("Поздравляем! Вы угадали число.")
        break   