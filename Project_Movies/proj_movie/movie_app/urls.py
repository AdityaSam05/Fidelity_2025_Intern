from django.urls import path,include
from .views import CreateMov,Movie_list_view,Movdetail,UpdateMov,DeleteMov

urlpatterns = [
    path('create/',CreateMov.as_view()),
    path('list/',Movie_list_view.as_view()),
    path('show/<int:movie_Id>',Movdetail.as_view()),
    path('update/<int:movie_Id>/',UpdateMov.as_view()),
    path('delete/<int:movie_Id>/',DeleteMov.as_view()),
]