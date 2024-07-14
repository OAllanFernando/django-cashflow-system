from django.urls import path
from.views import CidadeCreate, CidadeUpdate
from.views import EstadoCreate, EstadoUpdate

urlpatterns = [
    path('cadastrar/estado/', EstadoCreate.as_view(), name='cadastrar-estado'),
    path('editar/estado/<int:pk>/', EstadoUpdate.as_view(), name='editar-estado'),
    path('cadastrar/cidade/', CidadeCreate.as_view(), name='cadastrar-cidade'),
    path('editar/cidade/<int:pk>/', CidadeUpdate.as_view(), name='editar-cidade'),
    
]

