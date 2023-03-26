from abc import ABC, abstractmethod
from exeptions import *


class Storage(ABC):  # абстрактный класс

    @abstractmethod
    def add(self, name, count):
        pass

    @abstractmethod
    def remove(self, name, count):
        pass

    @abstractmethod
    def get_free_space(self):
        pass

    @abstractmethod
    def get_items(self):
        pass

    @abstractmethod
    def get_unique_items_count(self):
        pass


class BaseStorage(Storage):  # базовый класс хранилища
    def __init__(self, items, capacity):
        self.items = items
        self.capacity = capacity

    def add(self, name, count):
        available_count = self.get_free_space()  # получаеим доступное место

        if available_count < count:  # вызываем исключение если места неостаточно
            raise NotSpaceRequired

        if name in self.items.keys():
            self.items[name] += count  # увеличиваем количество имеющегося товара
        else:
            self.items[name] = count  # добавляем новый товар

    def remove(self, name, count):
        if not self.items.get(name):  # вызываем исключение, если товар не отсутствует
            raise NotRequiredPosution
        else:
            if self.items.get(name) > count:
                self.items[name] -= count  # уменьшаем товар
            elif self.items.get(name) == count:
                self.items.pop(name)  # удаляем товар, если остаток равен 0
            else:
                raise NotRequiredCountAvailable  # вызываем исключени, если товара не достаточно

    def get_free_space(self):
        return self.capacity - sum(self.items.values())  # считаем свободное место

    def get_items(self):
        return self.items  # возвращаем словарь продуктов с количеством

    def get_unique_items_count(self):
        return len(set(self.items.keys()))  # определяем количество уникальных позиций


class Store(BaseStorage):  # класс ля складов
    def __init__(self, items, capacity=100):
        super().__init__(items, capacity)


class Shop(BaseStorage): # класс для магазинов
    def __init__(self, items, capacity=100):
        super().__init__(items, capacity)

    def add(self, name, count):  # переинициализируем метод родительского класса
        if self.get_unique_items_count() >= 5:
            raise ToManyPositions

        super().add(name, count)  # вызываем метод родительского класса


class Request:  # класс для запросов
    def __init__(self, str_req, storages):
        route = str_req.split(' ')  # разделяем запрос на слова
        if len(route) != 7:  # вызываем исключение если количество слов отлично от 7
            raise RequestError

        if not route[1].isdigit() and int(route[1] <= 0):  # вызываем исключение если количество товара не цифра
            # и не положительное

            raise RequestError
        if route[4] not in storages.keys() and route[6] not in storages.keys():  # вызываем исключение ели
            # нет существующего склада и магазина в запросе
            raise NotPointForRequest

        self.from_ = route[4]
        self.to = route[6]
        self.amount = int(route[1])
        self.product = route[2]



    def __repr__(self):
        return f"from {self.from_} to {self.to} {self.amount} {self.product}"



