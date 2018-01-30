# socialauth/views.py
from django.views.generic import TemplateView
from products.models import Products

class HomePageView(TemplateView):

    template_name = 'base.html'

    def products(self):
        return Products.objects.all()
