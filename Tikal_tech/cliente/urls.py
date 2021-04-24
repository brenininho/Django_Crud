from django.urls import path
from . import views


urlpatterns = [
    # ex: /cliente/
    path('', views.index, name='index'),
    # ex: /cliente/5/
    path('<int:client_id>/', views.detail, name='detail'),
    # ex: /cliente/5/results/
    path('<int:client_id>/results/', views.results, name='results'),
    # ex: /cliente/5/vote/
    path('<int:client_id>/vote/', views.vote, name='vote'),
]
