from django.views.generic import TemplateView
from braces.views import GroupRequiredMixin
# Create your views here.

# Repare aqui Allan, em Python a herança vem como parâmetro
class IndexView(TemplateView):
    template_name = "paginas/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Página Inicial"
        return context

class SobreView(TemplateView):
    template_name = "paginas/sobre.html"

class CriadorView(TemplateView):
    template_name = "paginas/criador.html"
    
    
