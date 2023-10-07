from  . import views
from django.urls import  path


urlpatterns = [
    

    #ADD TASK
    path('add_task/', views.addTask, name= 'addTask'),
]