# TODO Написать 3 класса с документацией и аннотацией типов
import doctest


class Ferry:
    def __init__(self, name: str, capacity: int, passengers: int):
        """
        Создание и подготовка к работе класса "Паром"

        :param name: Название парома
        :param capacity: Пассажировместимость парома
        :param passengers: Количество пассажиров

        Примеры:
        >>> ferry = Ferry('Alfa', 250, 0)#Иницмализация экземпляра класса
        """

        if not isinstance(name, str):
            raise TypeError('Название парома должно быть словом')
        self.name = name

        if not isinstance(capacity, int):
            raise TypeError('Пассажировместимость парома должна быть целым числом')
        if capacity <= 0:
            raise ValueError('Пассажировместимость парома должна быть положительным числом')
        self.capacity = capacity

        if not isinstance(passengers, int):
            raise TypeError('Количество пассажиров должно быть целым числом')
        if passengers < 0:
            raise ValueError('Количество пассажиров не может быть отрицательным числом')
        if passengers > capacity:
            raise ValueError('Перегрузка парома не допустима! ')
        self.passengers = passengers

    def is_vacant_seats(self, capacity: int, passengers: int) -> int:
        """
        Функция определяет количество свободных мест

        :return: Количество свободных мест

        Примеры:

        >>> ferry = Ferry('Beta', 250, 100)
        >>> ferry.is_vacant_seats(300, 210)
        90
        """
        vacant_seats = capacity - passengers
        if vacant_seats > 0:
            return vacant_seats
        else:
            raise ValueError('Свободных мест нет')

    def take_on_board(self, capacity: int, passengers: int, plus_passengers: int) -> int:

        """
        Принять новых пассажиров на борт

        :param plus_passengers: Количество новых пассажиров
        raise ValueError: Если количество новых пассажиров больше числа свободных мест,
        то вызываем ошибку
        :return: Количество свободных мест, количество пассажиров

        Примеры:

        >>> ferry = Ferry('Beta', 250, 100)
        >>> ferry.take_on_board(250,50,100)
        (100, 150)
        """
        vacant_seats = capacity - passengers
        if vacant_seats >= plus_passengers:
            vacant_seats -= plus_passengers
            passengers += plus_passengers
            return vacant_seats, passengers
        else:
            raise ValueError('Количество новых пассажиров больше числа свободных мест')

    def disembark(self, capacity: int, passengers: int, minus_passengers: int) -> int:
        """
        Высадить пассажиров

        :param minus_passengers: Количество высаживающихся пассажиров

        Raise ValueError:Если количество высаживающихся пассажиров больше чем
        пассажиров на борту, то вызываем ошибку
        :return: Количество свободных мест, количество пассажиров

        Примеры:

        >>> ferry = Ferry('Beta', 250, 100)
        >>> ferry.disembark(250,100, 50)
        (200, 50)
        """
        vacant_seats = capacity - passengers
        if minus_passengers <= passengers:
            vacant_seats += minus_passengers
            passengers -= minus_passengers
            return vacant_seats, passengers
        else:
            raise ValueError('На борту нет такого количества пассажиров!')


class Dog:

    def __init__(self, breed, name, weight, age):
        """
        Создание и подготовка к работе класса "Собака"

        :param breed: Порода собаки
        :param name: Кличка собаки
        :param weight: Вес собаки
        :param age: Возраст собаки

        Примеры:
        >>> dog_1 = Dog('greyhound', 'Larry', 16.5, 3)#Иницмализация экземпляров класса
        >>> dog_2 = Dog('pekinese', 'Idler', 7.3, 5.5)

        """

        if not isinstance(breed, str):
            raise TypeError('Порода собаки должна быть словом')
        self.breed = breed

        if not isinstance(name, str):
            raise TypeError('Кличка собаки должна быть словом')
        self.name = name

        if not isinstance(weight, (int, float)):
            raise TypeError('Вес собаки должен быть типа int или float')
        if weight <= 0:
            raise ValueError('Вес собаки должен быть положительным числом')
        self.weight = weight

        if not isinstance(age, (int, float)):
            raise TypeError('Возраст собаки должен быть типа int или float')
        if age <= 0:
            raise ValueError('Возраст собаки должен быть положительным числом')
        self.age = age

    def run(self) -> str:
        """
        Функция описыват бегущую собаку

        :return: str

        примеры:
        >>> dog_1 = Dog('greyhound', 'Larry', 16.5, 3)
        >>> dog_1.run()
        'The Greyhound Larry is running.'
        """
        result = f"The {self.breed.capitalize()} {self.name} is running."
        return result

    def sleep(self) -> str:
        """
        Функция описыват спящую собаку

        :return: str

        примеры:
        >>> dog_2 = Dog('pekinese', 'Idler', 7.3, 5.5)
        >>> dog_2.sleep()
        'The Pekinese Idler is sleeping.'
        """
        result = f"The {self.breed.capitalize()} {self.name} is sleeping."
        return result


class Truck:
    def __init__(self, cargo_capacity: float, load: float, fuel_volume: float):
        """
        Создание и подготовка к работе класса "Грузовой автомобиль"

        :param cargo_capacity: Грузоподъёмность
        :param load: Вес груза
        :param fuel_volume: Количество топлива

        Примеры:
        >>> truck = Truck(15000, 200,120)#Иницмализация экземпляра класса
        """

        self.load = None
        self.init_add_load(cargo_capacity, load)

        if not isinstance(cargo_capacity, (int, float)):
            raise TypeError('Грузоподъёмность должна быть числом')
        if cargo_capacity <= 0:
            raise ValueError('Грузоподъёмность должна быть положительным числом')
        self.cargo_capacity = cargo_capacity

        if not isinstance(fuel_volume, (int, float)):
            raise TypeError('Количество топлива должно быть типа int или float')
        if fuel_volume < 0:
            raise ValueError('Количество топлива не может быть отрицательным числом')
        if fuel_volume > 200:
            raise ValueError('Количество топлива не может быть больше чем 200 литров')
        self.fuel_volume = fuel_volume

    def init_add_load(self, cargo_capacity: float, load: float) -> float:
        """
        Функция определяет возможность перевозки данного груза

        :param load: Вес груза
        raise ValueError: Если вес груза больше чем грузоподъёмность автомобиля,,
        то вызываем ошибку

        :return: Вес груза

        Примеры:
        >>> truck= Truck(1500, 200, 120)
        >>> truck.init_add_load(1500, 1200)
        >>> truck.load
        1200

        """
        if not isinstance(load, (int, float)):
            raise TypeError('Вес груза должен быть числом')
        if load < 0:
            raise ValueError('Вес груза не может быть отрицательным числом')
        if cargo_capacity < load:
            raise ValueError('Данный груз слишком тяжёлый')
        self.load = load

    def get_max_range(self, load: float, fuel_volume: float) -> int:
        """
        Метод рассчитывает максимальное расстояние на которое можно
        перевезти груз, используя всё имеющееся топливо.

        :param load: Вес груза
        :param fuel_volume: Количество топлива

        :return:  Максимальное расстояние

        Примеры:
        >>> truck =Truck(15000, 0, 180)
        >>> truck.get_max_range(0, 180)
        1000
        >>> truck.get_max_range(15000, 200)
        416
        """

        empty_truck = 18  # расход топлива порожнего грузовика (л/100 км)
        load_1_kg = 0.002  # дополнительный расход топлива для 1 кг груза

        max_range = fuel_volume / (empty_truck + load_1_kg * load) * 100
        return int(max_range)


if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()
