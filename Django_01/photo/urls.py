from django.urls import path #장고에서 기본으로 제공하는 라이브러리 호출
from . import views #현재 폴더 안에 있는 view를 불러온다는 뜻

urlpatterns = [
    path('', views.photo_list, name='photo_list'),
    path('photo/<int:pk>/', views.photo_detail, name='photo_detail'),
    path('photo/new/', views.photo_post, name='photo_post'),
    path('photo/<int:pk>/edit/', views.photo_edit, name='photo_edit'),
]
