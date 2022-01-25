from django.urls import path, re_path

from catalog import views

urlpatterns = [
    path('', views.index, name='index'),
    path('fighters/', views.FighterListView.as_view(), name='fighters'),
    re_path('^fighter/(?P<pk>\d+)$', views.FighterDetailView.as_view(), name='fighter-detail')

]