class Car:
    """
        Класс Car симулирует поведение машины


        Attributes
        ----------
        _consumption : float
            Расход топлива на 1 милю
        _tank_volume : float
            Объём топливного бака
        _mileage : float
            Пробег машины
        engine_on : bool
            Индикатор состояния двигателя
        reserve : float
            Запас топлива
    """

    def __init__(self, consumption: float, tank_volume: float, mileage: float = 0):
        """
        Создание объекта "Машина"

        :param consumption: Расход топлива на 1 милю
        :param tank_volume: Объём топливного бака
        :param mileage: Пробег машины

        """
        self.reserve = tank_volume
        self.engine_on = False
        self._mileage = mileage
        self._consumption = consumption
        self._tank_volume = tank_volume

    @property
    def mileage(self) -> float:
        """
        Изменение этого аттрибута должно происходит только при
        создании и вызове функции drive
        """
        return self._mileage

    @property
    def consumption(self) -> float:
        """После создания изменение этого аттрибута происходить не должно """
        return self.consumption

    @property
    def tank_volume(self) -> float:
        """После создания изменение этого аттрибута происходить не должно """
        return self.tank_volume

    def drive(self, distance: float) -> None:
        """
        Движение машины

        :param distance: Расстояния, которое проедет машина
        """
        ...

    def refuel(self, new_reserve: float) -> None:
        """
        Заправить машину
        :param new_reserve: Новый уровень топлива
        """
        ...

    def __str__(self):
        return f"Автомобиль. Пробег: {self.mileage}. Остаток топлива: {self.reserve}"

    def __repr__(self):
        return f"{self.__class__.__name__}(consumption={self.consumption}, tank_volume={self.tank_volume}, mileage={self.mileage})"


class HybridCar(Car):
    """
            Класс HybridCar симулирует поведение гибридной машины


            Attributes
            ----------
            _consumption : float
                Расход топлива на 1 милю
            _tank_volume : float
                Объём топливного бака
            _mileage : float
                Пробег машины
            engine_on : bool
                Индикатор состояния двигателя
            reserve : float
                Запас топлива
            _battery_consumption : float
                Расход батареи на 1 милю
            _battery_capacity : float
                Вместимость батареи
            battery_reserve : float
                Заряд батареи
        """
    def __init__(self, consumption: float, tank_volume: float, battery_consumption: float, battery_capacity: float,
                 mileage: float = 0) -> None:
        """
        Создание объекта "Гибридная машина"

        :param consumption: Расход топлива на 1 милю
        :param tank_volume: Объём топливного бака
        :param mileage: Пробег машины
        :param battery_consumption:Расход батареи на 1 милю
        :param battery_capacity: Вместимость батареи
        """

        super().__init__(consumption, tank_volume, mileage)
        self._battery_consumption = battery_consumption
        self._battery_capacity = battery_capacity
        self.battery_reserve = battery_capacity

    @property
    def battery_capacity(self) -> float:
        """После создания изменение этого аттрибута происходить не должно """
        return self._battery_capacity

    @property
    def battery_consumption(self) -> float:
        """После создания изменение этого аттрибута происходить не должно """
        return self._battery_consumption

    def drive(self, distance: float) -> None:
        """
        Движение машины. Метод был перегружен, так как теперь он должен учитывать, что при
        окончании топлива будет использоваться батарея

        :param distance: Расстояния, которое проедет машина
        """
        ...

    def recharge(self, new_battery_reserve: float) -> None:
        """
        Зарядить машину
        :param new_battery_reserve: Новый уровень заряда батареи
        """
        ...

    def __str__(self):
        return f"Автомобиль. Пробег: {self.mileage}. Остаток топлива: {self.reserve}. " \
               f"Заряд батареи: {self.battery_reserve}"

    def __repr__(self):
        return f"{self.__class__.__name__}(consumption={self.consumption}, " \
               f"tank_volume={self.tank_volume}, mileage={self.mileage}, " \
               f"battery_consumption={self.battery_consumption}, battery_reserve={self.battery_reserve})"


if __name__ == "__main__":
    pass
