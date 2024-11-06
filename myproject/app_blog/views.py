from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'app_blog/index.html'  # Шлях до шаблону
