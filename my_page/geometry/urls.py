
from django.urls import path
from .views import *

urlpatterns = [
    path('rectangle/<int:width>/<int:height>', rectangle, name='rectangle_name'),
    path('square/<int:width>/', square, name='square_name'),
    path('circle/<int:radius>/', circle, name='circle_name'),
    path('get_rectangle_area/<int:width>/<int:height>', get_rectangle_area),
    path('get_square_area/<int:width>/', get_square_area),
    path('get_circle_area/<int:radius>/', get_circle_area),
]
