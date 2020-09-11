from django.conf.urls import url
from django.urls import path

from vote import views

urlpatterns = [
    path('<int:question_id>/',views.detail,name="detail"),
    path('<int:question_id>/results',views.results,name="results"),
    path('<int:question_id>/vote/',views.vote,name="vote"),
]