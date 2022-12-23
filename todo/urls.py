from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name='api-overview'),
    path('list', views.taskList, name='task-list'),
    path('detail/<str:pk>', views.detailView, name='detail-view'),
    path('create', views.createTask, name='create-task'),
    path('update/<int:pk>', views.updateTask, name='update-task'),
    path('delete/<int:pk>', views.deleteTask, name='delete-task'),
]
