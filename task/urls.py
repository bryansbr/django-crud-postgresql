from django.urls import path
from .views import list_tasks, create_task, update_task, delete_task

urlpatterns = [
  path('', list_tasks),
  path('create/', create_task, name='create_task'),
  path('update/<int:id>/', update_task, name='update_task'), # Future functionality...
  path('delete/<int:id>/', delete_task, name='delete_task'),
]