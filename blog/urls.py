from django.urls import path
from .views import BlogList, BlogDetail

urlpatterns = [
    path('', BlogList.as_view()),
    path('<int:pk>/', BlogDetail.as_view()),

]