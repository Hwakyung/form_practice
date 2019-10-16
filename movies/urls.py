from django.urls import path,include
from . import views
app_name= 'movies'
urlpatterns = [
    path('', views.index, name='index'),

    path('create/', views.create, name='create'),
    path('<int:id>/detail', views.detail, name='detail'),
    path('<int:id>/create/comment', views.create_comment, name='create_comment'),
]
