import pytest

from main import BooksCollector


class TestBooksCollector:

    @pytest.fixture(autouse=True)
    def collector(self):
        self.collector = BooksCollector()

        return self.collector
    
    def test_add_new_book_add_two_books_books_added(self):

        self.collector.add_new_book('Гордость и предубеждение и зомби')
        self.collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        assert len(self.collector.books_genre) == 2

    def test_set_book_genre_when_book_and_genre_exist_genre_is_set(self):

        self.collector.add_new_book('Гордость и предубеждение и зомби')
        self.collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')

        assert self.collector.books_genre['Гордость и предубеждение и зомби'] == 'Ужасы'

    def test_get_book_genre_when_book_in_list_genre_received(self):

        self.collector.add_new_book('Гордость и предубеждение и зомби')
        self.collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')

        assert self.collector.get_book_genre('Гордость и предубеждение и зомби') == 'Ужасы'  

    @pytest.mark.parametrize('genre, expected_books', [
        ['Комедии', ['Что делать, если ваш кот хочет вас убить']],
        ['Фантастика', []]
    ])
    def test_get_books_with_specific_genre_two_genre_received_one_book(self, genre, expected_books):

        self.collector.add_new_book('Гордость и предубеждение и зомби')
        self.collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        self.collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        self.collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Комедии')

        assert self.collector.get_books_with_specific_genre(genre) == expected_books

    def test_get_books_genre_empty_dict(self):
        assert self.collector.books_genre == {}

    @pytest.mark.parametrize('genre, expected_books', [
        ['Детективы', []],
        ['Мультфильмы', ['Гордость и предубеждение и зомби']],
        [None, []]
    ])
    def test_get_books_for_children_return_expected_books(self, genre, expected_books):

        self.collector.add_new_book('Гордость и предубеждение и зомби')
        self.collector.set_book_genre('Гордость и предубеждение и зомби', genre)

        assert self.collector.get_books_for_children() == expected_books

    def test_add_book_in_favorites_one_book_list_with_one_book(self):

            self.collector.add_new_book('Что делать, если ваш кот хочет вас убить')
            self.collector.add_book_in_favorites('Что делать, если ваш кот хочет вас убить')

            assert self.collector.favorites == ['Что делать, если ваш кот хочет вас убить']

    def test_delete_book_from_favorites_one_book_book_deleted(self):

        self.collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        self.collector.add_book_in_favorites('Что делать, если ваш кот хочет вас убить')
        self.collector.delete_book_from_favorites('Что делать, если ваш кот хочет вас убить')

        assert self.collector.favorites == []

    def test_get_list_of_favorites_books_received_two_books(self):

        self.collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        self.collector.add_book_in_favorites('Что делать, если ваш кот хочет вас убить')
        self.collector.add_new_book('Гордость и предубеждение и зомби')
        self.collector.add_book_in_favorites('Гордость и предубеждение и зомби')

        assert self.collector.favorites == ['Что делать, если ваш кот хочет вас убить', 'Гордость и предубеждение и зомби']
        