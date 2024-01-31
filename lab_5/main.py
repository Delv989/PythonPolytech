import doctest


class Employee:
    def __init__(self, name: str, salary: float, position: str):
        """
        Создание и подготовка к работе объекта "Сотрудник"

        :param name: Имя сотрудника
        :param salary: Зарплата сотрудника
        :param position: Должность сотрудника

        Примеры:
        >>> employee = Employee("Иван", 60000, "Инженер")
        """

        if not isinstance(name, str):
            raise TypeError("Имя сотрудника должно быть типа str")
        self.name = name

        if not isinstance(salary, (int, float)):
            raise TypeError("Зарплата сотрудника должна быть типа int или float")
        if salary <= 0:
            raise ValueError("Зарплата сотрудника должна быть положительным числом")
        self.salary = salary

        if not isinstance(position, str):
            raise TypeError("Должность сотрудника должно быть типа str")
        self.position = position

    def salary_change(self, new_salary: float) -> None:
        """
        Изменение зарплаты сотрудника

        :param new_salary: Новая зарплата сотрудника

        :raise ValueError: Если зарплата отрицательная, то вызовем ошибку

        Примеры:
        >>> employee = Employee("Иван", 60000, "Инженер")
        >>> employee.salary_change(70000)
        """
        if not isinstance(new_salary, (int, float)):
            raise TypeError("Зарплата сотрудника должна быть типа int или float")
        if new_salary <= 0:
            raise ValueError("Зарплата сотрудника должна быть положительным числом")
        ...

    def change_position(self, new_position: str) -> None:
        """
            Изменение должности сотрудника

            :param new_position: Новая должность сотрудника

            Примеры:
            >>> employee = Employee("Иван", 60000, "Инженер")
            >>> employee.change_position("Главный инженер")
        """
        if not isinstance(new_position, str):
            raise TypeError("Должность сотрудника должно быть типа str")
        ...


class Vector2D:
    def __init__(self, x: float, y: float):
        """
            Создание и подготовка к работе объекта "Вектор"

            :param x: Координата вектора по оси Ox
            :param y: Координата вектора по оси Oy

            Примеры:
            >>> vector = Vector2D(3, 4)
        """
        if not isinstance(x, (int, float)):
            raise TypeError("Координата должна быть типа int или float")
        self.x = x

        if not isinstance(y, (int, float)):
            raise TypeError("Координата должна быть типа int или float")
        self.y = y

    def norm(self) -> float:
        """
        Функция вычисляет норму вектора

        :return: Норма вектора

        Примеры:
         >>> vector = Vector2D(3, 4)
         >>> vector.norm()
        """
        ...

    def normalize(self) -> None:
        """
        Функция нормализует вектор

        Примеры:
        >>> vector = Vector2D(3, 4)
        >>> vector.normalize()
        """
        ...


class Circle:
    def __init__(self, x: float, y: float, radius: float):
        """
        Создание и подготовка к работе объекта "Круг"

        :param x: Координата центра круго по оси Ox
        :param y: Координата центра круга по оси Oy
        :param radius: Радиус круга

        Примеры:
        >>> circle = Circle(3, 4, 5)
        """
        if not isinstance(x, (int, float)):
            raise TypeError("Координата должна быть типа int или float")
        self.x = x

        if not isinstance(y, (int, float)):
            raise TypeError("Координата должна быть типа int или float")
        self.y = y

        if not isinstance(radius, (int, float)):
            raise TypeError("Радиус должен быть типа int или float")
        if radius <= 0:
            raise ValueError("Радиус должен быть положительным")
        self.radius = radius

    def area(self) -> float:
        """
        Функция вычисляет площадь круго

        :return: Площадь круга

        Пример:
        >>> circle = Circle(3, 4, 5)
        >>> circle.area()
        """
        ...

    def circumference(self) -> float:
        """
        Функция вычисляет длину окружности

        :return: Длина окружности

        Пример:
        >>> circle = Circle(3, 4, 5)
        >>> circle.circumference()
        """
        ...


if __name__ == "__main__":
    doctest.testmod()
