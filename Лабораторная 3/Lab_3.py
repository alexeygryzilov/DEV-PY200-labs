from typing import Union

class Book:
    """ Базовый класс книги. """

    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, new_name: str) -> None:
        if not isinstance(new_name, str):
            raise TypeError('Название книги должно быть типа "int"')
        self._name = new_name

    @property
    def author(self) -> str:
        return self._author

    @author.setter
    def author(self, new_author: str) -> None:
        if not isinstance(new_author, str):
            raise TypeError('Имя автора должно быть типа "int"')
        self._author = new_author


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages

    def __str__(self):
        return f"Бумажная книга: Название {self.name}. Автор {self.author}. Количество страниц {self.pages}"

    @property
    def name(self) -> str:
        return super().name

    @name.setter
    def name(self, value) -> None:
        raise AttributeError('Невозможно изменить атрибут "name" в классе "PaperBook".')

    @property
    def author(self) -> str:
        return super().author

    @author.setter
    def author(self, value) -> None:
        raise AttributeError('Невозможно изменить атрибут "author" в классе "PaperBook".')

    @property
    def pages(self) -> int:
        return self._pages

    @pages.setter
    def pages(self, new_pages: int) -> None:
        if not isinstance(new_pages, int):
            raise TypeError('Количество станиц должно быть типа "int".')
        elif new_pages <= 0:
            raise ValueError('Количество станиц должно быть положительным числом.')
        self._pages = new_pages


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: Union[int, float]):
        super().__init__(name, author)
        self.duration = duration

    @property
    def name(self) -> str:
        return super().name

    @name.setter
    def name(self, value) -> None:
        raise AttributeError('Невозможно изменить атрибут "name" в классе "AudioBook".')

    @property
    def author(self) -> str:
        return super().author

    @author.setter
    def author(self, value) -> None:
        raise AttributeError('Невозможно изменить атрибут "author" в классе "AudioBook".')

    @property
    def duration(self) -> float:
        return self._duration

    @duration.setter
    def duration(self, new_duration) -> None:
        if not isinstance(new_duration, (int, float)):
            raise TypeError('Продолжительность аудиокниги должна быть типа "int" или "float".')
        elif new_duration <= 0:
            raise ValueError('Продолжительность аудиокниги должна быть положительным числом.')
        self._duration = new_duration

    def __str__(self):
        return f"Электронная книга: Название {self.name}. Автор {self.author}. Продолжительность {self.duration} сек"


if __name__ == '__main__':
    book_1 = Book('Полтава', 'А.С.Пушкин')
    print(book_1.__repr__())
    print(book_1)
    book_2 = PaperBook('Полтава', 'А.С.Пушкин', 88)
    print(book_2.__repr__())
    print(book_2)
    book_3 = AudioBook('Мцыри', 'М.Ю.Лермонтов', 3256.55)
    print(book_3)
    #   book_2.name = 'Метель'  # AttributeError: Невозможно изменить атрибут "name" в классе "PaperBook".
    #   book_2.pages = 32.56  #TypeError: Количество станиц должно быть типа "int".
    book_3.duration = -3300  # ValueError: Продолжительность аудиокниги должна быть положительным числом.
