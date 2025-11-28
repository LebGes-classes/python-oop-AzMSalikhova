class Ship:
    """Класс для описания корабля."""

    def __init__(self, name: str="", displacement: int=0, ship_type: str="") -> None:
        """Инициализация класса.

        Args:
            name: Наименование корабля.
            displacement: Водоизмещение корабля.
            ship_type: Тип корабля.
        """

        self.__name = name
        self.__displacement = displacement
        self.__ship_type = ship_type

    def get_name(self) -> str:
        """Геттер для наименования корабля.

        Returns:
            __name: Наименование корабля.
        """

        return f'Наименование корабля: {self.__name}'

    def set_name(self, new_name: str) -> None:
        """Сеттер для наименования корабля.

        Args:
            new_name: Наименование корабля.
        """

        if new_name and new_name.strip():
            self.__name = new_name.strip()
        else:
            print("Ошибка: наименование корабля не может быть пустым")

    def get_displacement(self) -> str:
        """Геттер для водоизмещения корабля.

        Returns:
            __displacement: Водоизмещение корабля.
        """

        return f'Водоизмещение: {self.__displacement}'

    def set_displacement(self, new_displacement: int) -> None:
        """Сеттер для водоизмещения корабля.

        Args:
            new_displacement: Водоизмещение корабля.
        """

        if new_displacement > 0:
            self.__displacement = new_displacement
        else:
            print("Ошибка: водоизмещение должно быть числом > 0")

    def get_type(self) -> str:
        """Геттер для типа корабля.

        Returns:
            __ship_type: Тип корабля.
        """

        return f'Тип корабля: {self.__ship_type}'

    def set_type(self, new_type: str) -> None:
        """Сеттер для типа корабля.

        Args:
            new_type: Тип корабля.
        """

        if new_type or new_type.strip():
            self.__ship_type = new_type.strip()
        else:
            print("Ошибка: тип корабля не может быть пустым")

    def display_info(self) -> None:
        """Вывод информации о корабле."""

        print(
            f'\nКорабль называется {self.__name}\n'
            f'Водоизмещение: {self.__displacement} тонн\n'
            f'Тип корабля: {self.__ship_type}\n'
        )

    def can_carry_passengers(self) -> str:
        """Метод, проверяющий, может ли корабль перевозить пассажиров.

        Returns:
            str: 'Да', если может перевозить пассажиров, иначе 'Нет'.
        """

        if self.__ship_type in ["пассажирский", "круизный", "яхта"]:

            return 'Да'
        else:

            return 'Нет'

    def calculate_cargo_capacity(self, ship_weight: int = 0) -> str:
        """Метод для вычисления грузоподъёмности корабля.

        Args:
            ship_weight: Вес корабля.

        Returns:
             str: Вывод одного из форматов сообщения:
                -сообщение с грузоподъёмностью корабля;
                -сообщение об ошибке ввода.
        """

        if ship_weight >= self.__displacement:

            return "Ошибка: вес корабля не может быть больше водоизмещения или равен водоизмещению"
        elif ship_weight <= 0:

            return "Ошибка: вес корабля должен быть больше 0"
        else:
            cargo_capacity = self.__displacement - ship_weight

            return f"Грузоподъемность {self.__name}: {int(cargo_capacity)} тонн"


class Main:
    """Класс для демонстрации корабля."""

    def main(self):
        """Метод, демонстрирующий работу класса."""

        print("Демонстрация работы класса Ship:")

        ship1 = Ship("Titanic", 52_310, "пассажирский")

        ship2 = Ship()
        ship2.set_name("USS Nimitz")
        ship2.set_displacement(104_600)
        ship2.set_type("военный")

        print("Корабль №1:")
        ship1.display_info()
        print(f"Может ли корабль №1 возить пассажиров? {ship1.can_carry_passengers()}")
        print(ship1.calculate_cargo_capacity(46_328))

        print("Корабль №2:")
        ship2.display_info()
        print(f"Может ли корабль №2 возить пассажиров? {ship2.can_carry_passengers()}")
        print(ship2.calculate_cargo_capacity(101_600))

        menu = Menu()
        menu.run()


class Menu:
    """Класс для работы пользовательского меню."""

    def run(self):
        """Метод запуска меню"""

        ship = None
        running = True

        while running:
            print("=" * 45 + "\n" +
                  " " * 18 + "МЕНЮ" + "\n" +
                  "1. Создать корабль." + "\n" +
                  "2. Показать основную информацию о корабле." + "\n" +
                  "3. Рассчитать грузоподъёмность корабля." + "\n" +
                  "4. Может ли этот корабль возить пассажиров?" + "\n" +
                  "5. Завершить программу.")

            choice = input("Выберите действие из меню: ")

            match choice:
                case "1":
                    ship = self.create_ship()
                case "2":
                    if ship is None:
                        print("Сначала создайте корабль.")
                    else:
                        print("Основная информация о корабле:")

                        ship.display_info()
                case "3":
                    if ship is None:
                        print("Сначала создайте корабль.")
                    else:
                        self.calculate_cargo(ship)
                case "4":
                    if ship is None:
                        print("Сначала создайте корабль.")
                    else:
                        print(ship.can_carry_passengers())
                case "5":
                    print("Программа успешно завершена.")

                    running = False
                case _:
                    print("Введите корректный номер из меню.")

    def create_ship(self):
        """Метод, создающий корабль."""

        ship = Ship()

        name = input("Введите наименование: ")
        ship.set_name(name)

        if ship.get_name() == "Наименование корабля: ":
            print("Корабль не создан.")

            return None

        try:
            displacement = int(input("Введите водоизмещение: "))
            ship.set_displacement(displacement)

            if ship.get_displacement() == "Водоизмещение: 0":
                print("Корабль не создан.")

                return None
        except ValueError:
            print("Корабль не создан.")

            return None

        ship_type = input("Введите тип корабля: ")
        ship.set_type(ship_type)

        if ship.get_type() == "Тип корабля: ":
            print("Корабль не создан.")

            return None

        print("Корабль создан!")

        return ship

    def calculate_cargo(self, ship):
        """Метод для вычисления грузоподъёмности корабля, созданного пользователем."""

        try:
            weight = int(input("Введите вес корабля: "))
            result = ship.calculate_cargo_capacity(weight)

            print(result)
        except ValueError:
            print("Введите корректные данные! Вес - это число.")


if __name__ == "__main__":
    main_program = Main()
    main_program.main()
