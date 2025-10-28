"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views
from app.views import (
    ProjectViewSet,
    TaskViewSet,
    BulkCreateTasksView,
    BulkUpdateTasksView,
    BulkDeleteTasksView,
    notify_sending_view,
)
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('projects', ProjectViewSet)
router.register('tasks', TaskViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add/', notify_sending_view, name='add'), 
    *router.urls,
    path('tasks/bulk-create/', BulkCreateTasksView.as_view(), name='bulk-create-tasks'),
    path('tasks/bulk-update/', BulkUpdateTasksView.as_view(), name='bulk-update-tasks'),
    path('tasks/bulk-delete/', BulkDeleteTasksView.as_view(), name='bulk-delete-tasks'),

]


router = DefaultRouter()
router.register('projects', ProjectViewSet)
router.register('tasks', TaskViewSet)

urlpatterns = [
    *router.urls,
    path('tasks/bulk-create/', BulkCreateTasksView.as_view()),
    path('tasks/bulk-update/', BulkUpdateTasksView.as_view()),
    path('tasks/bulk-delete/', BulkDeleteTasksView.as_view()),
]
