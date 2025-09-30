from django.urls import path
from .views import project_list, project_detail

urlpatterns = [
    path('', project_list, name='projects'),
    path('<int:pk>/', project_detail, name='project_detail'),
]
