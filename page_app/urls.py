from django.urls import path
from page_app.views import index, contato, footer, header, home, services

urlpatterns = [
    # Cadastrar URLs aqui
    path('', index),

    path('contato/', contato),
    path('footer/', footer),
    path('header/', header),
    path('home/', home), 
    path('services/', services),
]