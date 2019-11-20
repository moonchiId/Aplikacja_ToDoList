from django.urls import path
from . import views
from django.conf.urls import url


urlpatterns = [
    path('', views.home, name='home'),
    path('delete/<list_id>', views.delete, name='delete'),
    path('done/<list_id>', views.done, name='done'),
    path('not_done/<list_id>', views.not_done, name='not_done'),
    path('edit/<list_id>', views.edit, name='edit'),
    url('about/', views.about, name='about'),

]
