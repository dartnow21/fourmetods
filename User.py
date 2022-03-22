from sympy import *
import numpy as np
from fourmetods.SearchExtremes import *
from fourmetods.MethodLagranja import *
from fourmetods.SearchExtremes import *
from fourmetods.GoldenSection import *
from fourmetods.BrentMet_var2 import *
from fourmetods.BFGS import *
from fourmetods.PorabolMet import *


class User:
    def userAnswer(self):
        print(
            "Каким методом для нахождения экстремумов хотите воспользоваться? 1 - Обычный способ / 2 - Метод Лагранжа / 3 - Метод золотого сечения \n"
            "/ 4 - Метод параболы / 5 - Метод Брента / 6 - Метод Бройдена-Флетчера-Гольфарба-Шанно")
        user_answer = int(input())
        if user_answer == 1:

            x, y = symbols('x y')
            print("Введите функцию f(x, y). Например:  x**2 + y ** 2 + 1")
            f = input()
            # x/y+x**2+y**3
            # exp(x+y)*(x**2-2*y**2)
            # x**2 + y ** 2 + 1
            print('Есть ли ограничения по x и y? 1-да / 0 – нет')
            ogr = int(input())
            x_from, x_to, y_from, y_to = -10, 10, -10, 10
            if ogr == 1:
                print('Введите допустимые интервалы по x:')
                print("Введите точку от. Пример: -10")
                x_from = float(input())
                print("Введите точку до. Пример: 10")
                x_to = float(input())

                print('Введите допустимые интервалы по y:')
                print("Введите точку от. Пример: -10")
                y_from = float(input())
                print("Введите точку до. Пример: 10")
                y_to = float(input())
            functions = SearchExtremes()
            functions.find(x, y, f, x_from, x_to, y_from, y_to)
        elif user_answer == 2:

            x, y = 'x', 'y'
            print("Введите функцию f(x). Например:  4*y**2 + x**2")

            f = input()
            # 5 - 3*x - 4*y
            # x + 3*y
            # 5*x*y - 4
            print("Ввод условия(ограничения).")
            print("Введите левую часть ограничения. Например: x**2 + y**2")
            left_x_y = input()
            print("Введите правую часть ограничения. Например: 25")
            # x**2 + y**2
            # (x**2)/8 + (y**2)/2
            right_x_y = input()
            x_y = left_x_y + '-' + right_x_y

            f_x_y = f + ' + L * (' + x_y + ')'
            print('Есть ли ограничения по x и y? 1-да / 0 – нет')
            ogr = int(input())
            x_from, x_to, y_from, y_to = -30, 30, -30, 30
            if ogr == 1:
                print('Введите допустимые интервалы по x:')
                print("Введите точку от. Пример: -10")
                x_from = float(input())
                print("Введите точку до. Пример: 10")
                x_to = float(input())

                print('Введите допустимые интервалы по y:')
                print("Введите точку от. Пример: -10")
                y_from = float(input())
                print("Введите точку до. Пример: 10")
                y_to = float(input())
            functions = MethodLagranja()
            functions.find(x, y, x_y, f, f_x_y, x_from, x_to, y_from, y_to, left_x_y)
        elif user_answer == 3:
            print("Введите функцию f(x, y). Например:  -5*x**5 + 4*x**4 - 12* x**3 + 11*x**2 - 2*x - 1")
            f = input()
            print('Есть ли ограничения по x? 1-да / 0 – нет')
            org = int(input())
            Xl, Xu = -10, 10
            if org == 1:
                print("Введите левое ограничение по x. Например: -0.5")
                Xl = float(input())
                print("Введите правое ограничение по x. Например: 0.5")
                Xu = float(input())
            print("Хотите указать e(точность)? 1 - да / 0 - нет")
            ep = int(input())
            e = 10 ** (-5)
            if ep == 1:
                print("Введите e. Например: 0.001")
                e = float(input())
            ea = 500
            print("Хотите увидеть промежуточные рузльтаты поиск экстремума? 1 - да / 0 - нет")
            while True:
                answ = int(input())
                if answ == 1:
                    flag = 'True'
                    break
                elif answ == 0:
                    flag = 'False'
                    break
                else:
                    print("Такого ответа нет! Введите корректно.")
            print("Хотите указать кол-во итераций? 1 - да / 0 - нет")
            it = int(input())
            iter = 500
            if it == 1:
                print("Введите кол-во итераций. Например: 10")
                iter = int(input())
            functions = GoldenSection()
            print(functions.find(f, Xl, Xu, e, ea, flag, iter))
        elif user_answer == 4:
            print("Введите функцию f(x, y). Например:  -3*x*sin(0.75*x) + exp(-2*x)")
            f = input()
            print('Есть ли ограничения по x? 1-да / 0 – нет')
            org = int(input())
            Xl, Xu = -10, 10
            if org == 1:
                print("Введите левое ограничение по x. Например: 0")
                Xl = float(input())
                print("Введите правое ограничение по x. Например: 6")
                Xu = float(input())
            print("Хотите указать e(точность)? 1 - да / 0 - нет")
            ep = int(input())
            e = 10 ** (-5)
            if ep == 1:
                print("Введите e. Например: 0.001")
                e = float(input())
            print("Хотите увидеть промежуточные рузльтаты поиск экстремума? 1 - да / 0 - нет")
            while True:
                answ = int(input())
                if answ == 1:
                    flag = 'True'
                    break
                elif answ == 0:
                    flag = 'False'
                    break
                else:
                    print("Такого ответа нет! Введите корректно.")
            print("Хотите указать кол-во итераций? 1 - да / 0 - нет")
            it = int(input())
            iter = 500
            if it == 1:
                print("Введите кол-во итераций. Например: 10")
                iter = int(input())
            functions = PorabolMet()
            functions.find(f, Xl, Xu, e, flag, iter)
        elif user_answer == 5:
            print("Введите функцию f(x). Например:  -3*x*sin(0.75*x) + exp(-2*x)")
            y = input()
            print("Введите левое ограничение по x. Например: 0")
            a = float(input())
            print("Введите правое ограничение по x. Например: 6")
            b = float(input())
            print("Введите e. Например: 0.001")
            eps = float(input())
            print("Введите кол-во итераций. Например: 10")
            iterations = int(input())
            function = BrentMet()
            function.find(y, a, b, eps, iterations)
        elif user_answer == 6:
            print("Введите функцию f(x, y). Например:  x**2 - x*y + y**2 + 9*x - 6*y + 20")
            f = input()
            print('Есть ли ограничения по x и y? 1-да / 0 – нет')
            ogr = int(input())
            Xl, Xu, Yl, Yu = -10, 10, -10, 10
            if ogr == 1:
                print("Введите левое ограничение по x. Например: -5")
                Xl = float(input())
                print("Введите правое ограничение по x. Например: 5")
                Xu = float(input())
                print("Введите левое ограничение по y. Например: -5")
                Yl = float(input())
                print("Введите правое ограничение по y. Например: 5")
                Yu = float(input())
            print("Необходимо ввести точку от которой мы будем отталкиваться.")
            print('Введите x. Например: 1')
            x = float(input())
            print('Введите y. Например: 1')
            y = float(input())
            print("Хотите указать e(точность)? 1 - да / 0 - нет")
            ep = int(input())
            e = 10 ** (-5)
            if ep == 1:
                print("Введите e. Например: 0.001")
                e = float(input())
            print("Хотите указать кол-во итераций? 1 - да / 0 - нет")
            it = int(input())
            iter = 500
            if it == 1:
                print("Введите кол-во итераций. Например: 10")
                iter = int(input())
            functions = BFGS()
            functions.find(f, Xl, Xu, Yl, Yu, np.array([[x], [y]]), e, iter)

