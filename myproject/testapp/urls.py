from django.urls import path

from . import views



urlpatterns = [
    #path("", views.index, name='index'),
    path("", views.IndexListView.as_view(), name='task_views'),
    path("create/", views.TackCreate.as_view(), name='create_task'),
    path("new/", views.new_task, name='new_task'),
    path("new_client/", views.new_client, name='new_client'),

]
