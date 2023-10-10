from main import BooksCollector
import pytest


class TestBooksCollector:

    @pytest.fixture
    def collector(self):
        collector = BooksCollector()
        return collector

    def test_add_new_book_add_two_books_result_two_books(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2

    def test_add_new_book_no_genre_result_empty_string(self, collector):
        book_name = 'Гордость и предубеждение и зомби'
        collector.add_new_book(book_name)
        assert collector.get_book_genre(book_name) == ''

    @pytest.mark.parametrize('book_name', ['', 'Книга с названием,где содержится 41символ'])
    def test_add_new_book_add_wrong_name_length_zero_result(self, collector, book_name):
        collector.add_new_book(book_name)
        assert len(collector.get_books_genre()) == 0

    def test_add_new_book_add_the_same_book_twice_result_one_book(self, collector):
        book_name = 'Гордость и предубеждение и зомби'
        collector.add_new_book(book_name)
        collector.add_new_book(book_name)
        assert len(collector.get_books_genre()) == 1

    def test_set_book_genre_add_genre_result_genre_added(self, collector):
        book_name = 'Гордость и предубеждение и зомби'
        genre_name = 'Фантастика'
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre_name)
        assert collector.get_book_genre(book_name) == genre_name

    def test_set_book_genre_for_non_existence_genre_result_empty_string(self, collector):
        book_name = 'Гордость и предубеждение и зомби'
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, 'Придуманный жанр')
        assert collector.get_book_genre(book_name) == ''

    def test_get_book_genre_for_no_added_book_result_none(self, collector):
        book_name = 'Книга, которой нет в self.books_genre'
        collector.set_book_genre(book_name, 'Фантастика')
        assert collector.get_book_genre(book_name) is None

    def test_get_books_with_specific_genre_result_one_book(self, collector):
        book_one_honor = 'Гордость и предубеждение и зомби'
        book_two_cat = 'Что делать, если ваш кот хочет вас убить'
        genre_fantastic = 'Фантастика'
        collector.add_new_book(book_one_honor)
        collector.add_new_book(book_two_cat)
        collector.set_book_genre(book_one_honor, genre_fantastic)
        collector.set_book_genre(book_two_cat, 'Ужасы')
        assert collector.get_books_with_specific_genre(genre_fantastic) == ['Гордость и предубеждение и зомби']

    @pytest.mark.parametrize('book_name, genre', [['', 'Фантастика'], ['Гордость и предубеждение', 'Выдуманный жанр']])
    def test_get_books_with_specific_genre_no_added_book_or_genre_result_empty_list(self, collector, book_name, genre):
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        assert len(collector.get_books_with_specific_genre(genre)) == 0

    def test_get_books_genre_result_dict_of_book(self, collector):
        book_name = 'Гордость и предубеждение и зомби'
        genre_name = 'Фантастика'
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre_name)
        assert collector.get_books_genre() == {book_name: genre_name}

    def test_get_books_for_children_result_one_children_book(self, collector):
        book_one_honor = 'Гордость и предубеждение и зомби'
        book_two_crime = 'Преступление и наказание'
        collector.add_new_book(book_one_honor)
        collector.add_new_book(book_two_crime)
        collector.set_book_genre(book_one_honor, 'Ужасы')
        collector.set_book_genre(book_two_crime, 'Фантастика')
        assert collector.get_books_for_children() == ['Преступление и наказание']

    def test_get_books_for_children_for_no_children_books_result_empty_list(self, collector):
        book_name = 'Гордость и предубеждение и зомби'
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, 'Ужасы')
        assert len(collector.get_books_for_children()) == 0

    def test_add_book_in_favorites_result_one_book(self, collector):
        book_name = 'Гордость и предубеждение и зомби'
        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)
        assert len(collector.get_list_of_favorites_books()) == 1

    def test_add_book_in_favorites_add_the_same_book_twice_result_one_book(self, collector):
        book_name = 'Гордость и предубеждение и зомби'
        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)
        collector.add_book_in_favorites(book_name)
        assert len(collector.get_list_of_favorites_books()) == 1

    def test_delete_book_from_favorites_result_one_book(self, collector):
        book_one_honor = 'Гордость и предубеждение и зомби'
        book_two_crime = 'Преступление и наказание'
        collector.add_new_book(book_one_honor)
        collector.add_new_book(book_two_crime)
        collector.add_book_in_favorites(book_one_honor)
        collector.add_book_in_favorites(book_two_crime)
        collector.delete_book_from_favorites(book_one_honor)
        assert collector.get_list_of_favorites_books() == ['Преступление и наказание']

    def test_delete_book_from_favorites_with_no_favorites_result_empty_list(self, collector):
        collector.delete_book_from_favorites('Гордость и предубеждение и зомби')
        assert len(collector.get_list_of_favorites_books()) == 0

    def test_get_list_of_favorites_books_with_no_books_result_empty_list(self, collector):
        assert len(collector.get_list_of_favorites_books()) == 0
