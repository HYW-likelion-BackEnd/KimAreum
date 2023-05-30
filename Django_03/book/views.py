from rest_framework import viewsets, permissions, generics, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
#from rest_framework.views import APIView

from .models import Book
from .serializers import BookSerializer

#함수형 View
@api_view(['Get', 'POST'])
def booksAPI(request) :
    if request.method == "GET" : #들어오는 요청
        books = Book.objects.all() #모든 정보를 다 가져옴
        serializer = BookSerializer(books, many=True) #many=True > 여러 데이터에 대한 처리를 하는 옵션
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == "POST" : #도서 정보를 등록, 역직렬화
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid() :
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED) #201 생성을 했다는 메세지 리턴
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) #에러 발생 시 400 메세지로 에러 구문 보냄

@api_view(['GET']) #get 요청을 처리하게 하는 데코레이터
def bookAPI(request, bid) : #bid를 통해서 특정 책의 데이터를 가져옴
    book = get_object_or_404(Book, bid=bid) #데이터를 Book 모델에 가져오는데 만약 해당하는 데이터가 없으면 404 오류
    serializer = BookSerializer(book) #직렬화 과정
    return Response(serializer.data, status=status.HTTP_200_OK) #데이터를 반환하고 200 메세지를 보내면서 데이터를 가져오는 데 성공

# #클래스형 View / 두 가지 차이점 비교해서 쓰기 벨로그에!!
# class BooksAPI(APIView) :
#     def get(self, request) :
#         books = Book.objects.all()
#         serializer = BookSerializer(books, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     def post(self, request) :
#         serializer = BookSerializer(data=request.data)
#         if serializer.is_valid() :
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
# class BookAPI(APIView) :
#     def get(self, request, bid) :
#         book = get_object_or_404(Book, bid=bid)
#         serializer = BookSerializer(book)
#         return Response(serializer.data, status=status.HTTP_200_OK)