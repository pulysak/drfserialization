from django.urls import path

from . import views

urlpatterns = [
    path('list/', views.StudentListView.as_view(), name='list'),
    path('reverse_list/', views.ReverseStudentJson.as_view(), name='reverse_list'),
]
