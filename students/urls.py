from django.urls import path

from students import views

app_name = "student"
urlpatterns = [
    path('insert/', views.insert),
    path('list/<int:class_id>/', views.students, name='student'),
    path('classes/', views.classes, name='classes'),
    path('gender/', views.gender, name='gender'),
    path('add/', views.add, name='add'),
    path('delete', views.delete, name='delete'),

]
