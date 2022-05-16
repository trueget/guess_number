import random

c = random.randint(1,10)
print('угадай число от 1 до 10!')
while True:
    n = input()
    if str(c) == n:
        print(f'Верно, это число - {c}')
        break
    else:
        print('Попробуйте снова!')