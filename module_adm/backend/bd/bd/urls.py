from django.urls import path
from administration import views

urlpatterns = [
    path('', views.index, name='index'),  # Esta línea manejará la solicitud a la raíz del sitio
    path('collaborators/', views.get_collaborators, name='get_collaborators'),
    path('collaborators/<int:collaborator_id>/', views.get_collaborator, name='get_collaborator'),
    path('collaborators/create/', views.create_collaborator, name='create_collaborator'),
    path('collaborators/<int:collaborator_id>/update/', views.update_collaborator, name='update_collaborator'),
    path('collaborators/<int:collaborator_id>/delete/', views.delete_collaborator, name='delete_collaborator'),
]

