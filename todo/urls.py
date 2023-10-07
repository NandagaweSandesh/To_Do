from  . import views
from django.urls import  path


urlpatterns = [
    

    #ADD TASK
    path('add_task/', views.addTask, name= 'addTask'),
    #MARK AS DONE
    path('mark_as_done/<int:pk>/', views.mark_as_done, name= 'mark_as_done'),
    #EDIT TASK
    path('edit_task/<int:pk>/', views.edit_task, name= 'edit_task'),
    #DELETE TASK
    path('delete_task/<int:pk>/', views.delete_task, name= 'delete_task'),
    #UNDO TASK
    path('undo_task/<int:pk>/', views.undo_task, name= 'undo_task'),

]