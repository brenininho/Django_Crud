from django.urls import path
from . import views


app_name = 'cliente'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>/', views.cliente, name='cliente'),
    path('novo', views.cliente, name='cliente_novo'),
    path('<int:pk>/delete', views.delete, name='cliente_delete')

]