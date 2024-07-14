from django.views.generic import TemplateView
# Create your views here.

# Repare aqui Allan, em Python a herança vem como parâmetro
class IndexView(TemplateView):
    template_name = "paginas/index.html"


class SobreView(TemplateView):
    template_name = "paginas/sobre.html"

class CriadorView(TemplateView):
    template_name = "paginas/criador.html"
