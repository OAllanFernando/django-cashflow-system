from django.views.generic import TemplateView
# Create your views here.

# Repare aqui Allan, em Python a herança vem como parâmetro
class IndexView(TemplateView):
    template_name = "paginas/index.html"