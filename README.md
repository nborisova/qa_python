# qa_python

**В файле test_main.py представлены 1 фикстура и 9 тестов, проверяющие методы класса BooksCollector:**

1. Фикстура ```collector``` – создает объект класса ```BooksCollector```  
2. Тест ```test_add_new_book_add_two_books_books_added``` – проверяет, что метод ```add_new_book``` добавил 2 книги в словарь  
3. Тест ```test_set_book_genre_when_book_and_genre_exist_genre_is_set``` – проверяет, что метод ```set_book_genre``` установил жанр для добавленной книги  
4. Тест ```test_get_book_genre_when_book_in_list_genre_received``` – проверяет, что метод ```get_book_genre``` возвращает жанр по названию книги  
5. Тест ```test_get_books_with_specific_genre_two_genre_list_received_with_one_book``` – проверят, что метод ```get_books_with_specific_genre``` возвращает фильм с определенным жанром  
6. Тест ```test_get_books_genre_empty_dict``` – проверяет, что метод ```get_books_genre``` возвращает словарь ```books_genre```  
7. Тест ```test_get_books_for_children_book_in_age_rating_empty_list``` – проверяет, что метод ```get_books_for_children``` **не** возвращает фильмы, чей жанр не входит в детскую возрастную категорию  
8. Тест ```test_add_book_in_favorites_one_book_list_with_one_book``` – проверяет, что метод ```add_book_in_favorites``` добавляет книгу в список ```favorites```  
9. Тест ```test_delete_book_from_favorites_one_book_book_deleted``` – проверяет, что метод ```delete_book_from_favorites``` удаляет книгу из списка ```favorites```  
10. Тест ```test_get_list_of_favorites_books_received_two_books``` – проверяет, что метод ```get_list_of_favorites``` возвращает названия книг, которые были добавлены в список ```favorites```  
