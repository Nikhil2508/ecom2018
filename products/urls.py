from django.urls import path
from .views import ProductDetailView


urlpatterns = [
    path(r'^(?P<pk>\d+)$', ProductDetailView.as_view() , name='product_detail')
]
