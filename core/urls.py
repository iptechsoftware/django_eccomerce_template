from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
    path('product/<slug>/', views.ItemDetailView.as_view(), name='product'),
    path('checkout', views.checkout),
    path('add-to-cart/<slug>/', views.add_to_cart, name='add-to-cart'),
    path('remove-from-cart/<slug>/', views.remove_from_cart, name='remove-from-cart')

]
