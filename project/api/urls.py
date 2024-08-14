from django.urls import path
from .views import *


urlpatterns = [
    path('Stu_list/',Stu_list.as_view()),
    path('Stu_details/<int:pk>',Stu_details.as_view())
]
