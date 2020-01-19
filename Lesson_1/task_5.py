# По длинам трех отрезков, введенных пользователем, определить возможность существования треугольника,
# составленного из этих отрезков.
# Если такой треугольник существует, то определить,
# является ли он разносторонним, равнобедренным или равносторонним.

a = int(input('Введите длину первого отрезка: '))
b = int(input('Введите длину второго отрезка: '))
c = int(input('Введите длину третьего отрезка: '))

if b + c <= a or a + c <= b or a + b <= c:
    print('Нельзя составить треугольник')
elif a != b and a != c and b != c:
    print('Разносторонний треугольник')
elif a == b == c:
    print('Равносторонний треугольник')
else:
    print('Треугольник равнобедренный')
