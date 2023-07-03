from django.urls import path
from . import views
urlpatterns = [
    path('',views.hellaw_main,name='hellaw_main'),
    path('board/',views.board_postList, name='board_postList'),
    path('board/<int:pk>/',views.board_detail, name='board_detail'),
    path('board/post/',views.board_post,name='board_post'),
    path('board/<int:pk>/edit/',views.board_edit, name='board_edit'),
    path('login/',views.login,name='login')
]