import pytest


# Тесты для метода add_new_book
def test_add_new_book(collector):
    collector.add_new_book("Книга 1")
    assert "Книга 1" in collector.get_books_genre()

# Тесты для метода set_book_genre
@pytest.mark.parametrize("book_name, genre, expected_genre", [
    ("Книга 1", "Фантастика", "Фантастика"),  # Обычный случай установки жанра
    ("Книга 1", "Неверный жанр", ""),         # Неверный жанр
    ("Несуществующая книга", "Фантастика", None),  # Не существует книги
])
def test_set_book_genre(collector, book_name, genre, expected_genre):
    collector.add_new_book("Книга 1")
    collector.set_book_genre(book_name, genre)
    assert collector.get_book_genre(book_name) == expected_genre

# Тесты для метода get_books_with_specific_genre
@pytest.mark.parametrize("genre, expected_books", [
    ("Фантастика", ["Книга 1", "Книга 2"]),  # Книги с жанром Фантастика
    ("Ужасы", []),                           # Нет книг с жанром Ужасы
    ("Неверный жанр", [])                    # Неверный жанр
])
def test_get_books_with_specific_genre(collector, genre, expected_books):
    collector.add_new_book("Книга 1")
    collector.add_new_book("Книга 2")
    collector.set_book_genre("Книга 1", "Фантастика")
    collector.set_book_genre("Книга 2", "Фантастика")
    assert collector.get_books_with_specific_genre(genre) == expected_books

# Тест для метода get_books_genre
def test_get_books_genre(collector):
    collector.add_new_book("Книга 1")
    collector.set_book_genre("Книга 1", "Фантастика")
    assert collector.get_books_genre() == {"Книга 1": "Фантастика"}

# Тест для метода get_books_for_children
def test_get_books_for_children(collector):
    collector.add_new_book("Книга 1")
    collector.add_new_book("Книга 2")
    collector.set_book_genre("Книга 1", "Фантастика")
    collector.set_book_genre("Книга 2", "Ужасы")
    assert collector.get_books_for_children() == ["Книга 1"]

# Тест для метода add_book_in_favorites
def test_add_book_in_favorites(collector):
    collector.add_new_book("Книга 1")
    collector.add_book_in_favorites("Книга 1")
    assert collector.get_list_of_favorites_books() == ["Книга 1"]

# Тест для метода delete_book_from_favorites
def test_delete_book_from_favorites(collector):
    collector.add_new_book("Книга 1")
    collector.add_book_in_favorites("Книга 1")
    collector.delete_book_from_favorites("Книга 1")
    assert collector.get_list_of_favorites_books() == []

# Тест для метода get_list_of_favorites_books
def test_get_list_of_favorites_books(collector):
    collector.add_new_book("Книга 1")
    collector.add_book_in_favorites("Книга 1")
    assert collector.get_list_of_favorites_books() == ["Книга 1"]