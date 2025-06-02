from django.urls import path
from . import views

app_name = 'todos'

urlpatterns = [
    path('', views.tasks, name='tasks'),
    path('done/<int:id>/', views.task_done, name='done')
]