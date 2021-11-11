import random
from typing import Tuple


# Изначальные значения здоровья и силы удара героя:
hp = 10
attack = 10


def game() -> None:
    print(
        'Текстовая игра "Герой и чудовища".\n',
        'Ты — рыцарь в фантастической стране. Чтобы выйграть \n'
        ' нужно победить 10 чудовищ и тем самым спасти королевство!\n',
        'Изначально у тебя 10 жизней и меч с силой аттаки 10.\n',
        'На твоем пути в случайном порядке тебе могут попасться\n'
        ' яблочко, меч или монстр. Если хочешь узнать больше начинай игру!\n',
        'Если хочешь начать введи цифру 1 или \n' 
        ' цифру 2 чтобы выйти из игры!'
    )
    answer = getinput()
    if answer in "1":
        hero_hp = hp
        hero_attack = attack
        m_counter = 0
        win_count = 10
        print(
            "Начинаем игру!",
        )
        while m_counter < win_count:
            # Рандомно вывести события из monsters(), swords(), apples()
            events = [monsters, swords, apples]
            current_event = random.choice(events)

            if current_event == apples:
                hero_hp = apples(hero_hp)
            elif current_event == swords:
                hero_attack = swords(hero_attack)
            else:
                hero_hp, hero_attack, m_counter = monsters(
                    hero_hp, hero_attack, m_counter
                )
                print("Твой счет", m_counter, "из", win_count)

            if m_counter == win_count:
                print("ПОБЕДА! Ты победил всех чудовищ!")
                quit()

            if hero_hp == 0:
                print("ПОРАЖЕНИЕ! Игра окончена!")
                quit()
    else:
        print("Рады видеть тебя в реальном мире!")


def monsters(x: int, y: int, z: int) -> Tuple[int, int, int]:
    """Монстры.
        :param x: жизнь героя
        :param y: сила атаки героя
        :param z: число атакованных монстров
        :return: x, y, z
        :rtype: int
        """
    # Количество жизней чудовища и сила его аттаки
    monster_hp = random.randint(1, 15)
    monster_attack = random.randint(1, 10)

    # Сражение с чудовищем:
    print(
        "БОЙ! На горизонте чудовище с",
        monster_hp,
        "жизнями и с силой атаки ",
        monster_attack,
        "\n. У тебя жизнь:",
        x,
        " и сила атаки:",
        y,
    )

    # Действия
    print("РЕШАЙСЯ! 1 - сражаться, 2 - убежать, \nчтобы набраться сил")
    answer = getinput()
    if answer in "1":
        print("СРАЖЕНИЕ!")
        if y > monster_hp and monster_attack < x:
            x = x - monster_attack
            z = z + 1
            print("ПОБЕДА! В бою твоя жизнь сократилась до", x)
            return x, y, z
        else:
            x = 0
            return x, y, z

    else:
        print("Удалось убежать!")
        return x, y, z


def swords(x: int) -> int:
    """Мечи.
    :return: x
    :rtype: int
    :type x: int
    """
    # Силы атаки мечей
    sword_attack = random.randint(1, 15)
    print("МЕЧ! Найден меч с силой атаки", sword_attack, "Старый меч", x)
    print("1 - взять меч себе (выбросив старый), 2 - пройти мимо меча")
    answer = getinput()
    if answer in "1":
        x = sword_attack
        print("Новый меч у тебя! Новая сила атаки:", x)
        return x
    else:
        print("Старый меч лучше новых двух")
        return x


def apples(x: int) -> int:
    """Яблочки.
    :return: x
    :rtype: int
    :type x: int
    """
    apple_hp = random.randint(1, 5)
    x = x + apple_hp
    print("СЪЕДЕНО ЯБЛОЧКО! Количество жизней увеличилось на", apple_hp, "и равно", x)
    return x


def getinput() -> str:
    """Ввод игрока.
    :return: answer
    :rtype: str
    """
    print("твой выбор:")
    while True:
        answer = input()
        if answer in ("1", "2"):
            return answer
        print("Ввод некорректный. Введи еще раз 1 или 2")


game()
