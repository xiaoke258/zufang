from django.urls import path,re_path
from app01 import views

urlpatterns = [
    path('db/', views.db_test,name='main'),
    path('book/', views.book,name='book'),
    path('add_book/', views.add,name='add_book'),
    path(r'edit_book/(?<book_id>\d+)/', views.edit,name='edit_book'),
    path(r'delete_book/(?<book_id>\d+)/', views.delete,name='delete_book'),
]
