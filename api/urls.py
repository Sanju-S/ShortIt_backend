from django.urls import path
from . import views

urlpatterns = [
    path('', views.AllLinkView.as_view(), name="all_links"),
    path('create/', views.GetShortLinkView.as_view(), name="get_short_link"),
    path('get/', views.GetFullLinkView.as_view(), name="get_full_link"),
    path('custom/', views.GetCustomLinkView.as_view(), name='get_custom_link'),
]
