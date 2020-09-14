from django.urls import path

from students import views

app_name = "student"
urlpatterns = [
    path('insert/', views.insert),
    path('list/<int:class_id>/', views.students, name='student'),
    path('classes/', views.classes, name='classes'),

]