from django.urls import path
from .views import IndexView, SobreView, CriadorView
urlpatterns = [
   path("inicio/", IndexView.as_view(), name="index" ),
   path("sobre/", SobreView.as_view(), name="sobre" ),
   path("criador/", CriadorView.as_view(), name="criador")

]
