from django.urls import path

from . import views

app_name = "polls"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:question_id>/", views.detail, name="detail"),
    path("<int:question_id>/results/", views.results, name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
    path('create/', views.new_poll,name='create'),
    path('<int:question_id>/delete',views.delete_poll,name='delete_poll'),
    path('<int:question_id>/add_choice/', views.add_choice, name='add_choice'),
    path('choice/<int:choice_id>/delete',views.delete_choice, name='delete_choice'),

]