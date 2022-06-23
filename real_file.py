# | - соединение
# & - пересечение
# - - разность (что не входит в МНОЖЕСТВО2, но входит в МНОЖЕСТВО1)
# ^ - симметрическая разность(какие элементы не входят друг в друга)
# <= - проверка на подмножество
# >= - проверка на надмножество



def main():
    basketball, baseball = get_names()

    ever_sport = baseball & basketball # Множество, показывающее игроков, которые находятся в Баскетболе и в бейсболе
    full_sport = baseball | basketball # Множество, показывающее игроков, котоыре находятся в любой команде
    baseball_players = baseball - basketball # Множество, показывающее игрово, которые находятся ТОЛЬКО в бейсбольной команде
    basketball_players = basketball - baseball  # Множество, показывающее игроков, которые находятся ТОЛЬКО в баскетбольной команде
    only_one_sport = baseball ^ basketball # Множество, показывающее игроков, которые занимаются только одним видом спорта

    print(baseball, "Бейсбол")
    print(basketball, "Баскетбол")
    print(ever_sport, "Пересечение")
    print(full_sport, "В любой команде")
    print(baseball_players, "В бейсбольной команде ТОЛЬКО")
    print(basketball_players, "В Баскетбольной команде ТОЛЬКО")
    print(only_one_sport, "Только один вид спорта")


def get_names():
    basketball = []
    baseball = []

    baseball_real = set()
    basketball_real = set()

    num = num = int(input("Введите '1' - чтобы ввести имя игрока в баскетбол, '2'- чтобы не вводить: "))
    while num != 2:
        basketball.append(input("Введите имя игрока, играющего в баскетбол: "))
        num = int(input("Введите '1' - чтобы ввести имя ещё, '2'- чтобы перестать: "))

    num = int(input("Введите '1' - чтобы ввести имя игрока в бейсбол, '2'- чтобы не вводить: "))
    while num != 2:
        baseball.append(input("Введите имя игрока, играющего в бейсбол: "))
        num = int(input("Введите '1' - чтобы ввести имя ещё, '2'- чтобы перестать: "))

    baseball_real.update(baseball)
    basketball_real.update(basketball)

    return basketball_real, baseball_real

main()



