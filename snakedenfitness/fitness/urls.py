from . import views
from django.urls import path

urlpatterns = [
    path('', views.fitness_home, name="fitness_home"),
    path('trainer/', views.trainer_home, name="trainer_home"),
    path('workout_form/', views.workout_form, name="workout_form"),
    path('request_trainer/', views.request_trainer, name="request_trainer"),
    path('delete_workout/<int:id>', views.delete_workout, name="delete_workout"),
    path('edit_workout/<int:id>', views.edit_workout, name="edit_workout"),

    path('workout_log/', views.user_workout_data, name="user_workout_data"),
    path('trainer_workout_log/', views.trainer_workout_data, name="trainer_workout_data"),
    path('add_client/', views.add_client, name='add_client'),
    path('add_client_form/', views.clientTrainer_form, name="add_client_form"),
    path('update_client_form/', views.clientTrainer_update, name="update_client_form"),
    path('delete_client_form/<client_id>', views.clientTrainer_delete, name="delete_client_form"),
]