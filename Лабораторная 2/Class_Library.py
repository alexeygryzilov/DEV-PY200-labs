BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


class Book:

    def __init__(self, id_: int, name: str, pages: int):
        self.id_ = id_
        self.name = name
        self.pages = pages

    def __str__(self) -> str:
        return f'Книга "{self.name}"'

    def __repr__(self) -> str:
        return f'Book(id_={self.id_!r}, name={self.name!r}, pages={self.pages!r})'


class Library:

    def __init__(self, books=None):
        if not books:
            self.books = []
        else:
            self.books = books

    def get_next_book_id(self) -> int:
        if not self.books:
            id = 1
        else:
            id_list = [Book.id_ for Book in list_books]
            id = id_list[-1] + 1
        return id

    def get_index_by_book_id(self, idx) -> (int, str):
        id_list = [Book.id_ for Book in list_books]
        if idx not in id_list:
            raise ValueError("Книги с запрашиваемым id не существует")
        else:
            count = 0
            for id_ in id_list:
                while id_ != idx:
                    count += 1
                return count


if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
