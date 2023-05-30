#클래스형부터 url 연결
#from django.urls import path
#from .views import BookAPI, BooksAPI

#함수형 url 연결
from django.urls import path
from .views import bookAPI, booksAPI

# urlpatterns = [
#     path('cbv/books/', BooksAPI.as_view()),
#     path('cbv/book/<int:bid>/', BookAPI.as_view()),
# ]

urlpatterns = [
    path('fbv/books/', booksAPI),
    path('fbv/book/<int:bid>/', bookAPI),
]